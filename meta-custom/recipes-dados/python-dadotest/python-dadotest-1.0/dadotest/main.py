import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
import time
import cv2
import random
import sys
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(530, 500))    
        self.setWindowTitle("Poker de dados") 

        self.namejugador1 = QLabel(self)
        self.namejugador1.setText('Nombre jugador 1')
        self.N_jugador1 = QLineEdit(self)
        self.N_jugador1.returnPressed.connect(self.onPressedJ1)

        self.N_jugador1.move(20, 50)
        self.N_jugador1.resize(100, 22)
        self.namejugador1.move(30, 20)

        self.namejugador2 = QLabel(self)
        self.namejugador2.setText('Nombre jugador 2')
        self.N_jugador2 = QLineEdit(self)
        self.N_jugador2.returnPressed.connect(self.onPressedJ2)

        self.N_jugador2.move(150, 50)
        self.N_jugador2.resize(100, 22)
        self.namejugador2.move(160, 20)

        self.namejugador3 = QLabel(self)
        self.namejugador3.setText('Nombre jugador 3')
        self.N_jugador3 = QLineEdit(self)
        self.N_jugador3.returnPressed.connect(self.onPressedJ3)

        self.N_jugador3.move(280, 50)
        self.N_jugador3.resize(100, 22)
        self.namejugador3.move(290, 20)

        self.namejugador4 = QLabel(self)
        self.namejugador4.setText('Nombre jugador 4')
        self.N_jugador4 = QLineEdit(self)
        self.N_jugador4.returnPressed.connect(self.onPressedJ4)

        self.N_jugador4.move(410, 50)
        self.N_jugador4.resize(100, 22)
        self.namejugador4.move(420, 20)

        self.rondas = QLabel(self)
        self.rondas.setText('Numero de rondas')
        self.N_rondas = QLineEdit(self)

        self.N_rondas.move(210, 120)
        self.N_rondas.resize(100, 22)
        self.rondas.move(220, 90)

        self.J1 = QLabel(self)
        self.puntaje1 = QLineEdit(self)

        self.puntaje1.move(20, 190)
        self.puntaje1.resize(100, 22)
        self.J1.move(30, 160)

        self.J2 = QLabel(self)
        self.puntaje2 = QLineEdit(self)

        self.puntaje2.move(150, 190)
        self.puntaje2.resize(100, 22)
        self.J2.move(160, 160)

        self.J3 = QLabel(self)
        self.puntaje3 = QLineEdit(self)

        self.puntaje3.move(280, 190)
        self.puntaje3.resize(100, 22)
        self.J3.move(290, 160)

        self.J4 = QLabel(self)
        self.puntaje4 = QLineEdit(self)

        self.puntaje4.move(410, 190)
        self.puntaje4.resize(100, 22)
        self.J4.move(420, 160)

        Btn_Inicio = QPushButton('Inicio', self)
        Btn_Inicio.clicked.connect(self.Juego)
        Btn_Inicio.resize(130,32)
        Btn_Inicio.move(200, 360)

        self.Inicio=QLabel(self)
        self.Inicio.resize(130,32)
        self.Inicio.move(200,260)

    def onPressedJ1(self):
        self.J1.setText(self.N_jugador1.text())

    def onPressedJ2(self):
        self.J2.setText(self.N_jugador2.text())

    def onPressedJ3(self):
        self.J3.setText(self.N_jugador3.text())

    def onPressedJ4(self):
        self.J4.setText(self.N_jugador4.text())

    def Juego(self):  
        a="BIENVENIDO AL JUEGO!"
        self.Inicio.setText(a)
        cont=1
        #time.sleep(2)
        #b=""
        #self.Inicio.setText(b)

        cap = cv2.VideoCapture(0)
        leido, frame = cap.read()

        if leido == True:
                #print("hola")
	        nombre_foto = "Imagen"+ str(cont)+".png" 
	        cv2.imwrite(nombre_foto, frame)
	        cap.release()
        else:
	        cap.release()

        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )


