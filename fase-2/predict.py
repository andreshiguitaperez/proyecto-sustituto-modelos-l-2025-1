# predict.py
"""
Genera predicciones de cáncer a partir de imágenes DICOM usando un modelo entrenado.
Guarda los resultados en un archivo CSV llamado 'submission.csv'.
"""

from fastai.vision.all import *
import pandas as pd
from pathlib import Path
from helpers import dcm_to_image, get_dcm_path

# Ruta base dentro del contenedor
path = Path('/app')

# Cargar datos de prueba y modelo entrenado
df_test = pd.read_csv(path/'test.csv')
learn = load_learner(path/'export.pkl')

def predict_image(image_id):
    """
    Genera la probabilidad de cáncer para una imagen dada.
    """
    dcm_path = get_dcm_path(image_id, path, 'test_images')
    if dcm_path:
        img = dcm_to_image(dcm_path)
        pred, _, probs = learn.predict(img)
        return probs[1].item()  # Probabilidad de clase "cáncer"
    else:
        return 0.0  # Devuelve 0.0 si no se encuentra la imagen

# Generar predicciones y guardarlas
df_test['cancer'] = df_test['image_id'].apply(predict_image)
df_test[['image_id', 'cancer']].to_csv(path/'submission.csv', index=False)
print("✅ Archivo de predicciones guardado como submission.csv")