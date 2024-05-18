import time
import random
import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

tomatoes = 0
total_tomatoes = 0
tomato_increase = 1
tomato_cooldown = 1000
last_tomato = pygame.time.get_ticks()
tomatoes_consumed = 0
tomatoes_tossed = 0
tomatoes_have_been_consumed = False
tomatoes_have_been_tossed = False
walmart = False
enemy_tick = 0
enemy_cooldown = 1
potato_carcas = 0
purchased_damage = False
damage_up_tick = 0
d_up_cost = 10
f_up_cost = 20
tomatoes_exchange_total = 20
enemy_chance = False
total_enemies = 0
enemies_defeated = 0
fertilizer_tick = 0
purchased_fertilizer = False
lasterest_enemy_cooldown = 1
lasterest_enemy_clock = pygame.time.get_ticks()

width = 10
height = 800
damage = 1
enemy_hp = 10
scale = 0

#screen size

screen_height = 900
screen_width = 1750
main_area = True
shop_area = False
enemy_encounter = False

class Potato(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("project/img/potato" + str(random.randint(1, 4)) + "-removebg-preview.png")
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

potato_group = pygame.sprite.Group()
potato_sprite = Potato(int(150), 250)

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))
pygame.display.set_caption("Tomato Box")

bg = pygame.image.load("project/img/white.png")
bg = pygame.transform.scale(bg, (screen_height, screen_width))

#tomatoes

tomato_size = 20
tomato_font = pygame.font.SysFont("Times new roman", tomato_size)
def draw_tomato_text(text, font, text_col, x, y):
    ima = font.render(text, True, text_col)
    screen.blit(ima, (x,y))
font_size = 15
text_font = pygame.font.SysFont("Times new roman", font_size)
def draw_text(text, font, text_col, x, y):
    ima = font.render(text, True, text_col)
    screen.blit(ima, (x,y))

def draw_bg():
    screen.blit(bg, (0, 0))

color_dark = 200, 200, 200
color_light = 100, 100, 100

running = True
while running == True:
    clock.tick(fps)
    pygame.display.flip()
    draw_bg()
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if 10/2 <= mouse[0] <= 10/2+180 and 100/2 <= mouse[1] <= 100/2+40 and main_area == True: 
                tomatoes_consumed += tomatoes
                tomatoes = 0
                tomatoes_have_been_consumed = True

            if tomatoes >= 10 and tomatoes_consumed >= 10 and 10/2 <= mouse[0] <= 10/2+180 and 100/2 <= mouse[1] <= 280/2+40 and main_area == True: 
                tomatoes_tossed += 10
                tomatoes -= 10
                tomatoes_have_been_tossed = True

            if width/2 <= mouse[0] <= width/2+180 and height/2 <= mouse[1] <= height/2+40 and main_area == True and total_enemies >= 1:
                main_area = False
                shop_area = True

            elif width/2 <= mouse[0] <= width/2+180 and height/2 <= mouse[1] <= height/2+40 and shop_area == True:
                shop_area = False
                main_area = True
            
            elif width/2 <= mouse[0] <= width/2+180 and 500/2 <= mouse[1] <= 500/2+40 and shop_area == True and tomatoes >= d_up_cost:
                tomatoes -= d_up_cost
                damage += 1
                purchased_damage = True
                damage_up_tick += 1 
                d_up_cost += 5

            elif width/2 <= mouse[0] <= width/2+180 and 350/2 <= mouse[1] <= 350/2+40 and shop_area == True and tomatoes >= f_up_cost:
                tomatoes -= f_up_cost
                fertilizer_tick += 1
                purchased_fertilizer = True
                f_up_cost = int(20 * (fertilizer_tick + 1))

            if width/2 <= mouse[0] <= width/2+180 and 650/2 <= mouse[1] <= 650/2+40 and potato_carcas >= 1 and shop_area == True:
                tomatoes += tomatoes_exchange_total
                total_tomatoes += tomatoes_exchange_total
                tomatoes_exchange_total += 10
                potato_carcas -= 1

            elif width/2 <= mouse[0] <= width/2+300 and height/2 <= mouse[1] <= height/2+200 and enemy_encounter == True:
                enemy_hp -= damage

    tomato_increase = (1 * fertilizer_tick) + 1

    if 10/2 <= mouse[0] <= 10/2+180 and 100/2 <= mouse[1] <= 100/2+40 and main_area == True: 
        pygame.draw.rect(screen,color_light,[10/2,100/2,180,40]) 
        draw_text("Consume all the Tomatoes", text_font, (0, 0, 0), 10, 60)
          
    elif main_area == True: 
        pygame.draw.rect(screen,color_dark,[10/2,100/2,180,40]) 
        draw_text("Consume all the Tomatoes", text_font, (0, 0, 0), 10, 60)

    if tomatoes_have_been_consumed == True and main_area == True:
        draw_text("You've consumed " + str(tomatoes_consumed) + " tomatoes", text_font, (0, 0, 0), 10, 100)

