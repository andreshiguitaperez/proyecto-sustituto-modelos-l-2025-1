import requests
import argparse

# Dirección del contenedor (ajusta si es necesario)
BASE_URL = "http://localhost:5000"

def predict_dicom(dcm_path):
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
    response = requests.post(f"{BASE_URL}/train")
    if response.status_code == 200:
        print("✅ Entrenamiento iniciado correctamente")
        print(response.json()["message"])
        print("\n📄 Logs del entrenamiento:\n")
        print(response.json().get("stdout", "(sin logs)"))
    else:
        print("❌ Error al iniciar entrenamiento:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente API cáncer de mama")
    parser.add_argument("dicom_path", help="Ruta al archivo DICOM a predecir")
    args = parser.parse_args()

    print("\n--- Realizando predicción ---")
    predict_dicom(args.dicom_path)

    print("\n--- Iniciando entrenamiento ---")
    try:
        train_model()
    except Exception as e:
        print("❌ Excepción al llamar a /train:", e)
