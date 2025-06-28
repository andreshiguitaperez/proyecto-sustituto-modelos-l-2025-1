"""
Cliente Python para consumir la API REST desplegada en Docker.
- Realiza una predicción enviando una imagen DICOM.
- Inicia el entrenamiento remoto del modelo.
"""

import requests

# Dirección del contenedor (ajusta si usas Docker Desktop, WSL o puerto diferente)
BASE_URL = "http://localhost:5000"

def predict_dicom(dcm_path):
    """
    Envía una imagen DICOM al endpoint /predict y devuelve la probabilidad de cáncer.
    """
    with open(dcm_path, 'rb') as f:
        files = {'file': (dcm_path, f, 'application/dicom')}
        response = requests.post(f"{BASE_URL}/predict", files=files)
    
    if response.status_code == 200:
        print("✅ Predicción exitosa")
        print("Probabilidad de cáncer:", response.json()["probability"])
    else:
        print("❌ Error en la predicción:", response.status_code)
        print(response.text)

def train_model():
    """
    Llama al endpoint /train para entrenar el modelo.
    """
    response = requests.post(f"{BASE_URL}/train")
    
    if response.status_code == 200:
        print("✅ Entrenamiento iniciado correctamente")
        print(response.json()["message"])
        print("🔍 Logs del entrenamiento:\n")
        print(response.json()["stdout"])
    else:
        print("❌ Error al iniciar entrenamiento:", response.status_code)
        print(response.text)

# 🧪 Ejemplo de uso
if __name__ == "__main__":
    # Reemplaza con la ruta a una imagen DICOM real que tengas localmente
    test_dcm_path = "/home/andres_udem/Documents/PruebaFuncionamiento/proyecto-sustituto-modelos-l-2025-1/fase-3/imagenesPrueba/68070693.dcm"

    print("\n--- Realizando predicción ---")
    predict_dicom(test_dcm_path)

    print("\n--- Iniciando entrenamiento ---")
    try:
        train_model()
    except Exception as e:
        print("❌ Excepción al llamar a /train:", e)
