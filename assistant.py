import random
import importlib
from commands import assistantvoice

commandslist = ["endprogram", "flip", "joke", "roll", "settimer", "time", "add", "subtract", "multiply", "divide", "googlesearch", "imagesearch"]

#other variables
wakeupreply = ("Hello, What would you like me to do?", "Yes?", "How can I help?")
command = ''
vort = ''

def voiceortext(finding):
    if vort == "voice":
        thing = assistantvoice.takeCommand()
    elif vort == "text":
        thing = input(f"{finding}: ")
    return thing

#Do you want to type or talk
if vort != 'text' and vort != 'voice':
    vort = input("Would You like to start in text or voice mode? ")
    vort = vort.lower()

print(f"You Chose {vort} Mode")

#Always Runs
while True:
    

    if vort == "voice":
        wakeup = assistantvoice.takeCommand()
        assistantvoice.speak(random.choice(wakeupreply))

    elif vort == "text":
        assistantvoice.speak(random.choice(wakeupreply))
        wakeup = "sam"

    #if wakeup word heard
    if 'Sam' or 'Samantha' in wakeup:
        command = voiceortext("Command")
        for cmd in commandslist:
            module = importlib.import_module(f'commands.{cmd}')
            if module.command_matches_input(command):
                module.execute(command)