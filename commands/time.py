import datetime
from commands import assistantvoice

timeamount = ["minute", 'hour', 'second']
hours = ''

def command_matches_input(input):
    if 'time' in input and "timer" not in input:
        return True
    else:
        return False

def execute(input):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    if current_time[0] == '1' and current_time[1] != '1' and current_time[1] != '2':
        hours = ''
        for char in current_time:
            
            hours += char
            if char == ":":
                break
        hours = hours[:-1]
        print(hours)
        hours = int(hours) - 12
        print(hours)
        current_time = str(hours) + current_time[2:]
        print(current_time)
    if current_time[3] == '0' and current_time[4] == '0':
        assistantvoice.speak(f"The Current Time is {current_time} o clock")  

    else:
        assistantvoice.speak(f"The Current Time is {current_time}")  