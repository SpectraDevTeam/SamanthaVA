import webbrowser
import requests
from googlesearch import search
from commands import assistantvoice

tld = ''

def command_matches_input(input):
    if 'google' in input:
        return True
    else:
        return False

def execute(input):
    # Remove everything beofore Google from the string
    words = input.split()
    index = words.index('for')
    new_words = words[index:]
    new_input = ' '.join(new_words)
    new_input = new_input.replace('for', '')

    url = f"https://www.google.com/search?q={new_input}"


    # Open the file in a browser
    webbrowser.open_new_tab(url)
    assistantvoice.speak(f"Here are ten Results on google for {new_input}")

