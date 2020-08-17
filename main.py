# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:46:03 2020

@author: Admin
"""
from ventana import *
import serial
import pyttsx3 
engine=pyttsx3.init()
engine.setProperty("rate", 180)
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
       
        
        self.led1.clicked.connect(self.prender_led1)
        self.led2.clicked.connect(self.prender_led2)
        self.led3.clicked.connect(self.prender_led3)
        self.led4.clicked.connect(self.prender_led4)
        self.pushButton.clicked.connect(self.salir)
        
    def prender_led1(self):  
        ser=serial.Serial('COM3',9600)
        ser.write(b'1\r\n')
        estado=ser.readline()
        if estado==b'on\r\n':
            self.label.setText(str("Prendido"))
            engine.say("Led 1 prendido")
            engine.runAndWait()
            
        if estado==b'off\r\n':
            self.label.setText(str("Apagado"))
            engine.say("Led 1 apagado")
            engine.runAndWait()
        
    def prender_led2(self):
        ser=serial.Serial('COM3',9600)
        ser.write(b'2\r\n')
        estado=ser.readline()
        if estado==b'on\r\n':
            self.label_2.setText(str("Prendido"))
            engine.say("Led 2 prendido")
            engine.runAndWait()
            
        if estado==b'off\r\n':
            self.label_2.setText(str("Apagado"))
            engine.say("Led 2 apagado")
            engine.runAndWait()
        
        
    def prender_led3(self):
        ser=serial.Serial('COM3',9600)
        ser.write(b'3\r\n')
        estado=ser.readline()
        if estado==b'on\r\n':
            self.label_3.setText(str("Prendido"))
            engine.say("Led 3 prendido")
            engine.runAndWait()
            
        if estado==b'off\r\n':
            self.label_3.setText(str("Apagado"))
            engine.say("Led 3 apagado")
            engine.runAndWait()
        
    def prender_led4(self):
        ser=serial.Serial('COM3',9600)
        ser.write(b'4\r\n')
        estado=ser.readline()
        if estado==b'on\r\n':
            self.label_4.setText(str("Prendido"))
            engine.say("Led 4 prendido")
            engine.runAndWait()
            
        if estado==b'off\r\n':
            self.label_4.setText(str("Apagado"))
            engine.say("Led 4 apagado")
            engine.runAndWait()
            
    
    def salir(self):
        engine.say("pestaña cerrada")
        engine.runAndWait()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()