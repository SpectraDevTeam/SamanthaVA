from commands import assistantvoice

def command_matches_input(input):
    if 'end' in input:
        return True
    else:
        return False

def execute(input):
    assistantvoice.speak("Goodbye")
    exit()
    