FROM python:3.10-slim

# Evitar que Python genere archivos .pyc y forzar logs inmediatos
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y python3-gdcm gcc unzip wget && \
    apt-get clean

# Crea carpeta de trabajo
WORKDIR /app

# Copia todos los archivos del proyecto (scripts, helpers, etc.)
COPY . /app

# Instala las librerías de Python necesarias
RUN pip install --no-cache-dir torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir fastai==2.7.12 pydicom==2.4.4 numpy==1.24.4 matplotlib pandas \
    pylibjpeg pylibjpeg-libjpeg gdown flask

# Descarga y descomprime imágenes desde Google Drive
RUN gdown https://drive.google.com/uc?id=1vYsO0iBUbnyWE7_IIkCQXabv7h2Worm5 -O train_images.zip && \
    unzip train_images.zip -d ./ && \
    rm train_images.zip && \
    chmod -R 755 /app/train_images

RUN gdown https://drive.google.com/uc?id=1la2PpHnK-hHQSh19xdkeqwrsGA3Yyj0M -O test_images.zip && \
    unzip test_images.zip -d ./ && \
    rm test_images.zip && \
    chmod -R 755 /app/test_images

# Expone el puerto 5000 para la API Flask
EXPOSE 5000

# Comando por defecto: ejecuta la API REST
CMD ["python", "apirest.py"]
