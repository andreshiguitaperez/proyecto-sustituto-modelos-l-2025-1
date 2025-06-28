# helpers.py
"""
Funciones auxiliares para cargar y procesar imágenes DICOM,
así como para obtener las entradas y etiquetas desde un DataFrame.
"""

from fastai.vision.all import *
import pydicom
from pathlib import Path
import numpy as np

def dcm_to_image(dcm_path):
    """
    Convierte un archivo DICOM en una imagen PIL normalizada.
    """
    dcm = pydicom.dcmread(dcm_path)
    img = dcm.pixel_array.astype(np.float32)
    img = (img - np.min(img)) / (np.max(img) - np.min(img))
    return PILImage.create((img * 255).astype(np.uint8))

def get_dcm_path(image_id, base_path, folder_name):
    """
    Busca el archivo DICOM correspondiente a un ID dentro de una carpeta.
    """
    search_path = base_path / folder_name
    matches = list(search_path.rglob(f"{image_id}.dcm"))
    return matches[0] if matches else None

def get_x(row, base_path):
    """
    Obtiene la imagen correspondiente a una fila del DataFrame.
    """
    p = get_dcm_path(row['image_id'], base_path, 'train_images')
    if p is not None:
        return dcm_to_image(p)
    else:
        raise FileNotFoundError(f"No se encontró la imagen para ID: {row['image_id']}")

def get_x_wrapper(row):
    """
    Versión simplificada de get_x que usa una variable global `path`.
    """
    return get_x(row, path)

def get_y(row):
    """
    Retorna la etiqueta (columna 'cancer') de una fila del DataFrame.
    """
    return row['cancer']