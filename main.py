# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:46:03 2020

@author: Admin
"""
from ventana2 import *  #importamos la ventana de diseño de PYQT
# import serial      # llamamos la comunicacion serial
import pyttsx3    # libreria para que cmunique texto con voz
import speech_recognition as sr      # para el reconocimiento de voz
import detector_de_voz  as dv        # pequeño script para reconocimiento de voz
import activar_salidas_arduino as activar    # pequeño scritp para activar salidas de arduino


r = sr.Recognizer() 
engine=pyttsx3.init()
engine.setProperty("rate", 180)
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def actualizar(self,lista):
        print(lista)
        if lista[0]==b'on1\r\n':
            self.estado_led_1.setText(str("Prendido"))
        else:
            self.estado_led_1.setText(str("Apagado"))
        
        if lista[1]==b'on2\r\n':
            self.estado_led_2.setText(str("Prendido"))
        else:
            self.estado_led_2.setText(str("Apagado"))
            
        if lista[2]==b'on3\r\n':
            self.estado_led_3.setText(str("Prendido"))
        else:
            self.estado_led_3.setText(str("Apagado"))
            
        if lista[3]==b'on4\r\n':
            self.estado_led_4.setText(str("Prendido"))
        else:
            self.estado_led_4.setText(str("Apagado"))
            
class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.LED01.clicked.connect(self.prender_led1)
        self.LED02.clicked.connect(self.prender_led2)
        self.LED03.clicked.connect(self.prender_led3)
        self.LED04.clicked.connect(self.prender_led4)
        self.escuchar.clicked.connect(self.escuchar_1)
        self.salir_ventana.clicked.connect(self.salir)
        self.conectar_serial.clicked.connect(self.serial_activado)
        self.desconectar_serial.clicked.connect(self.serial_desactivado)
        

    def serial_activado(self):
        self.estado_serial.setText(str("CONECTADO"))
        engine.say("puerto serial conectado")
        engine.runAndWait()
        com = self.puertos.currentText()#obtenemos el valor del puerto seri de QT
 
        print(com)
        com=str(com) #Lo  convertimos a string 
        baudios= 9600
        activar.comunicacion_config(com,baudios)
        lista = activar.inicializar_salida()
        actualizar(self,lista)
        
        
    def serial_desactivado(self):
        self.estado_serial.setText(str("DESCONECTADO"))
        engine.say("puerto serial desconectado")
        engine.runAndWait()
        activar.cerrar_serial()

        

    def escuchar_1(self):
        
        texto = dv.detector_de_voz()
        print (texto)
        self.estado_voz.setText(texto)
        estados = activar.estado()
        
        if texto=="prender led 1" and estados[0]==b'off1\r\n':
            self.estado_led_1.setText(str("Prendido"))
            engine.say("prender led 1")
            engine.runAndWait()
            activar.prender_led1()
            
        if texto=="prender led 2" and estados[1]==b'off2\r\n':
            self.estado_led_2.setText(str("Prendido"))
            engine.say("prender led 2")
            engine.runAndWait()
            activar.prender_led2()
            
        if texto=="prender led 3" and estados[2]==b'off3\r\n':
            self.estado_led_3.setText(str("Prendido"))
            engine.say("prender led 3")
            engine.runAndWait()
            activar.prender_led3()
            
        if texto=="prender led 4" and estados[3]==b'off4\r\n':
            self.estado_led_4.setText(str("Prendido"))
            engine.say("prender led 4")
            engine.runAndWait()
            activar.prender_led4()
            
        if texto=="Apagar led 1" and estados[0]==b'on1\r\n':
            self.estado_led_1.setText(str("Apagado"))
            engine.say("Apagando led 1")
            engine.runAndWait()
            activar.prender_led1()
            
        if texto=="Apagar led 2" and estados[1]==b'on2\r\n':
            self.estado_led_2.setText(str("Apagado"))
            engine.say("Apagando led 2")
            engine.runAndWait()
            activar.prender_led2()
            
        if texto=="Apagar led 3" and estados[2]==b'on3\r\n':
            self.estado_led_3.setText(str("Apagado"))
            engine.say("Apagando led 3")
            engine.runAndWait()
            activar.prender_led3()
            
        if texto=="Apagar led 4" and estados[3]==b'on4\r\n':
            self.estado_led_4.setText(str("Apagado"))
            engine.say("Apagando led 4")
            engine.runAndWait()
            activar.prender_led4()
      
        
    def prender_led1(self):  
        estado=activar.prender_led1()
        if estado==b'on\r\n':
            self.estado_led_1.setText(str("Prendido"))
            engine.say("Led 1 prendido")
            engine.runAndWait()
            
        if estado==b'off\r\n':
            self.estado_led_1.setText(str("Apagado"))
            engine.say("Led 1 apagado")
            engine.runAndWait()
        
    def prender_led2(self):
        estado= activar.prender_led2()
        
        if estado==b'on\r\n':
            self.estado_led_2.setText(str("Prendido"))
            engine.say("Led 2 prendido")
            engine.runAndWait()    
        if estado==b'off\r\n':
            self.estado_led_2.setText(str("Apagado"))
            engine.say("Led 2 apagado")
            engine.runAndWait()
        
        
    def prender_led3(self):
        estado= activar.prender_led3()
        if estado==b'on\r\n':
            self.estado_led_3.setText(str("Prendido"))
            engine.say("Led 3 prendido")
            engine.runAndWait()    
        if estado==b'off\r\n':
            self.estado_led_3.setText(str("Apagado"))
            engine.say("Led 3 apagado")
            engine.runAndWait()
        
    def prender_led4(self):
        estado= activar.prender_led4()
        if estado==b'on\r\n':
            self.estado_led_4.setText(str("Prendido"))
            engine.say("Led 4 prendido")
            engine.runAndWait()   
        if estado==b'off\r\n':
            self.estado_led_4.setText(str("Apagado"))
            engine.say("Led 4 apagado")
            engine.runAndWait()
            
    
    def salir(self):
        engine.say("ventana cerrada")
        engine.runAndWait()
        activar.cerrar_serial()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()