import pygame
import time
from commands import assistantvoice
from playsound import playsound

num = ''
timeset = ''
stop = False

def command_matches_input(input):
    if 'timer' in input:
        return True
    else:
        return False

def execute(string, input):
    stop = False
    while stop != True:
        timeset = ''
        for num in input:
            timeset += num

        timeset = int(timeset)

        if timeset == 1:
            assistantvoice.speak(f"Timer for {timeset} {string}, starting now")
        else: 
            assistantvoice.speak(f"Timer for {timeset} {string}s, starting now")
        if string == "minute":
            timeset = timeset * 60
        elif string == "hour":
            timeset = timeset * 3600
        elif string == "second":
            pass


        pygame.init()
        pygame.font.init()

        screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Timer")
        font = pygame.font.SysFont("comicsans", 60)

        timer_start = 0
        timer_current = 0
        while timer_start <= timeset:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    assistantvoice.speak("Timer has been cancelled")
                    stop = True
            
            timer_current = timeset - timer_start
            
            timer_text = font.render(str(timer_current), True, (255, 255, 255))
            screen.blit(timer_text, (200 - timer_text.get_width()//2, 200 - timer_text.get_height()//2))
            pygame.display.update()
            timer_start += 1
            time.sleep(1)
            screen.fill((0, 0, 0))

        

        assistantvoice.speak("Timer is Done")
        stop = True
    if stop == True:
        pygame.quit()
