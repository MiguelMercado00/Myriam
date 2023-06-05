# Code by: Miguel Mercado
# June 2023

import speech_recognition as sr
import subprocess as sub
from gtts import gTTS
import pywhatkit
import datetime
import os
import newspaper
import wikipedia
import webbrowser
import random
import requests
from bs4 import BeautifulSoup
import geocoder

def talk(texto):
    tts = gTTS(text=texto, lang="es")
    tts.save("output.mp3")
    sub.call(["afplay", "output.mp3"])  # Reproduce el audio

def tomar():
    try:
        with sr.Microphone() as voz:
            print("Señor, ¿En qué puedo ayudarle?")
            talk("Señor, ¿En qué puedo ayudarle")

            voice = escuchar.listen(voz)
            rec = escuchar.recognize_google(voice, language="es")
            rec = rec.lower()
            if nombre in rec:
                rec = rec.replace(nombre, '')
                print(rec)
    except:
        print("Señor, no le he entendido")
        talk("Señor, no le he entendido")
        pass
    return rec

def buscar_en_internet(consulta):
    print("Buscando en Internet: " + consulta)
    talk("Buscando en Internet: " + consulta)
    pywhatkit.search(consulta)

def reproducir_musica(musica):
    print("Reproduciendo " + musica)
    talk("Reproduciendo " + musica)
    pywhatkit.playonyt(musica)

def enviar_mensaje_whatsapp(numero, mensaje):
    print("Enviando mensaje a Whatsapp")
    talk("Enviando mensaje a Whatsapp")
    pywhatkit.sendwhatmsg_instantly(numero, mensaje)

def obtener_titulares(url):
    noticias = newspaper.build(url)
    for articulo in noticias.articles[:5]:  # Obtener los primeros 5 titulares
        articulo.download()
        articulo.parse()
        print(articulo.title)
        talk(articulo.title)

def abrir_youtube(inicio):
    print("Abriendo Youtube")
    talk("Abriendo Youtube")
    webbrowser.open(inicio)

def abrir_gmail(inicio):
    print("Abriendo Gmail")
    talk("Abriendo Gmail")
    webbrowser.open(inicio)

def abrir_instagram(inicio):
    print("Abriendo Instagram")
    talk("Abriendo Instagram")
    webbrowser.open(inicio)

def abrir_chatgpt(inicio):
    print("Abriendo ChatGPT")
    talk("Abriendo ChatGPT")
    webbrowser.open(inicio)

def abrir_whatsapp(inicio):
    print("Abriendo Whatsapp")
    talk("Abriendo Whatsapp")
    webbrowser.open(inicio)

def abrir_facebook(inicio):
    print("Abriendo Facebook")
    talk("Abriendo Facebook")
    webbrowser.open(inicio)

def fecha_de_hoy():
    fecha = datetime.datetime.now().strftime('%d/%m/%Y')
    print("Señor, hoy es " + fecha)
    talk("Señor, hoy es " + fecha)

def obtener_ciudad_actual():
    g = geocoder.ip('me')
    if g.city:
        return g.city
    else:
        return None

def temperatura():
    ciudad = obtener_ciudad_actual()
    url = "https://www.google.com/search?q=temperatura+en+" + ciudad
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    temperatura = soup.find("div", class_="BNeawe").text
    print("Señor, la temperatura en " + ciudad + " es de " + temperatura)
    talk("Señor, la temperatura en " + ciudad + " es de " + temperatura)

def abrir_calculadora():
    print("Abriendo calculadora")
    talk("Abriendo calculadora")
    os.system("open -a Calculator")

def abrir_spotify():
    print("Abriendo Spotify")
    talk("Abriendo Spotify")
    os.system("open -a Spotify")

def abrir_notion():
    print("Abriendo Notion")
    talk("Abriendo Notion")
    os.system("open -a Notion")

def abrir_iterm():
    print("Abriendo iTerm")
    talk("Abriendo iTerm")
    os.system("open -a iTerm")

def abrir_vscode():
    print("Abriendo Visual Studio Code")
    talk("Abriendo Visual Studio Code")
    os.system("open -a Visual\ Studio\ Code")


def contar_chiste():
    chistes = [
        "¿Qué le dice un pez a otro? Nada.",
        "¿Qué le dice un jaguar a otro? Jaguar you.",
        "¿Qué le dice un árbol a otro? Estamos en las ramas.",
        "¿Qué le dice un espagueti a otro? El cuerpo me pide salsa.",
        "¿Qué le dice un café a otro? Para café.",
        "¿Qué le dice una impresora a otra? Esa hoja es tuya o es impresión mía.",
        "¿Qué le dice un pato a otro? Estamos empatados.",
        "¿Qué le dice un árbol a otro? Nos vemos en el bosque.",
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "¿Por qué los peces no usan Facebook? Porque ya están enganchados al acuario.",
        "¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.",
        "¿Por qué los tomates van al colegio? Porque quieren ser salsa de mayor.",
        "¿Qué hace una abeja en el gimnasio? ¡Zummmba!"
    ]
    chiste = random.choice(chistes)
    print(chiste)
    talk(chiste)

