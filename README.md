# **proyecto-sustituto-modelos-l-2025-1**

## **Modelos l - Proyecto Sustituto (2025-1)**

Andres Dario Higuita Perez - C.C: 1022099411 - adario.higuita@udea.edu.co

### **Basado en Proyecto de Kaggle:**

**Competición:**
https://www.kaggle.com/competitions/rsna-breast-cancer-detection/code?competitionId=39272&sortBy=voteCount&excludeNonAccessedDatasources=true

**NoteBook:**
https://www.kaggle.com/code/radek1/eda-training-a-fast-ai-model-submission


**Profesor: RAUL RAMOS POLLAN correo: raul.ramos@udea.edu.co**

**Monitor: JONATHAN GRANDA correo: jonathan.granda@udea.edu.co**

**UNIVERSIDAD DE ANTIOQUIA**


## **PROYECTO PREDICTIVO DE CANCER DE MAMA**
*Hacer clic para desplegar contenido por fase...*
<details style="margin-left: 20px; border: 1px solid #ccc; padding: 10px; border-radius: 5px;">
<summary style="cursor: pointer; font-weight: bold; font-size:22px">📁 Paso a paso de ejecución del proyecto en la fase 1</summary>
<br>

*Ejecutar el notebook con **googleColab** prioritariamente para una correcta conexión a Drive institucional...*

*En el notebook hay un cuadro de codigo para su ejecución despues de la lectura de cada paso...*

1. Se realiza la instalación librerías necesarias para la correcta ejecución del los siguientes pasos.

*Ignorar advertencias de conflicto de dependencias, ya que es un conflicto dificil de resolver en la versiones de colab, mas sin embargo los bloques de codigo se ejecutan sin problema en su mayoria y solo hay un paso que puede fallar pero tiene solución indicada.*


2. Se realiza ejecución de codigo para la conexión a Drive donde estarán alojados los archivos de train y test, previamente compartidos al profesor Raul y monitor Jonathan. Para ello deben realizar lo siguiente:

