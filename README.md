# PrograPPC
Proyecto final programacion paralela y concurrente

Para ejecutar este programa en localhost, descarga la carpeta en tu equipo.
- Crear un ambiente virtual: **$ virtualenv nombre_del entorno**
- Instalar en el entorno virtual sklearn y pickles para la carga del modelo: **$ pip install scikit-learn** , **$ pip install pickles**
- Cuando verifiques que las librerias esten instaladas con: **$ pip show nombre_de_libreria**
- Inicia el servidor web django con: **$ python manage runserver.py** (si tienes mas versiones de python deberas especificar en el comando si utilizaras python 3).


La pagina se cargara en el servidor local, la terminal te dara la ruta, persiona CTRL+Enter para abrirlo en el navegador y en la ruta agrega la direccion **/parametros/form**. Aqui te desplegara el formulario donde seleccionaras los datos del vendedor y el tipo de ejecucion que buscas: Secuencial o Paralela.
