# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:40:35 2020

@author: Admin
"""



import pyttsx3  
import serial
engine=pyttsx3.init()
engine.setProperty("rate", 180)
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)

def prender_led1():  
        ser=serial.Serial('COM3',9600)
        ser.write(b'1\r\n')
        
def prender_led2():
        ser=serial.Serial('COM3',9600)
        ser.write(b'2\r\n')
    
def prender_led3():
    
        ser=serial.Serial('COM3',9600)
        ser.write(b'3\r\n')    
def prender_led4():
        ser=serial.Serial('COM3',9600)
        ser.write(b'4\r\n')
       