**⚠️ ¡¡IMPORTANTE!!**  
   **Siga los siguientes pasos en orden, de arriba hacia abajo, para que la sincronización con Google Drive sea exitosa:**

   a. ✅ **Aceptar acceso compartido**  
      Acepte la invitación para acceder a la carpeta **Modelos_l** compartida por **Andrés Higuita** desde el correo `adario.higuita@udea.edu.co`.

   b. 📂 **Mover la carpeta a “Mi unidad”**  
      Ingrese a su [Google Drive](https://drive.google.com), ubique la carpeta **Modelos_l** en la sección **"Compartido conmigo"**, y arrástrela hacia **"Mi unidad"**.  
      Esto añadirá un acceso directo necesario para gestionarla desde el Notebook en Colab.

   c. ▶️ **Ejecutar el código de conexión**  
      En el Notebook de Colab, ejecute la celda correspondiente para montar Google Drive.

   d. 🔐 **Autorizar acceso a archivos**  
      Cuando se lo solicite, permita que el Notebook acceda a sus archivos de Google Drive.

   e. 🏫 **Usar cuenta institucional**  
      Inicie sesión con su **cuenta institucional** (la misma a la que se compartió la carpeta **Modelos_l**).

   f. ✅ **Aceptar todos los permisos**  
      Acepte **todas las solicitudes de permisos por defecto**. En total, son **8 servicios** que el Notebook necesita para acceder y sincronizar.

   g. ☁️ **Confirmar y sincronizar**  
      Una vez completados los pasos anteriores, el sistema sincronizará automáticamente los archivos compartidos.

   h. 📁 **Ruta de acceso en el entorno Colab**  
      Los archivos estarán disponibles desde la siguiente ruta dentro del entorno del Notebook:  
      `/content/drive/MyDrive/Modelos_l/`

3. Una vez aceptado el acceso a la carpeta compartida en Google Drive, se procede a extraer los archivos necesarios para el entrenamiento y prueba del modelo desde la carpeta base **Modelos_l**. Para ello, debe ejecutarse el bloque de código correspondiente en el notebook.

   Este paso realizará lo siguiente:

   - 📁 Se crea automáticamente una carpeta llamada **`rsna_project`** dentro del directorio **`/content/`** del entorno de Colab.
   - 📦 Dentro de esta carpeta se extraen o ubican los archivos y carpetas compartidas desde Drive, específicamente:
     - `train.csv` → Archivo con datos de entrenamiento.
     - `test.csv` → Archivo con datos de prueba.
     - `train_images/` → Carpeta que contiene las imágenes utilizadas para entrenar el modelo.
     - `test_images/` → Carpeta que contiene las imágenes que serán utilizadas para realizar predicciones.

   ✅ Asegúrese de que los archivos estén correctamente ubicados en la carpeta **Modelos_l** dentro de su Google Drive antes de ejecutar este paso.


4. Se realiza importación de librerias.

**⚠️ ¡¡IMPORTANTE!!**  
   Si aparece un error al importar `fastai.vision.all`, debe **reiniciar el entorno de ejecución** siguiendo estos pasos:

   a. 🧭 Dirígete a la barra de opciones superior del notebook de Colab.  
   b. 🔄 Haz clic en **"Entorno de ejecución"**.  
   c. 📌 En el menú desplegable, selecciona **"Reiniciar la sesión"**.  
   d. ⏳ Espera unos segundos a que se reinicie el entorno por completo.  
   e. ✅ Una vez reiniciado, puedes continuar ejecutando el resto del código **sin inconvenientes**.

   ---

   💡 *Reiniciar el entorno suele resolver errores relacionados con incompatibilidades temporales de librerías.*


5. Se define ruta de trabajo y cargar train.csv


6. Se acondiciona función para leer .dcm como imagen


7. Se acondiciona función para obtener el path de cada imagen .dcm


8. Se realiza un filtrado de las imágenes que realmente existen dentro del train


9. Se preparan los datos con DataBlock


10. Se realiza entrenamiento del modelo


11. Se hacen predicciones sobre el set de prueba


12. Se genera archivo submission.csv con los resultados de la predicción realizada


</details>

<details style="margin-left: 20px; border: 1px solid #ccc; padding: 10px; border-radius: 5px;">
<summary style="cursor: pointer; font-weight: bold; font-size:22px">📁 Paso a paso de ejecución del proyecto en la fase 2</summary>
<br>

## **CONSIDERACIONES INICIALES**

* *En esta fase 2 es necesario contemplar que la ejecución de la misma se realizará en un SO Linux (preferiblemente Ubuntu) con Docker instalado de acuerdo a la documentación oficial en https://docs.docker.com/engine/install/*

* *Por favor leer detalladamente y seguir las instrucciones de arriba hacia abajo*

### **PASOS PARA LA CORRECTA EJECUCIÓN**

Al clonar o descargar este repositorio obtenemos la carpeta fase-2 con los archivos:

*Cada archivo tiene los comentarios con explicaciones necesarias dado el caso*

├── Dockerfile

├── export.pkl

├── helpers.py

├── predict.py

├── requirements.txt

├── submission.csv

├── test.csv

├── train.csv

├── train.py

**Posteriormente ubicados en la carpeta fase-2, realizamos lo siguiente:**

Construimos la imagen de Docker con el comando:
```bash
sudo docker build -t cancer_prediction_model .
```
***PD: Por favor tener un poco de paciencia en la espera de la construcción de la imagen ya que para la ejecución de este proyecto es explicitamente necesario usar librerias de torch y fastai las cuales son extensas***

Esta imagen creada contiene los mismos archivos del repositorio y ademas las carpetas **test_images** (*contiene imagenes para procesar una predicción*) y **train_images** (*contiene una cantidad limitada de 94 imagenes para el entrenamiento*), esto con la finalidad mensionada por parte del profesor que este fuese autocontenido, estas carpetas contienen las imagenes para testear/predecir y las imagenes para entrenar el modelo.

Con esta imagen podemos hacer ejecuciones:

#### **DESDE LA PARTE EXTERNA DEL CONTENEDOR**

##### **PREDECIR CANCER DE MAMA**
Podemos precedir indicandole la ubicación del archivo **test.csv** (*que contiene los indices y datos de las imagenes a predecir cancer de mama*), la ubicación del **export.pkl** (*el modelo entrenado*), la ubicación del archivo **submission.csv** (*el archivo que contiene las predicciones resultantes*) y por ultimo se indica que se ejecute el archivo **predict.py** con el siguiente script:

```bash
sudo docker run --rm -v $(pwd)/submission.csv:/app/submission.csv -v $(pwd)/test.csv:/app/test.csv -v $(pwd)/export.pkl:/app/export.pkl cancer_prediction_model python predict.py
```
Obteniendo **submission.csv** como el siguiente:
```bash
image_id,cancer
736471439,0.22821328043937683
```

*PD: Las imagenes indicadas en el archivo **test.csv** se encuentran dentro del contenedor con la finalidad de autogestión.*

##### **ENTRENAR EL MODELO DE PREDICCIÓN**
Podemos entrenar el modelo indicandole la ubicación del archivo **train.csv** (*que contiene los indices y datos de las imagenes para entrenar el modelo*), la ubicación del **export.pkl** (*el modelo entrenado y que será sobreescrito con el nuevo entrenamiento realizado*) y por ultimo se indica que se ejecute el archivo **train.py** con el siguiente script:

```bash
sudo docker run --rm -v $(pwd)/export.pkl:/export.pkl -v $(pwd)/train.csv:/train.csv cancer_prediction_model python train.py
```
Una vez finalizada la ejecución se obtiene el archivo **export.pkl** con el cual podemos hacer nuevas predicción y validar su rendimiento.

*PD: Las imagenes indicadas en el archivo **train.csv** se encuentran dentro del contenedor con la finalidad de autogestión.*


#### **DESDE LA PARTE INTERNA DEL CONTENEDOR**

Debemos de ingresar al contenedor con el siguiente comando:

```bash
sudo docker run -it cancer_prediction_model bash
```

##### **PREDECIR CANCER DE MAMA**
Podemos precedir ajustando las variables del archivo **test.csv** (*que contiene los indices y datos de las imagenes a predecir cancer de mama*) si se requiere y solo sería ejecutar el archivo **predict.py** con el siguiente script:

```bash
python predict.py
```
Obteniendo **submission.csv** como el siguiente:
```bash
image_id,cancer
736471439,0.22821328043937683
```

*PD: Las imagenes indicadas en el archivo **test.csv** se encuentran dentro del contenedor con la finalidad de autogestión.*

##### **ENTRENAR EL MODELO DE PREDICCIÓN**
Podemos entrenar el modelo ajustando las variables del archivo del archivo **train.csv** (*que contiene los indices y datos de las imagenes para entrenar el modelo*) si se requiere y se ejecuta el  archivo **train.py** con el siguiente script:

```bash
python train.py
```
Una vez finalizada la ejecución se obtiene el archivo **export.pkl** con el cual podemos hacer nuevas predicción y validar su rendimiento.

*PD: Las imagenes indicadas en el archivo **train.csv** se encuentran dentro del contenedor con la finalidad de autogestión.*

</details>

<details style="margin-left: 20px; border: 1px solid #ccc; padding: 10px; border-radius: 5px;">
<summary style="cursor: pointer; font-weight: bold; font-size:22px">📁 Paso a paso de ejecución del proyecto en la fase 3</summary>
<br>

*Proximamente...*

</details>
