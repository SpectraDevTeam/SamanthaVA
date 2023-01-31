from commands import assistantvoice
import random

coin = ("Heads", "Tails")

def command_matches_input(input):
    if 'flip' in input:
        return True
    else:
        return False

def execute(input):
    landed = random.choice(coin)
    assistantvoice.speak(f"It landed {landed}")
    return f"It landed {landed}"
    