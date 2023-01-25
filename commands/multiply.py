from commands import assistantvoice
import re

result = 0

def command_matches_input(input):
    if 'multiply' in input:
        return True
    else:
        return False

def execute(input):
    result = 0
    for match in re.finditer(r'\d+', input):
        result *= int(match.group(0))
    
    assistantvoice.speak(f"The Answer is {result}")