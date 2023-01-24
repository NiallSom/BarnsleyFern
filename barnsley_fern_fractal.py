import pygame
import random
end = False
while not end:
 colour = input("What color? Green(g) or Multi-coloured(m): ")
 if colour =="g" or colour =="m":
    end = True
 else:
    print("Sorry! That option is not available, please try again.")
pygame.init()
width,height = 1000,1000
screen = pygame.display.set_mode((width,height))#creates a window for the visual
clock = pygame.time.Clock()#for FPS, quicker if it is not used
pygame.display.set_caption("Chaos fractal")
x,y = 0,0
def main(x,y):
    formulas = [(0.00 * x + 0.00 * y, 0.00 * x + 0.16 * y + 0.00),#1% chance
             (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60),#85% chance
             (0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.60),#7% chance
            (-0.15 * x + 0.28 * y,0.26 * x + 0.24 * y + 0.44)]#7% chance
    ranChoice = random.choices(formulas,weights=(1,85,7,7))
    return ranChoice[0][0],ranChoice[0][1]
while 1:
 #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    x,y = main(x,y)
    if colour.lower() == "g":
        fernColour = (0,255,0)
    elif colour.lower() == "m":
        fernColour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.circle(screen,(fernColour),(85*x+450,-57*y+750),1)
    pygame.display.flip()
pygame.quit()
