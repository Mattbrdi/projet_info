import pygame 
import sys
from button import Button
from game import Game
from instructions import Instructions

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Portal des élèves")

# Load background image
background = pygame.image.load("images/main_menu.png")

# Load title
font = pygame.font.SysFont("Georgia", 60)
text = font.render("Portal des élèves", True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.center = (400, 100)

# Set up the buttons
start_button = Button(60, 300, 200, 50, "Start", font="Georgia")
instructions_button = Button(60, 400, 200, 50, "How-To-Play", font="Georgia")
quit_button = Button(60, 500, 200, 50, "Quit", font="Georgia")

# Main loop
running = True
is_display_instructions = False
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if start_button.is_clicked(x, y):
                is_display_instructions = False
                game = Game()
                game.run(['carte_2.txt', 'carte_3.txt','carte_4.txt'])
            elif instructions_button.is_clicked(x, y):
                instructions = Instructions()
                instructions.run()
            elif quit_button.is_clicked(x, y):
                sys.exit()

    # Draw the background
    screen.blit(background, (70, 70))

    # Draw the title
    screen.blit(text, text_rect)

    # Draw the buttons
    start_button.draw(screen)
    instructions_button.draw(screen)
    quit_button.draw(screen)
    
    # Update the screen
    pygame.display.flip()