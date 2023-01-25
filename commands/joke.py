from commands import assistantvoice
import random

jokes = []

def command_matches_input(input):
    if 'joke' in input:
        return True
    else:
        return False

def execute(input):
    with open('commands/jokes.txt', 'r') as jokefile:
        lines = jokefile.readlines()
        for line in lines:
            jokes.append(line)
    
    for x in range(len(jokes)):
        jokes[x] = jokes[x][:-2]
    
    jokespeak = random.choice(jokes)
    assistantvoice.speak(f"{jokespeak}")
    