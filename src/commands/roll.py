from commands import assistantvoice
import random

num = ''

def command_matches_input(input):
    if 'roll' in input:
        return True
    else:
        return False

def execute(input):
    num = ''

    for chr in input:
        if chr.isdigit():
            
            num += f'{chr}'
    if num.isdigit() == False:
        assistantvoice.speak("How many sides")
        num = assistantvoice.voiceortext("Sides")
    if num.isdigit():
        gennum = random.randint(1, int(num))

    assistantvoice.speak(f"You rolled a {gennum} out of {num}")