import pygame
import move
import textwrap
import network
import sys
import fighter
from fighter import *
from pygame.locals import *
from random import randint
pygame.init()
global ability, HP, enemy_HP, querry, current_buff, armor, enemy, previous_game, your_turn, active_player, damage, refresh, current_buff
active_player = 0
HP = 100
your_turn = 0
enemy_HP = 100
armor = 0
current_buff = 0
refresh = 0
game = 0
damage = 0
ability = "none"
querry = ""
my_char =""
my_background = ""
enemy = "jim"
previous_game = "WELCOME"
#remember to reset buff at the end of each game
win = pygame.display.set_mode((480, 320))
pygame.display.set_caption("Fight Night")


net = network.network()

clock= pygame.time.Clock()


moveCounter=0

def new_game():
    global HP, enemy_HP, current_buff, refresh, armor, ability, querry
    HP = 100
    enemy_HP = 100
    current_buff = 0
    refresh = 0
    armor = 0
    ability = "none"
    querry = send_data()+"penis head"
    print ("querry was sent")
    argument_one = randint(1, 13)
    argument_two = randint(1, 4)
    switch_one = {
        1: "addison",
        2: "elon",
        3: "jim",
        4: "kanye",
        5: "linus",
        6: "mike",
        7: "niki",
        8: "rick",
        9: "ronaldo",
        10: "serena",
        11: "tiger",
        12: "tom",
        13: "trump",
   }
    switch_two = {
        1: "apple",
        2: "lava",
        3: "uvmgreen",
        4: "wrestling",
    }
    armor = get_armor(str(switch_one.get(argument_one)))
    print(armor)
    return switch_one.get(argument_one), switch_two.get(argument_two)

#fetches character name from a querry input
def get_char_name(stringq):
    arr = stringq.split(":")
    return arr[1]

#function to apply damage
def take_damage(dam_instance):
    global armor, HP
    armor = get_armor(str(my_char))
    reduction = armor + current_buff
    if dam_instance<reduction:
        HP = HP
    else:
        HP = HP + reduction - dam_instance

def redrawGameWindow():
    global game, refresh, enemy
    global moveCounter, my_char, my_background, previous_game, ability

    if game==0:
        bg = pygame.image.load('images/Backgrounds/uvmgreen.jpg')
        win.blit(bg, (0, 0))
        font = pygame.font.SysFont('Helventiaa', 80)
        win.blit(font.render(previous_game, True, (220,220,220)), (100, 30))
    if (game == 1 or game == 2) and refresh == 0:
        enemy = get_char_name(send_data())
    if game == 1 or game == 2:
        bg = pygame.image.load('images/Backgrounds/'+str(my_background)+'.jpg')
        char = pygame.image.load('images/Backs/'+str(my_char)+'.png')
        win.blit(bg, (0, 0))  # This will draw our background image at (0,0)
        win.blit(char, (0, 0))
        try:
            enemy_char = pygame.image.load('images/Fronts/'+str(enemy)+'.png')
            enemy_char = pygame.transform.scale(enemy_char, (120, 120))
            win.blit(enemy_char, (290, 0))
        except (FileNotFoundError):
            refresh = 0

        #label boxes
        char_label_box = pygame.Rect(250, 200, 200, 50)
        pygame.draw.rect(win, [240, 200, 200], char_label_box)
        pygame.draw.polygon(win,[240, 200, 200],[[200, 250], [250, 250], [250, 200]], 0)
        #enemy label boxes
        enemy_label_box = pygame.Rect(60, 8, 200, 50)
        pygame.draw.rect(win, [240, 200, 200], enemy_label_box)
        pygame.draw.polygon(win,[240, 200, 200],[[260, 8], [260, 58], [310, 8]], 0)
        font = pygame.font.SysFont('Arial', 15)
        win.blit(font.render(str(enemy).upper()+" (opponent)", True, (0,0,0)), (64, 12))
        win.blit(font.render(str(my_char).upper()+" (you)", True, (0,0,0)), (254, 202))
        win.blit(font.render("HP: "+str(enemy_HP), True, (0,0,0)), (64, 34))
        win.blit(font.render("HP: "+str(HP), True, (0,0,0)), (254, 224))

        enemy_hp_box = pygame.Rect(125, 37, enemy_HP, 10)
        pygame.draw.rect(win, [255, 0, 0], enemy_hp_box)
        char_hp_box = pygame.Rect(315, 229, HP, 10)
        pygame.draw.rect(win, [0, 0, 255], char_hp_box)

        #take your turn
    if(game==2):
        ability_one_box = pygame.Rect(60, 260, 150, 50)
        pygame.draw.rect(win, [50, 200, 50], ability_one_box)
        ability_two_box = pygame.Rect(260, 260, 150, 50)
        pygame.draw.rect(win, [50, 200, 50], ability_two_box)
        pygame.draw.rect(win, [0, 0, 0], ability_one_box,4)
        pygame.draw.rect(win, [0, 0, 0], ability_two_box,4)
        font = pygame.font.SysFont('Arial', 16)
        total = 0
        ability_1 = get_ability(str(my_char))
        ability_2 = get_ability2(str(my_char))
        for i in ability_1:
            total = total + 1
        total = int((13 - total)*1.2)+1
        for i in range(total):
            ability_1 = " " + ability_1
        total = 0
        for i in ability_2:
            total = total + 1
        total = int((13 - total)*1.5)+1
        for i in range(total):
            ability_2 = " " + ability_2

        win.blit(font.render(ability_1, True, (0,0,0)), (63, 270))
        win.blit(font.render(ability_2, True, (0,0,0)), (263, 270))
 #   move animation

    move1=move.move(ability)
    if moveCounter < len(move1.images):
        if game == 1:
            if ability == "heal" or ability == "buff":
                win.blit(move1.images[moveCounter], (40,100))
            else:
                win.blit(move1.images[moveCounter], (250,0))
        else:
            if ability == "heal" or ability == "buff":
                win.blit(move1.images[moveCounter], (250,0))
            else:
                win.blit(move1.images[moveCounter], (40,100))
    else:
        moveCounter=0
    moveCounter = moveCounter+1


    #pygame exit function
    button = pygame.Rect(0, 0, 30, 30)  # creates a rect object
    pygame.draw.rect(win, [200, 10, 10], button)
    font = pygame.font.SysFont('Arial', 27)
    win.blit(font.render('X', True, (0,0,0)), (5, 0))

    #function to start a new game
    if game==0:
        button = pygame.Rect(127, 130, 230, 40)  # creates a rect object
        pygame.draw.rect(win, [100, 20, 200], button)
        font = pygame.font.SysFont('Helventica', 55)
        win.blit(font.render('NEW GAME', True, (255,255,255)), (133, 134))

    pygame.display.update()