def frases_motivadoras():
    frases = [
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "La disciplina es el puente entre metas y logros.",
        "Si no luchas por lo que quieres, no llores por lo que pierdes.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "No te preocupes por los fracasos, preocúpate por las posibilidades que pierdes cuando ni siquiera lo intentas.",
        "El único modo de hacer un gran trabajo es amar lo que haces.",
        "El camino hacia el éxito está siempre en construcción.",
        "El único límite para alcanzar tus sueños eres tú mismo.",
        "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. Si amas lo que haces, tendrás éxito.",
        "La motivación nos impulsa a comenzar y el hábito nos permite continuar.",
        "Cada experto en algún punto fue un principiante. No tengas miedo de comenzar.",
        "El mejor momento para plantar un árbol fue hace 20 años. El segundo mejor momento es ahora.",
        "El éxito no es definitivo, el fracaso no es fatal: lo que cuenta es el coraje para continuar.",
        "El único lugar donde el éxito viene antes que el trabajo es en el diccionario.",
        "No hay atajos para cualquier lugar que valga la pena.",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
        "La clave del éxito es comenzar antes de que estés listo.",
        "El único lugar donde el éxito viene antes que el trabajo es en el diccionario.",
        "Si no te gusta algo, cámbialo. Si no puedes cambiarlo, cambia tu actitud.",
        "El éxito es la capacidad de ir de fracaso en fracaso sin perder el entusiasmo.",
        "El éxito no es definitivo, el fracaso no es fatal: lo que cuenta es el coraje para continuar.",
        "Si no te gusta algo, cámbialo. Si no puedes cambiarlo, cambia tu actitud.",
        "La motivación nos impulsa a comenzar y el hábito nos permite continuar.",
        "Si crees que puedes, ya estás a medio camino.",
        "No tengas miedo de renunciar a lo bueno para ir tras lo grandioso.",
        "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.",
        "No importa lo lento que vayas, siempre y cuando no te detengas.",
        "La disciplina es el puente entre metas y logros.",
        "El único fracaso real en la vida es no intentarlo.",
        "El éxito no es para los que piensan en ello, sino para los que lo persiguen.",
        "Los obstáculos son esas cosas espantosas que ves cuando apartas los ojos de tu meta.",
        "Cree en ti mismo y todo será posible.",
        "La única manera de hacer un gran trabajo es amar lo que haces."
    ]
    frase = random.choice(frases)
    print(frase)
    talk(frase)

def buscar_wikipedia(tema):
    print("Buscando en Wikipedia: " + tema)
    talk("Buscando en Wikipedia: " + tema)
    try:
        contenido = wikipedia.summary(tema, sentences=3)
        print(contenido)
        talk(contenido)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Hay varias opciones relacionadas. Por favor, sé más específico.")
        talk("Hay varias opciones relacionadas. Por favor, sé más específico.")
    except wikipedia.exceptions.PageError as e:
        print("No se encontró ninguna página relacionada con ese tema.")
        talk("No se encontró ninguna página relacionada con ese tema.")

nombre = 'myriam'
escuchar = sr.Recognizer()

def run_myriam():
    while True:
        rec = tomar()
        if 'reproduce' in rec:
            musica = rec.replace('reproduce', '')
            reproducir_musica(musica)
        elif 'hora' in rec:
            time = datetime.datetime.now().strftime('%H:%M')
            print("Señor, son las " + time)
            talk("Señor, son las " + time)
        elif 'temperatura' in rec:
            temperatura()

        elif 'hasta luego' in rec:
            if datetime.datetime.now().hour < 12:
                talk("Hasta luego señor. Que tenga un buen día.")
            elif 12 <= datetime.datetime.now().hour < 18:
                talk("Hasta luego señor. Que tenga una buena tarde.")
            else:
                talk("Hasta luego señor. Que tenga una buena noche.")
            os._exit(0)  # Termina el programa de manera abrupta
        elif 'busca' in rec:
            consulta = rec.replace('busca', '')
            buscar_en_internet(consulta)
        elif 'envía un mensaje' in rec:
            numero = "+57 xxx xxxxxxx" # Número de celular al que va a llegar el mensaje
            mensaje = "Hola"
            enviar_mensaje_whatsapp(numero, mensaje)
        elif 'calculadora' in rec:
            abrir_calculadora()
        elif 'spotify' in rec:
            abrir_spotify()
        elif 'notion' in rec:
            abrir_notion()
        elif 'iterm' in rec:
            abrir_iterm()
        elif 'visual studio code' in rec:
            abrir_vscode()
        elif 'chiste' in rec:
            contar_chiste()
        elif 'día' in rec:
            fecha_de_hoy()
        elif 'youtube' in rec:
            abrir_youtube('https://www.youtube.com/')
        elif 'instagram' in rec:
            abrir_instagram('https://www.instagram.com/')
        elif 'gmail' in rec:
            abrir_gmail('https://mail.google.com/mail/u/0/#inbox')
        elif 'chat' in rec:
            abrir_chatgpt('https://chat.openai.com/')
        elif 'noticias' in rec:
            obtener_titulares('https://www.bbc.com/news')
        elif 'whatsapp' in rec:
            abrir_whatsapp('https://web.whatsapp.com/')
        elif 'facebook' in rec:
            abrir_facebook('https://www.facebook.com/')
        elif 'wikipedia' in rec:
            tema = rec.replace('wikipedia', '')
            buscar_wikipedia(tema)
        elif 'frase motivadora' in rec:
            frases_motivadoras()
        elif 'prepárame' in rec:
            fecha_de_hoy()
            temperatura()
            frases_motivadoras()


run_myriam()

