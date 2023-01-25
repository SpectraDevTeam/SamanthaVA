from commands import assistantvoice
import time
from playsound import playsound

num = ''

def command_matches_input(input):
    if 'timer' in input:
        return True
    else:
        return False

def execute(input):
    num = ''
    for chr in input:
        if chr.isdigit():
    
            num += f'{chr}'
    
    if 'minute' in input:

        assistantvoice.speak(f"Timer for {num} minutes, starting now")
    if 'hour' in input:

        assistantvoice.speak(f"Timer for {num} hours, starting now")
    if 'second' in input:

        assistantvoice.speak(f"Timer for {num} seconds, starting now")
    
    num = ''
    for chr in input:
        if chr.isdigit():
            
            num += f'{chr}'
    num = int(num)
    if 'minute' in input:
        num *=  60
    if 'hour' in input:
        num *= 60
        num *= 60

    time.sleep(num)
    playsound('/Users/spectrathefox/Desktop/Repos/samantha/SamVA/audiofiles/timeroff.mp3')
    playsound('/Users/spectrathefox/Desktop/Repos/samantha/SamVA/audiofiles/timeroff.mp3')
    assistantvoice.speak("Timer is Done")
