from commands import assistantvoice
import re


def command_matches_input(input):
    if 'divide' in input:
        return True
    else:
        return False

def execute(input):
    result = 0
    times = 0
    nums = [0, 0]
    while(times != 2):
        for match in re.finditer(r'\d+', input):
            
            nums[times] += int(match.group(0))
            print(nums[times])
            times += 1
        
    result = nums[0] / nums[1]
    assistantvoice.speak(f"The Answer is {result}")
