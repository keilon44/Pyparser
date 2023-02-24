import re
import pyaudio
import numpy
import soundfile
import speech_recognition as sr
import connection
def audiototext(filepath):
    #Cambio de formato del fichero Wav para que pueda ser leído por el recognizer
    data, samplerate = soundfile.read('cedillo.wav')
    soundfile.write('cedillo2.wav', data, samplerate, subtype='PCM_16')

    #Creamos la instancia del recognizer
    r = sr.Recognizer()

    with sr.AudioFile(filepath) as source:
        audio = r.record(source)
    # Reconocimiento de texto
    text = r.recognize_google(audio, language = "es-ES")

    #Una vez llamado el texto hay que filtrarlo para ver si se pueden obtener el da
    extract_info_from_wav(text)

def extract_info_from_wav(text):

    #Metodo que se encarga de filtrar el fichero habría que mejorar como obtener los datos importantes.
    # Filtrar nombre.

    match = re.search(r'(?i)soy\s*([A-Z][a-z]+)', text) #Filtra por la palabra "Soy"
    if match:
        name = match.group(1)
        print("Nombre: " + name)
    else:
        print("Nombre no encontrado")
    
    # Filtrar teléfono
    
        match = re.search(r'(?i)[\s|\-|\(]*(\d{3})[\s|\-|\)]*(\d{3})[\s|\-|\(]*(\d{4})([\s|\-|\)]|$)', text)
    if match:
        phone = match.group(1) + match.group(2) + match.group(3)
        print("Teléfono: " + phone)
    else:
        print("Teléfono no encontrado")
    
    # Filtrar correo electrónico
    
        match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    if match:
        email = match.group()
        print("Correo electrónico: " + email)
    else:
        print("Correo electrónico no encontrado")
    
    # Filtrar empresa

    match = re.search(r'(?i)de\s*([A-Z][a-z]+)', text)
    if match:
        empresa = match.group(1)
        print("Empresa: " + empresa)
    else:
        print("Empresa no encontrado")

    #conexion con la base de datos y ejecución de query

    connection.insertquery(name, phone, email, empresa, text)

