import pygame
import moduleexample as module
import random as r

display = module.make_display(1080, 720, "_internal/Assets/background.jpeg", "UFO game")
fps = pygame.time.Clock()
land = pygame.sprite.Group()
lands = []
x1 = 0
for i in range(100):
    lands.append(module.GameObject("_internal/Assets/Snowgrass.png", x1, 650, 40, 40))
    x1 += 40
for i in lands:
    land.add(i)

player = module.GameObject("_internal/Assets/UFO149.png", 0, 0, 40, 40)
player.rect.y = 610  # Initial position of the player
player_speed_y = 0  # Vertical speed of the player
gravity = 1  # Gravity value

obs1 = module.GameObject("_internal/Assets/ball.png", 1080, r.randint(0, 720), 50, 50)
obs_1speed = 10

obs2 = module.GameObject("_internal/Assets/Sawblade.png", 1080, r.randint(0, 720), 50, 50)
obs_2speed = 15

txt = module.TextArea(0, 0, 50, 50, (255, 255, 255))
score = txt.set_text("SCORE: ", 40, (255, 0, 0))
display.add_sprite(score, txt.rect)

txt1 = module.TextArea(180, 0, 50, 50,(255, 255, 255))
value = txt1.set_text('0', 40, (255, 0, 0))
display.add_sprite(value, txt1.rect)


point = 0
screen = 'menu'


#make music in pg

pygame.mixer.init()
pygame.mixer.music.load("_internal/Assets/song.ogg")
pygame.mixer.music.play(-1)

while True: 
    x = 0
    y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
    if screen == "menu":
        point = 0
        #display.add_sprite(button_start, 1080/2, 180)
        display.update_background()
        name = module.TextArea(175, 200, 500, 200, (255, 255, 255))
        name_txt = name.set_text("GAME", 100, (255, 0, 0))
        display.add_sprite(name_txt, name.rect)
        button = display.create_rect(487, 140, 280, 70, (0, 255, 0))
        button_txt = module.TextArea(487, 140, 50, 50, (255, 255, 255))
        button_start = button_txt.set_text('Play Game', 50, (255, 255, 255))
        display.add_sprite(button_start, button_txt.rect)
        if button.collidepoint(x,y):
            screen = 'game'
            obs1.rect.x = 1080
            obs2.rect.x = 1080
            player.rect.y = 512
    elif screen == "game":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_speed_y = -10  # Jump
        player_speed_y += gravity  # Apply gravity
        player.rect.y += player_speed_y  # Update player's vertical position
        obs1.rect.x -= obs_1speed
        obs2.rect.x -= obs_2speed
        # Check collision with platforms
        collisions = pygame.sprite.spritecollide(player, land, False)
        for collision in collisions:
            if player_speed_y > 0:  # Player is falling
                player.rect.bottom = collision.rect.top  # Stop falling
        if player.rect.y < 0:
            player.rect.y = 0
        if player.rect.y > 720:
            screen = 'game over'
        if obs1.rect.x < 0:
            obs1.rect.x = 1080
            obs1.rect.y = r.randint(0, 720)
            point += 1
            value = txt1.set_text(str(point), 40, (255, 0, 0))
        if obs2.rect.x < 0:
            obs2.rect.x = 1080
            obs2.rect.y = r.randint(0, 720)
            point += 1 
            value = txt1.set_text(str(point), 40, (255, 0, 0))

        if player.check_collide(obs1):
            print("Collide with obs one")
            screen = 'game over'
        
        if player.check_collide(obs2):
            print("Collide with obs two")
            screen = 'game over'
        
        if x != 0 and y != 0:
            player_speed_y = -15


        # land.draw(display.my_display())
        display.update_background()
        display.add_sprite(score, txt.rect)
        display.add_sprite(value, txt1.rect)
        display.add_sprite(obs1.image, obs1.rect)
        display.add_sprite(obs2.image, obs2.rect)
        display.add_sprite(player.image, player.rect)

    if screen == "game over":
        #display.add_sprite(button_start, 1080/2, 180)
        display.update_background()
        name = module.TextArea(175, 200, 500, 200, (255, 255, 255))
        name_txt = name.set_text("GAME OVER \n score" + str(point), 50, (255, 0, 0))
        display.add_sprite(name_txt, name.rect)
        button = display.create_rect(487, 140, 280, 70, (0, 255, 0))
        button_txt = module.TextArea(487, 140, 50, 50, (255, 255, 255))
        button_start = button_txt.set_text('Play Game', 50, (255, 255, 255))
        display.add_sprite(button_start, button_txt.rect)
        if button.collidepoint(x,y):
            screen = 'menu'
    display.update_frame()
    fps.tick(60)