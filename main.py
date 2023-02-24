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
###COMPROBAR EL FORMATO DEL NOMBRE DEL FICHERO POR SI SE PUEDE OBTENER INFORMACIÓN DEL NÚMERO QUE LLAMA 
## Linea que se utiliza en caso de que venga con argumentos que para el funcionamiento normal de la aplicación.
pathfile = sys.argv[1]
def main(pathfile):
    print ('TestMain')
    #Es llamado desde el script de batch con el nombre de la ruta del fichero.
    #El main se encarga de llamar a la función audiototext
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
text.
print(text)

