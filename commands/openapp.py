import subprocess
import os
import assistantvoice

def command_matches_input(input):
    if 'app' in input:
        return True
    else:
        return False

def execute(input : str):
    input = input.replace("open ", "")
    input = input.capitalize()
    try:
        subprocess.run(["open", "-a", input], check=True)
        assistantvoice.speak(f"{input} opened successfully")
    except FileNotFoundError:
        print(f"\nApplication not found: {input}\n")
        assistantvoice.speak("Application not found")
