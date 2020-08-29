# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:40:35 2020

@author: Admin
"""


import serial
import time

def comunicacion_config(puerto_in,baudios_in):
    """Configuramos los baudios y puerto a utilizar con esta funcion, al utilizar este script es nesersario
    llamarlo para no generar errores"""
    baudios = baudios_in
    puerto = puerto_in
    global ser 
    ser =serial.Serial(puerto,baudios)
    time.sleep(1.9)
    # ser = serial.Serial('/dev/ttyUSB0')

def prender_led1():  
    """activa la salida led 1, envia '1'  y recibe un valor en string del dispositivo, 
    retorna la variable estado como parametro recibido del arduino"""
    ser.write(b'1\r\n')
    estado=ser.readline()
    return estado
       
def prender_led2():
    ser.write(b'2\r\n')
    estado=ser.readline()
    return estado
    
def prender_led3():
    ser.write(b'3\r\n')  
    estado=ser.readline()
    return estado
def prender_led4():
    ser.write(b'4\r\n')
    estado=ser.readline()
    return estado

def inicializar_salida():
    lista=[]
    ser.write(b'e\r\n')         
    for i in range(4):
        estado=ser.readline()
        lista.append(estado)
    salida=lista
    return salida

def estado():
    salida = inicializar_salida()
    return salida

def cerrar_serial():
    ser.close()
    
       