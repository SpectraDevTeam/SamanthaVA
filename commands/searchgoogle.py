import webbrowser
import requests
from googlesearch import search
import assistantvoice

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

    

    # Write the URL's to a .txt file
    with open('googlesearch.txt', 'w') as f:
        for url in search(new_input, tld="co.in", num=10, stop=10, pause=2):
            f.write(url + '\n')

    f.close()


    # Open the file in a browser
    webbrowser.open_new_tab("file:///Users/spectrathefox/Desktop/Repos/SamanthaVA/googlesearch.txt")
    assistantvoice.speak(f"Here are ten Results on google for {new_input}")

