from googletrans import Translator
import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print("lo que dijiste fue: ", command)
except:
    print("something is not working")


translator = Translator()

primary_text = command

traduccion = translator.translate(primary_text, dest="es")
traduccion_correcta = traduccion.text


engine = pyttsx3.init()
engine.runAndWait()

rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

engine.say(str(traduccion_correcta))
engine.runAndWait()
engine.stop()
