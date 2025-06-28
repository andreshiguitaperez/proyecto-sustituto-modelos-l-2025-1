"""
API REST con Flask que expone dos endpoints:
- /predict: recibe una imagen DICOM y devuelve la probabilidad de cáncer.
- /train: lanza el proceso de entrenamiento con los datos estándar.
"""

from flask import Flask, request, jsonify
import os
from pathlib import Path
import tempfile
from fastai.vision.all import load_learner
from helpers import dcm_to_image, get_dcm_path, get_x_wrapper
import subprocess

app = Flask(__name__)

# Ruta base del proyecto (dentro del contenedor)
path = Path('/app')

# Cargar el modelo al iniciar la API
model_path = path / 'export.pkl'
learn = load_learner(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Recibe un archivo DICOM y devuelve la probabilidad de cáncer.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró ningún archivo DICOM.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío.'}), 400

    try:
        # Guardar el archivo en un archivo temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix='.dcm') as temp_file:
            file.save(temp_file.name)
            img = dcm_to_image(temp_file.name)
            pred, _, probs = learn.predict(img)
            probability = float(probs[1])  # Probabilidad de clase "cáncer"
        os.unlink(temp_file.name)  # Eliminar archivo temporal
        return jsonify({'probability': probability})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/train', methods=['POST'])
def train():
    """
    Ejecuta el script de entrenamiento.
    """
    try:
        result = subprocess.run(
            ['python', 'train.py'],
            cwd=path,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            return jsonify({
                'error': result.stderr,
                'stdout': result.stdout
            }), 500
        return jsonify({
            'message': 'Entrenamiento completado exitosamente.',
            'stdout': result.stdout
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
