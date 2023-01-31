import pyttsx3

voicelist = []
numvoices = 1

engine = pyttsx3.init()
voices = engine.getProperty('voices')
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

for voice in voices:
    engine.setProperty('voice', voice.id)
    print(f"\nVoice: {voice.name}\n")
    voicelist.append(voice.name)
    engine.say("Hello World! This is my Voice!")
    engine.runAndWait()
    
print("Which voice would you like? Pick the number before the name you would like.")
for i in range(len(voices)):
    print(f"{i+1}. {voices[i].name}")

voicechosen = int(input("voice: "))
engine.setProperty('voice', voices[voicechosen-1].id)
engine.say("This is your chosen Voice!")
engine.runAndWait()

with open("voice.txt", "w") as v:
    for voice in voices:
        if voicelist[numvoices] == voice.name:
            engine.setProperty("voice", voice.id)
            v.write(engine.getProperty("voice"))

print(f"You chose {voicelist[numvoices]} for your voice. If You need to change the voice. Please erase all data from voice.txt and run this program again.")