#Tomato addition
    lasterest_tomato = pygame.time.get_ticks()
    if lasterest_tomato - last_tomato > tomato_cooldown and (main_area == True or enemy_encounter == True):
            tomatoes += tomato_increase
            total_tomatoes += tomato_increase
            last_tomato = lasterest_tomato
            if enemy_encounter != True and total_tomatoes >= 25:
                enemy_tick += 1

#tomato toss button 
    
    if tomatoes_consumed >= 10:

        if 10/2 <=mouse[0] <= 10/2+280 < mouse[1] <= 180/2+40 and main_area == True:
            pygame.draw.rect(screen,color_light,[10/2,280/2,180,40])
            draw_text("Toss 10 Upon Thy Floor", text_font, (0, 0, 0), 10, 150)

        elif main_area == True:
            pygame.draw.rect(screen,color_dark,[10/2,280/2,180,40])
            draw_text("Toss 10 Upon Thy Floor", text_font, (0, 0, 0), 10, 150)
    
    if tomatoes_have_been_tossed == True and main_area == True:
        draw_text("You've tossed " + str(tomatoes_tossed) + " tomatoes upon the floor", text_font, (0, 0, 0), 10, 200)

    if total_enemies >= 1:

        if width/2 <= mouse[0] <= width/2+180 and height/2 <= mouse[1] <= height/2+40 and main_area == True:
            pygame.draw.rect(screen,color_light,[width/2,height/2,180,40]) 
            draw_text("Shop", text_font, (0, 0, 0), 10, 410)
        
        elif main_area == True: 
            pygame.draw.rect(screen,color_dark,[width/2,height/2,180,40])
            draw_text("Shop", text_font, (0, 0, 0), 10, 410)

    if shop_area == True:
        if width/2 <= mouse[0] <= width/2+180 and height/2 <= mouse[1] <= height/2+40 and shop_area == True:
            pygame.draw.rect(screen,color_light,[width/2,height/2,180,40])
            draw_text("Main area", text_font, (0, 0, 0), 10, 410)
          
        elif shop_area == True: 
            pygame.draw.rect(screen,color_dark,[width/2,height/2,180,40])
            draw_text("Main area", text_font, (0, 0, 0), 10, 410)
            
        if width/2 <= mouse[0] <= width/2+180 and 500/2 <= mouse[1] <= 500/2+40 and shop_area == True:
            pygame.draw.rect(screen,color_light,[width/2,500/2,180,40])
            draw_text("Damage up                                   " + str(d_up_cost), text_font, (0, 0, 0), 10, 260)
          
        elif shop_area == True: 
            pygame.draw.rect(screen,color_dark,[width/2,500/2,180,40])
            draw_text("Damage up                                   " + str(d_up_cost), text_font, (0, 0, 0), 10, 260)

        if purchased_damage == True:
            draw_text("You've purchased " + str(damage_up_tick) + " damage up's", text_font, (0, 0, 0), 15, 290)

        if width/2 <= mouse[0] <= width/2+180 and 350/2 <= mouse[1] <= 350/2+40 and shop_area == True:
            pygame.draw.rect(screen,color_light,[width/2,350/2,180,40])
            draw_text("Fertilizer                                   " + str(f_up_cost), text_font, (0, 0, 0), 10, 170)
          
        elif shop_area == True: 
            pygame.draw.rect(screen,color_dark,[width/2,350/2,180,40])
            draw_text("Fertilizer                                   " + str(f_up_cost), text_font, (0, 0, 0), 10, 180)

        if purchased_fertilizer == True:
            draw_text("You've consumed " + str(fertilizer_tick) + " bags of Fertilizer", text_font, (0, 0, 0), 15, 200)


        if width/2 <= mouse[0] <= width/2+180 and 650/2 <= mouse[1] <= 650/2+40 and shop_area == True:
            pygame.draw.rect(screen,color_light,[width/2,650/2,180,40])
            draw_text("Exchange Potato Carcas", text_font, (0, 0, 0), 10, 330)
            draw_text("You have " + str(potato_carcas), text_font, (0, 0, 0), 15, 350)
        
        elif shop_area == True: 
            pygame.draw.rect(screen,color_dark,[width/2,650/2,180,40])
            draw_text("Exchange Potato Carcas", text_font, (0, 0, 0), 10, 330)
            draw_text("You have " + str(potato_carcas), text_font, (0, 0, 0), 15, 350)

    if total_tomatoes >= 25:
        enemy_chance = True

    if enemy_chance == True:
        if enemy_cooldown == enemy_tick:
            main_area = False
            enemy_encounter = True
            shop_area = False
            total_enemies += 1
            enemy_tick = 0
            enemy_cooldown = random.randint(1, 20)
            enemy_hp = random.randint(1 + scale, 5 + scale)
            potato_group.add(potato_sprite)
            enemy_timer = ((tomatoes_tossed) / ((enemies_defeated+1) * 3)) + 1

    if enemy_encounter == True:
        if width/2 <= mouse[0] <= width/2+300 and height/2 <= mouse[1] <= height/2+200 and enemy_encounter == True:
            pygame.draw.rect(screen,color_light,[width/2,height/2,300,200])
            draw_text("Hit", text_font, (0, 0, 0), 200, 500)
          
        elif enemy_encounter == True: 
            pygame.draw.rect(screen,color_dark,[width/2,height/2,300,200])
            draw_text("Hit", text_font, (0, 0, 0), 200, 500)

        lasterest_enemy_clock_move = pygame.time.get_ticks()
        if lasterest_enemy_clock_move - lasterest_enemy_clock > lasterest_enemy_cooldown:
            enemy_timer -= .1
            lasterest_enemy_clock = lasterest_enemy_clock_move

        potato_group.draw(screen)
        potato_group.update()
        draw_text("Enemy hp: " + str(enemy_hp), text_font, (0, 0, 0), 10, 100)
        draw_text("Time Remaining: " + str(float(enemy_timer)), text_font, (0, 0, 0), 10, 120)

        if enemy_timer <= 0:
            enemy_encounter = False
            
            main_area = True

        if enemy_hp <= 0:
            enemy_encounter = False
            potato_carcas += 1
            scale += random.randint(5, int(enemies_defeated+3)*int(total_enemies+2))
            main_area = True

    elif enemy_encounter == False:
        pass
             
#updating
    draw_tomato_text("Tomatoes: " + str(int(tomatoes)), tomato_font, (0, 0, 0), 10, 10)
    if enemies_defeated >= 1:
        draw_text("Defeated Enemies: " + str(enemies_defeated), tomato_font, (0, 0, 0), 100, 10)