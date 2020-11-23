import pygame
import move
import network
pygame.init()


win = pygame.display.set_mode((480, 320))
pygame.display.set_caption("Fight Night")



net = network.network()

move1=move.move("heal")


bg = pygame.image.load('images/Backgrounds/lava.jpg')
char = pygame.image.load('images/Fronts/Kanye.png')

clock= pygame.time.Clock()


moveCounter=0


def redrawGameWindow():
    global moveCounter
    win.blit(bg, (0, 0))  # This will draw our background image at (0,0)
    win.blit(char, (0, 0))
    #move animation
    if moveCounter < len(move1.images):
        win.blit(move1.images[moveCounter], (0,0))
    else:
        moveCounter=0
    moveCounter=moveCounter+1
    pygame.display.update()

def send_data():
    data=("1"+":"+"Trump"+":"+"100"+":"+"slash")
    reply = net.send(data)
    return reply

def parse_data(data):
    try:
        d =data.split(":")
        return (int (d[0]) , d[1], int(d[2]), d[3])
    except:
        return (1,"Kanye", 1,"none")

run = True
sent=False
while run:
    clock.tick(24)
    pygame.time.delay(100)
    print(send_data())
    sent=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    redrawGameWindow()

pygame.quit()