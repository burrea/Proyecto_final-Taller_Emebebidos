import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
import time
import cv2
import random
import numpy as np

class MainWindow(QMainWindow):#Clase donde se definen los objetos que definen las herramientas que componen la intefaz
    #Constructor de la clase
    def __init__(self): 
        QMainWindow.__init__(self)
        
        #Define las dimesiones de la ventana
        self.setMinimumSize(QSize(530, 500))    
        self.setWindowTitle("Poker de dados") 
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.namejugador1 = QLabel(self)
        self.namejugador1.setText('Nombre jugador 1')
        self.N_jugador1 = QLineEdit(self)
        self.N_jugador1.returnPressed.connect(self.onPressedJ1)
        #posiciona los objetos editor de línea y etiqueta
        self.N_jugador1.move(20, 50)
        self.N_jugador1.resize(100, 22)
        self.namejugador1.move(30, 20)
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.namejugador2 = QLabel(self)
        self.namejugador2.setText('Nombre jugador 2')
        self.N_jugador2 = QLineEdit(self)
        self.N_jugador2.returnPressed.connect(self.onPressedJ2)
        #posiciona los objetos editor de línea y etiqueta
        self.N_jugador2.move(150, 50)
        self.N_jugador2.resize(100, 22)
        self.namejugador2.move(160, 20)
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.namejugador3 = QLabel(self)
        self.namejugador3.setText('Nombre jugador 3')
        self.N_jugador3 = QLineEdit(self)
        self.N_jugador3.returnPressed.connect(self.onPressedJ3)
        
        self.N_jugador3.move(280, 50)
        self.N_jugador3.resize(100, 22)
        self.namejugador3.move(290, 20)
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.namejugador4 = QLabel(self)
        self.namejugador4.setText('Nombre jugador 4')
        self.N_jugador4 = QLineEdit(self)
        self.N_jugador4.returnPressed.connect(self.onPressedJ4)

        self.N_jugador4.move(410, 50)
        self.N_jugador4.resize(100, 22)
        self.namejugador4.move(420, 20)
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.rondas = QLabel(self)
        self.rondas.setText('Numero de rondas')
        self.N_rondas = QLineEdit(self)

        self.N_rondas.move(210, 120)
        self.N_rondas.resize(100, 22)
        self.rondas.move(220, 90)
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.J1 = QLabel(self)
        self.puntaje1 = QLineEdit(self)

        self.puntaje1.move(20, 190)
        self.puntaje1.resize(100, 22)
        self.J1.move(30, 160)
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.J2 = QLabel(self)
        self.puntaje2 = QLineEdit(self)

        self.puntaje2.move(150, 190)
        self.puntaje2.resize(100, 22)
        self.J2.move(160, 160)
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.J3 = QLabel(self)
        self.puntaje3 = QLineEdit(self)

        self.puntaje3.move(280, 190)
        self.puntaje3.resize(100, 22)
        self.J3.move(290, 160)
        #Agrega una etiqueta y un editor de línea a la interfaz
        self.J4 = QLabel(self)
        self.puntaje4 = QLineEdit(self)

        self.puntaje4.move(410, 190)
        self.puntaje4.resize(100, 22)
        self.J4.move(420, 160)
        #Agrega un boton a la interfaz y lo posiciona
        Btn_Inicio = QPushButton('Inicio', self)
        Btn_Inicio.clicked.connect(self.bienvenida)
        Btn_Inicio.resize(130,32)
        Btn_Inicio.move(200, 360)
        #Agrega un boton a la interfaz y lo posiciona
        Btn_turno = QPushButton('Captura', self)
        Btn_turno.clicked.connect(self.Juego)
        Btn_turno.resize(130,32)
        Btn_turno.move(370, 300)
        #Agrega un boton a la interfaz y lo posiciona
        Btn_Inicio = QPushButton('Salir del juego', self)
        Btn_Inicio.clicked.connect(self.salir)
        Btn_Inicio.resize(130,32)
        Btn_Inicio.move(200, 400)
        #Agrega etiqueta a la interfaz y la posiciona
        self.Inicio=QLabel(self)
        self.Inicio.resize(130,32)
        self.Inicio.move(200,260)
        #Agrega etiqueta a la interfaz y la posiciona
        self.turno=QLabel(self)
        self.turno.resize(130,32)
        self.turno.move(40,260)
        #Agrega etiqueta a la interfaz y la posiciona
        self.ganador=QLabel(self)
        self.ganador.resize(130,32)
        self.ganador.move(40,300)
        #Agrega etiqueta a la interfaz y la posiciona
        self.lbl4 = QLabel(self)
        self.lbl4.setPixmap(QPixmap("logo.png"))
        self.lbl4.resize(130,90)
        self.lbl4.move(370,350)

    def onPressedJ1(self):#Método para sobreescribir nombre de jugador
        self.J1.setText(self.N_jugador1.text())

    def onPressedJ2(self):#Método para sobreescribir nombre de jugador
        self.J2.setText(self.N_jugador2.text())

    def onPressedJ3(self):#Método para sobreescribir nombre de jugador
        self.J3.setText(self.N_jugador3.text())

    def onPressedJ4(self):#Método para sobreescribir nombre de jugador
        self.J4.setText(self.N_jugador4.text())

    def bienvenida(self):#Boton para dar la bienvenida al juego
        a="BIENVENIDO AL JUEGO!"
        self.Inicio.setText(a)

    def salir(self):#Boton que permite salir del juego
        self.close()

    def Juego(self):#Método que define la lógica del juego
        ronda=int(self.N_rondas.text())
        jugadores=4
        cont=1

        #self.puntaje1.setText(str(puntaje))
        #self.puntaje1.text(str(puntaje))
        #puntos=self.puntaje1.setText(str(puntaje))

        puntos= [0,0,0,0]
        puntaje_total = [0, 0, 0, 0]
        while(ronda != 0):
            turno=1
            while(turno<=jugadores):
                self.turno.setText(print("Turno de Jugador" + str(turno)) )
                time.sleep(3)
                print("Jugador"+ str(turno))
                cap = cv2.VideoCapture(0)
                leido, frame = cap.read()
                if leido == True:
                    nombre_foto = "Imagen_nueva.png"
                    cap.release()
                else:
                    cap.release()
                cv2.imwrite(nombre_foto,frame)
                
                puntos[turno-1]=puntos[turno-1]+1
                print (cv2.__version__)

                DICE_SIZE = 16
                BLUR_FACTOR = 5
                RED_LOW_THRESHOLD = 209
                MIN_PIP_AREA = 10

                img = cv2.imread(nombre_foto)

        ### imagen umbral

                blurred = cv2.medianBlur(img,BLUR_FACTOR)

                blue = cv2.split(blurred)[0]
                green = cv2.split(blurred)[1]
                red = cv2.split(blurred)[2]

        # Busca los contornos del dado usando el umbral rojo y lo invierte
                diceblocks = cv2.threshold(red, RED_LOW_THRESHOLD, 255, 1) # 185 --> 235
                invdiceblocks = 255 - diceblocks[1]
                #cv2.imshow("diceblocks",invdiceblocks)

        #Hace una tranformada de distancia y lo normaliza para que se pueda visualizar y umbralizar 
                pyramids = cv2.distanceTransform(invdiceblocks, 2, 3)
                cv2.normalize(pyramids, pyramids, 0, 1.2, cv2.NORM_MINMAX)

        #Obtener las marcas para el algoritmo watershed usando el umbral
                markers = cv2.threshold(pyramids, 0.8, 1, 0)[1] 
                #cv2.imshow("markers",markers)

        # Convierte la matriz de numpy de flotantes a enteros [0..1] to int [0..255]
                bwImg = cv2.convertScaleAbs(markers * 255)

        # captura los contornos
                pyramids, hierarchy = cv2.findContours(bwImg.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                print (str(len(pyramids)) + " dice.")
       
        #Ajusta el rectangulo rotado en la piramide transformada por distancia
                for pyramid in pyramids:
                    rect = cv2.minAreaRect(pyramid)

                    rect = rect[0], (rect[1][0] + DICE_SIZE,rect[1][1] + DICE_SIZE), rect[2]


                    floatBox = cv2.boxPoints(rect)
                    intBox = np.int0(floatBox)
                    bwImg = cv2.drawContours(bwImg,[intBox],0,(255,0,0),-1)

                    pts1 = floatBox
                    a,b,c,d = cv2.boundingRect(intBox)
                    pts2 = np.float32([[a,b],[a+c,b],[a,b+d],[a+c,b+d]])

                    M = cv2.getPerspectiveTransform(pts1,pts2)
                    dst = cv2.warpPerspective(bwImg,M,pts2.shape)
                    contours, hierarchy = cv2.findContours(bwImg.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	# captura los contornos grandes
                contours, hierarchy = cv2.findContours(bwImg.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	
        #Filtra los puntos y después los corta usando el área de contorno
                pips = 255 - cv2.threshold(cv2.cvtColor(blurred, cv2.COLOR_RGB2GRAY), 200, 255, 1)[1]
                onlypips = cv2.bitwise_and(bwImg,pips)
                #cv2.imshow("onlypips", onlypips)
                dice = cv2.cvtColor(onlypips, cv2.COLOR_GRAY2RGB)

                dice_results = [0,0,0,0,0,0]
                wrongdice = 0

        #Mira la cara del dado y determina el número de puntos
                for contour in contours:
                    pips = 0

                    rect = cv2.minAreaRect(contour)
                    floatBox = cv2.boxPoints(rect)
                    intBox = np.int0(floatBox)
                    a,b,c,d = cv2.boundingRect(intBox)


                    subimage = onlypips[b:b+d,a:a+c]

                    pip_contours, subhierarchy = cv2.findContours(subimage.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    for pip in pip_contours:
                        if cv2.contourArea(pip) >= MIN_PIP_AREA:
                            pips = pips + 1

                    if pips > 6 or pips == 0:
                        wrongdice = wrongdice + 1
                        print (pips)
                    else:
                        dice_results[pips - 1] = dice_results[pips - 1] + 1
                        cv2.putText(dice,str(pips),(a,b-5),0,1,(0,0,255))
	
               #Imprime los resultados
                print (dice_results)

                cv2.drawContours(dice,contours,-1,(255,255,0),1)
                #cv2.imshow('Dice', dice)
                #cv2.imshow('Original',img)


                puntaje_turno = 0
                cara = 1
                for resultado in dice_results:
                    if resultado == 1:
                        puntaje_turno = puntaje_turno + cara
                    if resultado == 2:
                        puntaje_turno = cara*2
                    cara += 1
                print ("puntaje jugador"+ ""+ str(puntaje_turno))

                self.turno.setHidden(True)

                puntaje_total[turno-1] = puntaje_total[turno-1]+ puntaje_turno
                if puntaje_total[turno-1] > 21:
                    puntaje_total[turno-1] = "xxxxxxxxxxxxx"

                self.puntaje1.setText(str(puntaje_total[0]))
                self.puntaje2.setText(str(puntaje_total[1]))
                self.puntaje3.setText(str(puntaje_total[2]))
                self.puntaje4.setText(str(puntaje_total[3]))

                print(puntaje_total)

                turno=turno+1

            ronda=ronda-1
        ganador=0
        valor=0
        for i in puntaje_total:
            if(type(i) == int):
                if(i>valor):
                    valor=i
                    ganador=puntaje_total.index(i)

        #print("el mayor es"+ str(ganador))
        self.ganador.setText("El ganador es jugador" +" "+ str(ganador+1))            
                    
                    
            
        print(puntos)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
