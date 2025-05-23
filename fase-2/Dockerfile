FROM python:3.10-slim

# Evito que python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalo las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y python3-gdcm gcc unzip wget && \
    apt-get clean

# Creo la carpeta principal de trabajo
WORKDIR /app

# Copio los archivos del proyecto
COPY . /app

# Instala las librerías de Python ya utilizadas en el notebook
RUN pip install --no-cache-dir torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir fastai==2.7.12 pydicom==2.4.4 numpy==1.24.4 matplotlib pandas \
    pylibjpeg pylibjpeg-libjpeg gdown

# Descargo y descomprimo train_images.zip desde Google Drive publico
RUN gdown https://drive.google.com/uc?id=1vYsO0iBUbnyWE7_IIkCQXabv7h2Worm5 -O train_images.zip && \
    unzip train_images.zip -d ./ && \
    rm train_images.zip && \
    chmod -R 755 /app/train_images

# Descargo y descomprimo test_images.zip desde Google Drive publico
RUN gdown https://drive.google.com/uc?id=1la2PpHnK-hHQSh19xdkeqwrsGA3Yyj0M -O test_images.zip && \
    unzip test_images.zip -d ./ && \
    rm test_images.zip && \
    chmod -R 755 /app/test_images

# Comando por defecto
CMD ["bash"]