# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:33:10 2020

@author: Admin
"""
import pyttsx3 
import speech_recognition as sr

r = sr.Recognizer()

#configuramos la voz 
engine=pyttsx3.init()
engine.setProperty("rate", 180)
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
#fin de configuracion 

def detector_de_voz():
        with sr.Microphone(device_index=1) as source:
            print('Hable: ')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio,language='es-ES')
                print('You said: {}'.format(text))
            except:
                print("Lo siento, no pude escuchar, o sin conección a Internet ")
                engine.say("Lo siento, no pude escuchar, o sin conección a Internet ")
                engine.runAndWait()
            return text