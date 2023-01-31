from commands import assistantvoice
import random
import listen

wakeupreply = ("Hello, What would you like me to do?", "Yes?", "How can I help?", "Welcome back, what can I do for you?", "Ready to get started, what can I do for you?", "I'm here to help, what do you need?", "What's on your mind?", "How may I assist you?")
vort = "voice"

#Always Runs
while True:
    keeplisten = True

    if vort == "voice":
        gotocommand = assistantvoice.listen_for_wakeup(keeplisten)
        if gotocommand:
            assistantvoice.speak(random.choice(wakeupreply))
            keeplisten = False
            listen.listen_for_command(vort)
            

    elif vort == "text":
        assistantvoice.speak(random.choice(wakeupreply))
        listen.listen_for_command(vort)
