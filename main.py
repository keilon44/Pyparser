import speech_recognition as sr
import re
import soundfile
import numpy
import connection
import parserpy as pppy
import re
import speech_recognition as sr
import connection
import sys

## Linea que se utiliza en caso de que venga con argumentos que para el funcionamiento normal de la aplicación.
##pathfile = sys.argv[1]
def main(pathfile):
    print ('TestMain')
main(pathfile)




##Funciona 
print ('Hola mundo')
#pppy.audiototext()
r = sr.Recognizer()
data, samplerate = soundfile.read('cedillo.wav')
soundfile.write('cedillo2.wav', data, samplerate, subtype='PCM_16')
with sr.AudioFile('cedillo2.wav') as source:
    audio = r.record(source)
# Reconocimiento de texto
text = r.recognize_google(audio, language = "es-ES")
print(text)

