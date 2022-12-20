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
primary_text = command
try:
    translator = Translator()
    traduccion = translator.translate(primary_text, dest="es")
    traduccion_correcta = traduccion.text
except:
    print("Something is wrong with Translation process")

try:
    engine = pyttsx3.init()
    engine.runAndWait()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    print("==============================================================================")
    print("la traduccion al español de lo que dijiste es: ", traduccion_correcta)

    engine.say("Lo que dijiste fue")
    engine.say(traduccion_correcta)
    engine.runAndWait()
    engine.stop()
except:
    print("Something is wrong with the sintetic voice")
