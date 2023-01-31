from commands import assistantvoice
import re

result = 0

def command_matches_input(input):
    if 'add' in input:
        return True
    else:
        return False

def execute(numbers):
    result = 0
    for num in numbers:
        result += int(num)
    
    assistantvoice.speak(f"The Answer is {result}")
