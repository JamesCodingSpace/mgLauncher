# MiniGame Launcher
A Python-Project by **Alex**, **Jonas** and **Jamie**
_v 0.1_

## Explanation
In the ever-expanding world of gaming, convenience and accessibility have become paramount for enthusiasts of all levels. 
Enter our Mini Game Launcher, a groundbreaking platform designed to streamline your gaming experience like "never" before.
Imagine having three of your favorite games neatly organized and readily accessible from one centralized hub. 
That's precisely what the Mini Game Launcher offers. 
It's a compact, user-friendly application that allows gamers to launch and play them effortlessly.
****
## Key Features
1. **Centralized Library:** Say goodbye to rummaging through various folders or icons scattered across your desktop. The Mini Game Launcher consolidates all your  games into one convenient location, providing quick and easy access to each title.

2. **Customizable Interface:** Personalization is key, and the Mini Game Launcher delivers. Customize your launcher's interface to suit your preferences using our given code.

3. **Instant Access:** With just a few clicks, launch any game in your library instantly. No more navigating through multiple menus or waiting for lengthy loading times. The Mini Game Launcher prioritizes efficiency, ensuring you spend more time gaming and less time waiting.

4. **Automatic Updates:** Stay up-to-date with the latest patches and game enhancements without lifting a finger. 

****
## How to get started
Getting started with the Mini Game Launcher is a breeze:

1. Download: Simply download the Mini Game Launcher from our official website or your preferred digital distribution platform.

2. Installation: Follow the on-screen instructions to install the launcher onto your device. Don't worry; the process is quick and straightforward.

3. Customize: Tailor the launcher's interface to your liking by adjusting settings and preferences to suit your gaming habits.

4. Start Gaming: With your library organized and accessible, dive into your favorite title with unparalleled ease and efficiency.

****
## Updates
Here you can see future updates
****
## Credits
Created for programming class at *DHBW Bad Mergentheim*
Questions? *jamie_rohner* on Discord










# Neu
import pygame
import time
import random

pygame.init()

# Farbdefinitionen
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 185, 0)
green2 = (0, 165, 0)
blue = (50, 153, 213)
darkblue = (0, 0, 139)

# Initialisierung des Spiels
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))      #erstellt das Fenster in der zuvor definierten größe
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()                                 # Uhr (für Framerrate wichtig)
snake_block = 10
snake_speed = 8

font_style = pygame.font.SysFont(None, 30)
FONT_STYLE = pygame.font.SysFont(None, 100)

# Funktion zum Zeichnen der Schlange
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, darkblue, [x[0], x[1], snake_block, snake_block])

# Funktion zum Anzeigen der Punkte
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def field():
    running = True
    for y in range(dis_height):
        for x in range(dis_width):
            if (x + y) % 2 == 0:
                color = green
            else:
                color = green2
            pygame.draw.rect(dis, color, (x * snake_block, y * snake_block, snake_block, snake_block))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.display.update()

# Funktion für das eigentliche Spiel
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            over = FONT_STYLE.render("GAME OVER", True, red)
            dis.blit(over, [dis_width//7, dis_height//2.5])
            info = font_style.render("Quit: press Q     Restart: press C", True, white)
            dis.blit(info, [dis_width//3, 0])
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: # Tastenbelegung after game
                    if event.key == pygame.K_q: # wenn Q gedrückt wird endet das Spiel
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: # wird C gedrückt wird das Spiel neu gestartet
                        gameLoop()

        for event in pygame.event.get(): # tastenbelegung in game
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        
        #dis.fill(field()) # Bildschirgestalltung
        # Zeichne das Farbraster
        for y in range(dis_height):
            for x in range(dis_width):
                if (x + y) % 2 == 0:
                    color = green
                else:
                    color = green2
                pygame.draw.rect(dis, color, (x * snake_block, y * snake_block, snake_block, snake_block))
        
        #es geht mit ursprünglichem Programm weiter
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake: # überprüfung der Länge der Schlage (test ob die Schlange etwas gegessen hat)
            del snake_List[0]

        for x in snake_List[:-1]: # überprüfung der Kollision mit sich selbst
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List) #Zeichnen der Schlange
        Your_score(Length_of_snake - 1)

        pygame.display.update()  

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed) #das Spiel versucht die framerrate auf die Geschwindigkeit 'snake_speed' einzustellen
    
    #pygame.quit()
    quit()

gameLoop()
