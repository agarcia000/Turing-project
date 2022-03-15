from math import e
import time
import docx
import speech_recognition as sr
import pyttsx3
import webbrowser
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

listener = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', rate-50)
from docx import Document
 
#try:
    #with sr.Microphone() as source:
       # print("Te estoy escuchando...")
        #voice = listener.listen(source)
       # rec = listener.recognize_google(voice)
       # print(rec)
#except:
    #pass

name = 'Areda'
nameusuario = ''
confirmacion= ''
Pregunta=input("quieres que hable en voz alta?")

print("Porfavor introduzca su nombre de usuario")
input(nombredeusuario)
print("Quieres que te llames"+nombredeusuario+"?")
input(confirmacion)
print("Entonces tu nombre correcto es"+nombredeusuario)
if confirmacion == ("no") or ("No"):
    print("Entonces escribe el nombre correctamente ahora:")
    input(nombredeusuario)
elif confirmacion == ("si") or ("Si"):
    print("Entiendo, bienvenido" + nameusuario)

while(1):
        if text == 0:
            continue
  
        if "acabar" in listen or "adios" in listen or "descansa" in listen or "Adios" in listen or "Adios" in listen or "Descansa" in listen:
            assistant_speaks("Ok bye, "+ name+'.')
            break

def functions():
    while(1):  
        if text == 0:
            continue
  
        if "acabar" in listen or "adios" in listen or "descansa" in listen or "Adios" in listen or "Adios" in listen or "Descansa" in listen:
            assistant_speaks("Ok bye, "+ name+'.')
            break
    rec = listen("Esperando nuevas ordenes de usted...")
    if "Hablemos de algo" in rec or "hablemos de algo" in rec or "me aburro" in rec or("Me aburro") in rec: 
     assistant_speaks("Hablemos de algo interesante, puedo entablar una conversacion o si lo prefieres dime algo que te guste y buscare informacion incluso...")
    elif 'presentate':
     assistant.speaks("Si claro, me llamo Areda y por ahora no tengo tantas funciones pero como podeis ver he sido creada por estos dos alumnos. Aunque no se hacer muchas cosas estoy segura que podre seguir aprendiendo poco a poco")
    else:
        asssistant.speaks("Perdon puedes repirlo porfavor?")