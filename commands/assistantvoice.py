import speech_recognition as sr
import pyttsx3

idvoice = "com.apple.voice.premium.en-UK.Serena"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', idvoice)
newVoiceRate = 100
engine.setProperty('rate', newVoiceRate)
vort = ""

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Now listening")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)  
    try:
        print("Deciphering")   
        query = r.recognize_google(audio, language ='en-US')
        print("You Said: " + query)
  
    except Exception as e:
        print(e)
        print("Did not hear anything") 
        return "None"
    
    
    
    return query

def voiceortext(finding):
    if vort == "voice":
        thing = takeCommand()
    elif vort == "text":
        thing = input(f"{finding}: ")
    return thing