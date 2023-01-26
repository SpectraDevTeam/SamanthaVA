import webbrowser
from commands import assistantvoice

def command_matches_input(input):
    if 'images' and 'google' in input:
        return True
    else:
        return False

def execute(input):
    words = input.split()

    index = words.index('for')
    new_words = words[index:]
    new_input = ' '.join(new_words)
    new_input = new_input.replace('for', '')

    webbrowser.open("https://www.google.com/search?tbm=isch&q=" + new_input)
    assistantvoice.speak(f"Here are the Results on google images for {new_input}")

execute('search google images for cookies')