import speech_recognition as sr
import pyttsx3
import platform
import os
from playsound import playsound
import subprocess
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
from tempfile import gettempdir

session = boto3.Session()
polly = session.client("polly")

current_os = platform.system()
idvoice = open("voice.txt", "r")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', idvoice)
newVoiceRate = 100
engine.setProperty('rate', newVoiceRate)

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
        query = r.recognize_google(audio, language ='en-US')
    except:
        query = ""
    
    
    return query

def listen_for_wakeup(continuereading):
    r = sr.Recognizer()
    while continuereading == True:
        print("Listening For Wakeup")
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                wakeup = r.recognize_google(audio)
                wakeup = wakeup.lower()
                if "sam" in wakeup:
                    return True
                else:
                    return False
            except:
                continue
