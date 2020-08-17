# Proyecto final Taller de Embebidos
### 1 semestre 2020
Reglas del Juego poker de dados:
1. Juegan 4 jugadores
2. Se elige la cantidad de rondas
3. Por cantidad de rondas cada jugador tienen un turno para lanzar dados
4. La cámara web toma captura de la posición de los dados y automaticamente se cuenta los puntos
5. si un jugador supera los veintiun puntos, no se le cuenta más los puntos y queda fuera del juego
6. De los jugadores no eliminados, gana el que tenga más puntos cuando se acaban las rondas
### Prof.Johan


Juego 21 con dados usando visión por computadora

El presente repositorio se compone de los archivos elementales para la aplicación embebida que simula un crupier en un juego de Blackjack de dados. Para esto, se utilizo el sistema empotrado Raspberry Pi modelo 3. Asimismo, se implemento el algoritmo Watershed por medio de la librería OpenCV para el correcto procesamiento de las imágenes. Se utilizo la misma librería para identificar el valor de la cara superior de los dados. Para esto, también se creo la aplicación del juego, mediante el lenguaje de programación Python con su respectiva interfaz gráfica. Para el desarrollo del sistema operativo que soportará esta aplicación, se utilizará la herramienta Yocto Project. 

Para la implementacion del juego fueron necesarios los paquetes que se enuncian a continuacion, de forma que se logre la interaccion de la interfaz con Qt5 con la logica del juego escrito en Python y usa PyQt5 y OpenCV.

  - python3-pyqt5
  - qtbase qtdeclarative qtmultimedia qtscript
  - sip3
  - opencv
  - v4l
  - gstreamer1.0
  - x11
  - ssh

**Contenido del repositorio**

| Descripcion | Ruta |
| ------ | ------ |
| Capa personalizada | [meta-custom][PMC] |
| Archivos de configuracion de la imagen | [bblayers.conf][PBB] y [local.conf][PLC] |
| Juego en Python | [juego][PJP] |

> La implementacion de la interfaz grafica con Qt5 fue producto de muchas iteraciones ya que comunmente se usa c++ para aplicaciones con Qt5. Se hace "cross compilacion" y el archivo ejecutable se despliega en la tarjeta mediante un "toolchain".
> Ya que la propuesta definio el uso de Python, y las pocas implementaciones encontradas en la literatura de Qt5 con Python, hicieron que el proceso requiriera contrucciones largas (en tiempo) y varias iteraciones.

Se uso una image base mediante el comando:
```sh
$ bitbake core-image-base
```

   [PMC]: <https://github.com/burrea/Proyecto_final-Taller_Emebebidos/tree/master/meta-custom/recipes-dados/python-dadotest/python-dadotest-1.0>
   [PBB]: <https://github.com/burrea/Proyecto_final-Taller_Emebebidos/blob/master/bblayers.conf>
   [PLC]: <https://github.com/burrea/Proyecto_final-Taller_Emebebidos/blob/master/local.conf>
