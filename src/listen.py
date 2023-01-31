from commands import assistantvoice
import importlib
import difflib
from textblob import TextBlob
import re

commandslist = ["end", "flip", "joke", "roll", "timer", "systime", "add", "subtract", "multiply", "divide", "search", "image", "app"]
fullinputcommands = ["search", "image"]
numinputcommands = ["roll", "add", "subtract", "multiply", "divide"]
command = ''
vort = ''
thing = ""

# find all numbers in the string using regex


def voiceortext(finding, vort):
    if vort == "voice":
        thing = assistantvoice.takeCommand()
    elif vort == "text":
        thing = input(f"{finding}: ")
    return thing


def listen_for_command(vort):
    command = voiceortext("Command", vort)
    command = command.lower()
    blob = TextBlob(command)
    subjects = blob.noun_phrases


    for cmd in commandslist:
        module = importlib.import_module(f'commands.{cmd}')

        if module.command_matches_input(command):
            if cmd not in fullinputcommands or numinputcommands:
                if cmd != "timer":
                    module.execute(subjects)
                if cmd == "timer":
                    whatis = command.split(" ")
                    for i in whatis:
                        if i in ["minute", "second", "hour", "minutes", "seconds", "hours"]:
                            times = i
                        else: 
                            times = "second"
                    numbers = re.findall(r'\d+', command)
                    module.execute(times, numbers)
            elif cmd in fullinputcommands:
                module.execute(command)
            elif cmd in numinputcommands:
                numbers = re.findall(r'\d+', command)
                module.execute(numbers)
            break
    else:
        synonyms = difflib.get_close_matches(command, commandslist, cutoff=0.25)
        for comm in commandslist:
            if comm in synonyms[0]:
                assistantvoice.speak(f"I'm sorry, I don't understand that command. Did you mean {synonyms[0]}?")
                answer = voiceortext("Yes or No? ", vort)
                answer = answer.lower()
                if answer == "yes":
                    try:
                        assistantvoice.speak("Okay")
                        module = importlib.import_module(f'commands.{synonyms[0]}')
                        module.execute(synonyms[0])
                    except FileNotFoundError:
                        assistantvoice.speak("ERROR. COMMAND LIST HAS NO FILE FOR THIS NAME.")
                    break
                else:
                    assistantvoice.speak("Okay, go ahead and try again")
                    break
            else:
                for syn in synonyms:
                    for comm in commandslist:
                        if comm in syn:
                            assistantvoice.speak(f"Did you mean {syn}?")
                            answer = voiceortext("Yes or No? ", vort)
                            answer = answer.lower()
                            if answer == "yes":
                                try:
                                    assistantvoice.speak("Okay")
                                    module = importlib.import_module(f'commands.{syn}')
                                    module.execute(syn)
                                except FileNotFoundError:
                                    assistantvoice.speak("ERROR. COMMAND LIST HAS NO FILE FOR THIS NAME.")
                                break
                            else:
                                assistantvoice.speak("Okay, go ahead and try again")
                                break