#function called if exit button is clicked
def quit():
    sys.exit()

#use an ability
def execute_ability(ability_num):
    global current_buff, game, refresh, damage, ability, enemy_HP, enemy, HP
    refresh = 1
    if(ability_num==1):
        ability_content = get_ability(str(my_char))
        print(ability_content,"ability content")
        ability_str = str(ability_content)
    elif(ability_num==2):
        ability_content = get_ability2(str(my_char))
        print(ability_content,"ability content")
        ability_str = str(ability_content)
    arr = use_ability(ability_str)
    type = arr[0]
    ability = type
    value = arr[1]
    if (type=="buff"):
        current_buff = current_buff + value
        damage = value
    elif (type=="debuff"):
        current_buff = current_buff + value
        damage = value
    elif (type=="heal"):
        damage = value
        HP = HP + damage
        if HP> 100:
            HP = 100
    else:
        damage = get_damage(value)
    global your_turn
    your_turn = 1
    send_data()
    game = 1
    enemy_armor = get_armor(str(enemy))
    if damage > (enemy_armor - current_buff) and (type == "jim" or type=="slash" or type =="burst" or type=="punch"):
        enemy_HP = enemy_HP - damage + enemy_armor - current_buff

def send_data():
    global damage, ability, active_player, your_turn
    data=(str(active_player)+":"+str(my_char)+":"+str(damage)+":"+ability+":"+str(your_turn))
#def send_turn():
#    global damage, ability, active_player, your_turn
#    data=(str(active_player)+":"+str(my_char)+":"+str(damage)+":"+ability+":"+"1")

    reply = net.send(data)
    return reply

def parse_data(data):
    try:
        d =data.split(":")
        return (int (d[0]) , d[1], int(d[2]), d[3], int(d[4]))
    except:
        return (1,"Jim", 1,"none")

run = True
sent=False
while run:
    # run at the start
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    flip = 0
#new game button
    if (game == 0):
        if 127+230 > mouse[0] > 127 and 130+40 > mouse[1] > 130:
            if click[0] == 1:
                new_game()
                my_char = new_game()[0]
                my_background = new_game()[1]
                if (refresh == 0):

                    print("Querry"+querry+str(HP))
                    enemy = get_char_name(querry)
                if (active_player == 0):
                    game = 2
                else:
                    game = 1
                    your_turn = 1

#ability execute button
#ability 1
    elif (game == 2):
        if 60+150 > mouse[0] > 60 and 300 > mouse[1] > 260:
            if click[0] == 1:
                execute_ability(1)
                flip = 1
#ability 2
        if 260+150 > mouse[0] > 260 and 300 > mouse[1] > 250:
            if click[0] == 1:
                execute_ability(2)
                flip = 1
    clock.tick(24)
    pygame.time.delay(100)
    info = send_data()
    #wait for your turn
    if(game==1):
       if parse_data(info)[4]==1:
            game=2
            your_turn = 0
            ability = parse_data(info)[3]
            if(parse_data(info)[3]=="heal"):
                enemy_HP = enemy_HP + parse_data(info)[2]
                if (enemy_HP)>100:
                    enemy_HP = 100
            elif(parse_data(info)[3]=="buff"):
                current_buff = current_buff - parse_data(info)[2]
            elif(parse_data(info)[3]=="debuff"):
                current_buff = current_buff - parse_data(info)[2]
            else:
                take_damage(parse_data(info)[2])
    print(info)
    if(flip == 1):
        your_turn = 0
        flip = 0
    sent=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #quit button
    if 0+30 > mouse[0] > 0 and 0+30 > mouse[1] > 0:
        if click[0] == 1:
            quit()


    if(enemy_HP<0):
        previous_game = "YOU WON"
        game = 0
    if (HP<0):
        previous_game = "YOU LOST"
        game = 0
    redrawGameWindow()


pygame.quit()
