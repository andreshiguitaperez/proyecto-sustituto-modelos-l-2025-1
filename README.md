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

**¡¡IMPORTANTE!!**
*   Deben aceptar el acceso a la carpeta **Modelos_l** compartida por Andres Higuita desde el correo adario.higuita@udea.edu.co.
*   Deben ejecutar el codigo siguiente para iniciar la conexión al drive de ustedes.
*   Deben permitir que el notebook pueda acceder a sus archivos de Google Drive.
*   Deben iniciar sesión con la cuenta institucional a las que ses compartió la carpeta **Modelos_l**.
*   Deben aceptar todas las sugerencias de permisos por defecto, en total son 8 servicios a los que accede el notebook.
*   Confirmar y finalmente se sincronizaran todos los archivos del drive.
*   La información sincronizada quedara en la ruta base "content/drive" de los archivos del notebook.


3. Al aceptar el acceso a la carpeta compartida de drive, con el siguiente codigo se extraen los archivos de test y train alojados en Drive, ya que la carpeta base seria **Modelos_l**.

*   Se crea la carpeta **"rsna_project"** dentro de **"content"**.
*   En ella se extraen-ubican archivos y carpetas: test.csv, train.csv,  test_images (imagenes de testeo) y train_images (imagenes de entrenamiento del modelo).


4. Se realiza importación de librerias.

**¡¡IMPORTANTE!!**

Si sale error en en la importación de **fastai.vision.all** se debe reiniciar el entorno de ejecución, de la siguiente manera:

* En la barra de opciones se da clic a la opción **Entorno de ejecución**
* Al desplegarse la lista de opciones se da clic en la opción **Reiniciar la sesión**
* Una vez reiniciado el entorno, se puede continuar con la ejecución de los pasos sin inconvenientes.


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

*Proximamente...*

</details>

<details style="margin-left: 20px; border: 1px solid #ccc; padding: 10px; border-radius: 5px;">
<summary style="cursor: pointer; font-weight: bold; font-size:22px">📁 Paso a paso de ejecución del proyecto en la fase 3</summary>
<br>

*Proximamente...*

</details>
