from commands import assistantvoice
import re


def command_matches_input(input):
    if 'subtract' in input:
        return True
    else:
        return False

def execute(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= int(num)
        
    assistantvoice.speak(f"The Answer is {result}")
