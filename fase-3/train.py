# train.py
"""
Entrena un modelo de clasificación de imágenes DICOM para detección de cáncer de mama.
Guarda el modelo entrenado como 'export.pkl'.
"""

from fastai.vision.all import *
import pandas as pd
from pathlib import Path
from helpers import get_x, get_y, get_dcm_path

# Esta es la ruta base del proyecto
path = Path('./')

# Se cargan datos y filtran imágenes que existen en disco
df = pd.read_csv(path/'train.csv')
df_filtered = df[df['image_id'].apply(lambda x: get_dcm_path(x, path, 'train_images') is not None)].reset_index(drop=True)

# Esta es una funcion auxiliar para obtener imágenes
def get_x_wrapper(row):
    return get_x(row, path)

# Se define el DataBlock con transformaciones y partición de validación
dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_x=get_x_wrapper,
    get_y=get_y,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    item_tfms=Resize(224)
)

# Se crean dataloaders y definir el modelo con resnet18
dls = dblock.dataloaders(df_filtered, bs=16)
learn = vision_learner(dls, resnet18, metrics=accuracy)

# Se entrena el modelo con fine-tuning
learn.fine_tune(2)

# Se exporta el modelo entrenado
learn.export('export.pkl')
print("✅ Modelo exportado como export.pkl")