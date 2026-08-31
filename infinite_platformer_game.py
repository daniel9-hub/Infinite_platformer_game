import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
game_running = False
pause = False
font = pygame.font.Font(None, size=40)
text_normal = font.render("NORMAL MODE",True,(255,255,255))
text_infinite = font.render("INFINITE MODE",True,(255,255,255))
normal_position = 535
infinite_position = 900
endless = False
main_menu = True
menu_move_left = False
menu_move_right = False
portal_x = random.randint(-2500, 2500)
portal_y = random.randint(200, 300)
original_portal_x = portal_x
original_portal_y = portal_y 

level = 1
endscreen = False

worlds = []
water = pygame.image.load("water.png")
for i in range(5):
    world = random.randint(1,1)
    worlds.append(world)
print(worlds)
worlds_index = 0
while running:
    while endscreen:
        screen.fill((0,0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                running = False
                endscreen = False
            
    died = False
    vh = 5
    vg = 0
    x = 80
    y = 100
    jump = False
    jumpc = 20
    jumpcc = 0
    lightning_x = 0
    lightning_y = 0
    lightning_strike = False
    lightning_time = 0
    lightning_blit = True
    
    px = 20
    py = 630
    
    shake_direction = 0
    shake_force_x = 0
    shake_force_y = 0
    shake = True
    
    yv = 0

    score = 2

    touching_ground = False

    player = pygame.image.load("player.png")
    player_left = pygame.transform.flip(player,True,False)
    player_final = player
    start_button = font.render("""Press "SPACE" to play""",True,(255,255,255))
    start_button_rect = start_button.get_rect()
    
    portal = pygame.image.load("portal.png")
    portal_rect = portal.get_rect()
    teleport = False
    
    lightning_warning = pygame.image.load("lightning_warning.png")
    lightning = pygame.image.load("lightning.png")
    lightning_rect = lightning.get_rect()
    background1 = pygame.image.load("background1.jpg")
    lightning_warning_y = 640
                                                # ENEMY SETUP
    enemy = pygame.image.load("enemy.png")
    enemy_rect = enemy.get_rect()
    ex = 900
    ey = 100
    enemy_rect.x = -300
    enemy_rect.y = -500
    enemy_jump = False
    eyv = 0
    enemy_touching_ground = False
    enemy_jumpc = 24
    enemy_jumped = False
    enemy_direction = -5
    background2 = pygame.image.load("background2.jpg")
    
    rush = pygame.image.load("rush.png  ")
    rx = 1280
    ry = 530
    rush_chance = 0
    rush_going = False
    rush_direction = -20
    rush_rect = rush.get_rect()
    rush_warning = False
    rush_warning_time = 0
    rush_went = False
    rush_ready = pygame.image.load("player.png")
    rrx = 1280
    rry = 530
    rush_ready_counter = 0
    rush_side = random.randint(0,1)
    background3 = pygame.image.load("background3.jpg")
    
    fx = 680
    fy = 420
    class Floater(pygame.sprite.Sprite):
        def __init__(self,fx,fy,):
            super().__init__()
            self.images = [pygame.image.load("floater1.png"),pygame.image.load("floater2.png"),pygame.image.load("floater3.png"),pygame.image.load("floater4.png")]
            self.image = random.choice(self.images)
            self.dfx = random.randint(0,1)
            self.dfy = random.randint(0,1)
            self.rect = self.image.get_rect()
    floater_counter = 0
    floater_visible = False
    floater_invisible_counter = 0
    floater_invisible_time = random.randint(80,180)
    floater_flash_counter = 0
    floater_collision = False
    background4 = pygame.image.load("background4.jpg")
    
    floaters = []
    
    for i in range(random.randint(3,3)):
        floaters.append(Floater(fx,fy))
    for floater in floaters:
        floater.rect.x = random.randint(0,1280)
        floater.rect.y = random.randint(0,720)
    
    direction_right = pygame.image.load("direction.jpg")
    direction_left = pygame.image.load("direction2.jpg")
    
    class Platform(pygame.sprite.Sprite):
        def __init__(self, px, py,):
            super().__init__()
            self.image = pygame.image.load("platform.png")
            self.rect = self.image.get_rect()
            self.rect.topleft = (px, py)
            self.speed = 0
            if random.random() < 0.3:
                self.speed = random.choice([-3, 3])
            self.start_x = px
        
        def update(self):
            self.rect.x += self.speed
            
            if self.rect.x > self.start_x + 50:
                self.speed = -abs(self.speed)
            
            if self.rect.x < self.start_x -50:
                self.speed = abs(self.speed)
        
        def draw(self, screen):
            screen.blit(self.image, self.rect)
            
            
        
    
    
    prect = player.get_rect()
    prect.topleft = (x, y)
    yd = prect.bottom
    x = (640 - (prect.x / 2))
    y = 100


    platforms = []

    for a in range(5):
        platforms.append(Platform(px, py))
        px += 550
        py = random.randint(500, 690)

                                                                # GAME RUNNING
    while game_running:
        died = False
        
        prect = player.get_rect()
        prect.topleft = (x, y)
        yd = prect.bottom
        portal_rect.x = portal_x
        portal_rect.y = portal_y
        
        main_menu = False
        touching_ground = False
        
        if portal_x > x:
            direction = direction_right
        elif portal_x < x:
            direction = direction_left
        
                                                        # PLAYER PLATFORM COLLISION
        for platform in platforms:
            if prect.colliderect(platform.rect):
                y = (platform.rect.y - prect.height) + 1
                touching_ground = True
        
        for platform in platforms: 
            if (platform.rect.left <= prect.centerx <= platform.rect.right):
                    if (y + prect.height) == platform.rect.y:
                        touching_ground = True
        
        if touching_ground == True:
            yv = 0
        
        if worlds[worlds_index] == 0:
            for platform in platforms:
                platform.image = pygame.image.load("platform.png")
            portal = pygame.image.load("portal - Copy.png")
        elif worlds[worlds_index] == 1:
            for platform in platforms:
                platform.image = pygame.image.load("platform1.jpg")
            portal = pygame.image.load("portal1.png")
        elif worlds[worlds_index] == 2:
            for platform in platforms:
                platform.image = pygame.image.load("platform2.jpg")
        elif worlds[worlds_index] == 3:
            for platform in platforms:
                platform.image = pygame.image.load("platform3.jpg")
        elif worlds[worlds_index] == 4:
            for platform in platforms:
                platform.image = pygame.image.load("platform4.png")
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if pause == True:
                        pause = False
                        game_running = False
                        main_menu = True
                    if pause == False:
                        pause = True
                if event.key == pygame.K_SPACE:
                    pause = False
                    
        if pause == True:
            screen.fill((0,0,0))
            screen.blit(start_button,(490,320))
            pygame.display.flip()
            continue
                                                    # MOVEMENT
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if x < 320:
                for platform in platforms:
                    platform.rect.x += 7
                for platform in platforms:
                    if platform.rect.x < 320:
                        platform.start_x += 7
                    else:
                        platform.start_x += 5
                lightning_x += 7
                lightning_rect.x += 7
                portal_x +=7
                ex += 7
            else:
                x -= 7
            player_final = player_left
            
            
        if keys[pygame.K_d]:
            if x > (980 - prect.width):
                for platform in platforms:
                    platform.rect.x -= 7
                    
                for platform in platforms:
                    if platform.rect.x > 980 -  platform.rect.width:
                        platform.start_x -= 7
                    else:
                        platform.start_x -= 5
                lightning_x -= 7
                lightning_rect.x -= 7
                portal_x -=7
                ex -= 7
            else:
                x += 7
            player_final = player
            
        if keys[pygame.K_SPACE] and touching_ground and not worlds[worlds_index] == 4:
            jump = True
            touching_ground = False
        elif keys[pygame.K_SPACE] and worlds[worlds_index] == 4:
            up = True
        else:
            up = False
            
                                                                                    # PLATFORM RESPAWN
        for platform in platforms[:]:
            if platform.rect.right < 0:
                py = random.randint(500, 680)
                newx = max(platform.rect.left for platform in platforms) + 600
                
                platforms.remove(platform)
                
                platforms.append(
                Platform(newx, py)
            )   
                score += 1
        
        for platform in platforms[:]:
            if platform.rect.left > 1280:
                py = random.randint(500, 710)
                newx = min(platform.rect.left for platform in platforms) - 600
                
                platforms.remove(platform)
                
                
                platforms.append(
                Platform(newx, py)
            )   
                score -= 1
        
        if worlds[worlds_index] == 0:
            background = pygame.image.load("background0.png")
        
                                                                        # JUMP
        if not worlds[worlds_index] == 4:
            g = 1
            if jump == True:
                    if jumpc > 0:
                            y -= jumpc
                            jumpc -= 1
                    else:
                        jumpc = 20
                        jump = False
                    
        if worlds[worlds_index] == 4:
            g = 0.1
            if up == True:
                yv -= 0.3
        
        if jump == False and touching_ground == False:
            y += yv
            yv += g
            
                                                        # SHAKE
        if 5000 < abs(portal_x) < 25000:
            shake = False
        elif 3000 < abs(portal_x) < 5000:
            shake_force_x = 1
            shake_force_y = 1
            shake = True
        elif 1500 < abs(portal_x) < 3000:
            shake_force_x = 3
            shake_force_y = 3
            shake = True
        elif 1000 < abs(x - portal_x) < 1500:
            shake_force_x = 6
            shake_force_y = 6
            shake = True
        elif 600 < abs(x - portal_rect.centerx) < 1000:
            shake_force_x = 12
            shake_force_y = 12
            shake = True
        elif abs(x - portal_rect.centerx) < 600:
            shake_force_x = 20
            shake_force_y = 20
            shake = True
        
                                    # ENEMY
        if worlds[worlds_index] == 2:
            enemy_rect.x = ex
            enemy_rect.y = ey
            background = background2
        if touching_ground == True and enemy_touching_ground == True:
            if worlds[worlds_index] == 2:
                if ex >= x:
                    enemy_direction = -7
                elif ex <= x:
                    enemy_direction = 7
        
        if worlds[worlds_index] == 2:
            ex += enemy_direction
        if enemy_jumpc == 24:
            ey += eyv
            eyv += 1
            
        enemy_touching_ground = False
        #print((ex + (enemy_rect.width / 2)) - (x + (prect.width / 2)))
        for platform in platforms:
            if enemy_rect.colliderect(platform.rect):
                ey = (platform.rect.y - enemy_rect.height + 1)
                eyv = 0
                enemy_touching_ground = True
                enemy_jumpc = 24
                enemy_jumped = False
            
        if enemy_touching_ground == False and enemy_jumped == False:
            enemy_jump = True
            if enemy_jumpc > 0:
                ey -= enemy_jumpc
                enemy_jumpc -=1
            if enemy_jumpc == 0:
                enemy_jumpc = 24
                enemy_jump = False
                enemy_jumped = True
        
        if ey > 720:
            if ex < x:
                ex = (1280 - enemy_rect.width)
                ey = 0
            else:
                ex = 0
                ey = 0
            
                                        # RUSH
        if worlds[worlds_index] == 3:
            background = background3
            portal = pygame.image.load("portal - Copy.png")
            portal = pygame.image.load("portal3.jpg")
            if rush_going == False:
                rush_chance = random.randint(1,200)
                if rush_chance == 1:
                    rush_going = True
            if rush_going == True:
                if rush_ready_counter < 80:
                    rush_ready_counter += 1
                    shake_force_x = 6
                    shake = True
                    if rush_side == 0:
                        rrx = 1200
                        rx = 1280
                    else:
                        rrx = 0
                        rx = (0 - rush_rect.width)
                elif rush_ready_counter == 80:
                    rrx = 1280
                    if rush_side == 0:
                        if rx >= 1280:
                            if rush_went == True:
                                rush_going = False
                                rush_went = False
                                rush_direction = 0
                                rush_ready_counter = 0
                                shake_force_x = 0
                                rush_side = random.randint(0,1)
                                
                            else:
                                rush_direction = -20

                                
                        elif rx <= 0 - (rush_rect.width):
                            rush_direction = 20
                            rush_went = True
                    elif rush_side == 1:
                        if rx <= 0 - (rush_rect.width):
                            if rush_went == True:
                                rush_going == False
                                rush_went = False
                                rush_direction = 0
                                rush_ready_counter = 0
                                shake_force_x = 0
                                rush_side = random.randint(0,1)
                            
                            else:
                                rush_direction = 20
                                
                        elif rx >= 1280:
                            rush_direction = -20
                            rush_went = True
                        
                    rx += rush_direction
                    shake_force_x = 10
                    shake = True
                
                
            rush_rect.x = rx
            rush_rect.y = ry
            
            if prect.colliderect(rush_rect):
                died = True
                game_running = False
                
                                        # FLOATER
        if worlds[worlds_index] == 4:
            floater_counter += 1
            background = background4
            portal = pygame.image.load("portal4.png")
            if y < -200:
                died = True
                game_running = False
            for floater in floaters:
            
                if floater_visible == True:
                    floater.rect.x += floater.dfx
                    floater.rect.y += floater.dfy
                    
                    
                    if floater_counter >= 300:
                        floater.dfx = random.randint(-3,3)
                        floater.dfy = random.randint(-3,3)
                        floater_counter = 0
                        floater_visible = False
                        for floater in floaters:
                            floater.rect.x = random.randint(0,1280)
                            floater.rect.y = random.randint(0,720)
                        
                        
                        while prect.colliderect(floater.rect):
                            floater.rect.x = random.randint(0,1280)
                            floater.rect.y = random.randint(0,720)
                            
                elif floater_visible == False:
                    if floater_invisible_counter < floater_invisible_time:
                        floater_invisible_counter += 1
                    elif floater_invisible_counter == floater_invisible_time:
                        floater_invisible_counter = 0
                        floater_visible = True
                        floater_invisible_time = random.randint(80,180)
                        for floater in floaters:
                            floater.images = [pygame.image.load("floater1.png"),pygame.image.load("floater2.png"),pygame.image.load("floater3.png"),pygame.image.load("floater4.png")]
                            floater.image = random.choice(floater.images)
        if random.randint(0,1000) == 0:
            floaters.append(Floater(random.randint(0,1280),random.randint(0,720)))
        #print(floater_invisible_time)
        #print(floater_invisible_counter)
        if y > 720:
            
            died = True
            game_running = False
        #print(ey)
        #print(y)
        #print(enemy_jumpc)
        #print(enemy_touching_ground)
        
        
        if prect.colliderect(enemy_rect):
            died = True
            game_running = False
            print("died")
                                                            # LIGHTNING
        if worlds[worlds_index] == 1:
            background = background1
            if lightning_strike == False:
                lightning_chance = random.randint(1, 20)
                if lightning_chance == 1:
                    lightning_strike = True
                    
                    lightning_x = random.randint(0, 1280)
                    for platform in platforms:
                        if platform.rect.x < lightning_x < (platform.rect.x + platform.rect.width):
                            lightning_y = (platform.rect.y - 800)
                            lightning_warning_y = (lightning_y + 720)
                            break
                        else: 
                            lightning_y = 0 
                            lightning_warning_y = 640
                    lightning_rect.x = lightning_x
                    lightning_rect.y = lightning_y
            print(lightning_warning_y)
                                                        # TELEPORT
        if prect.colliderect(portal_rect):
            teleport = True
        
        if teleport == True:
            #world = random.randint(1,2)
            game_running = False
            #print("teleported")
            if endless == True:
                worlds.clear()
                worlds.append(random.randint(0,4))
        
                                                        # END
        for platform in platforms:
            platform.update()
        
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        
                                                                                                    # LIGHTNING 2
        if worlds[worlds_index] == 1:
            if lightning_strike == True:
                if lightning_blit == True:              # START
                    screen.blit(lightning_warning, (lightning_x, lightning_warning_y))
                    lightning_time += 1
                if 45 > lightning_time >= 30:           # OFF
                    lightning_time += 1
                    lightning_blit = False
                    screen.blit(lightning, (-100, 800))
                if 55 > lightning_time >= 45:           # STRIKE
                    screen.blit(lightning, (lightning_x, lightning_y))
                    lightning_time += 1
                    shake_force_y = 30
                    shake = True
                    if prect.colliderect(lightning_rect):
                        died = True
                        game_running = False
                        #print("collision")
                        
                if lightning_time == 55:
                    screen.blit(lightning, (-100, 800))
                    lightning_strike = False
                    lightning_time = 0
                    lightning_blit = True
        #print(shake_force_x, shake)
        if shake == True:
            shake_x = random.randint(-shake_force_x, shake_force_x)
            shake_y = random.randint(-shake_force_y, shake_force_y)
        else:
            shake_x = 0
            shake_y = 0
        
        x += (shake_x / 2)
        y += (shake_y / 2)
        
        for platform in platforms:
            screen.blit(platform.image, (platform.rect.x + shake_x, platform.rect.y + shake_y))
        
        
        #print(lightning_time)
        #print(lightning_strike)
        
        screen.blit(player_final, (x, y))
        screen.blit(portal, (portal_x, portal_y))
        if worlds[worlds_index] == 2:
            screen.blit(enemy, (ex, ey))
        if worlds[worlds_index] == 3:
            screen.blit(rush, (rx, ry))
            screen.blit(rush_ready, (rrx, rry))
        if worlds[worlds_index] == 4 and floater_visible == True:
            for floater in floaters:
                screen.blit(floater.image, floater.rect)
                if prect.colliderect(floater.rect) or floater_collision == True:
                    if floater_flash_counter < 60:
                        screen.fill((255,255,255))
                        floater_flash_counter += 1
                        floater_collision = True
                    else:
                        floater_flash_counter = 0
                        floater_collision = False
        screen.blit(direction,(540,200))
        if worlds[worlds_index] == 4:
            screen.blit(water,(0,0))
        #print(portal_x)
        clock.tick(60)
        pygame.display.flip()
    
    portal_x = original_portal_x
    portal_y = original_portal_y
    
    screen.fill((0,0,0))
    if died == True:
        #print("died")
        game_running = True
        #worlds_index = 0
    if died == False:
        game_running = False
    if teleport == True:
        game_running = True
        level += 1
        if level == 6 and endless == False:
            endscreen = True
        portal_x = random.randint(-2500, 2500)
        portal_y = random.randint(200, 300)
        if endless == False:
            worlds_index += 1
        teleport = False
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                running = False
                game_running = False
                                                # MODE SELECT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = True
                if event.key == pygame.K_a and endless == False:
                    menu_move_left = True
                elif event.key == pygame.K_d and endless == True:
                    menu_move_right = True
    if menu_move_left == True:                    # MENU MOVE LEFT
        if infinite_position > 550 and menu_move_left == True:
            while infinite_position > 550:
                normal_position -=7
                infinite_position -=7
                clock.tick(60000)
                screen.blit(text_normal,(normal_position,500))
                screen.blit(text_infinite,(infinite_position,500))
                screen.blit(start_button,(500,320))
                pygame.display.flip()
                screen.fill((0,0,0))
        elif infinite_position == 550:
            endless = True
            menu_move_left = False
    if menu_move_right == True:                    # MENU MOVE RIGHT
        if normal_position < 535 and menu_move_right == True:
            while normal_position < 535:
                normal_position +=7
                infinite_position +=7
                clock.tick(60000)
                screen.blit(text_normal,(normal_position,500))
                screen.blit(text_infinite,(infinite_position,500))
                screen.blit(start_button,(500,320))
                pygame.display.flip()
                screen.fill((0,0,0))
        elif normal_position == 535:
            endless = False
            menu_move_right = False
    if main_menu:
        screen.blit(start_button, (500, 320))
        screen.blit(text_normal, (normal_position,500))
        screen.blit(text_infinite, (infinite_position,500))
    print(endless)
    pygame.display.flip()
    
    #print(1280 - start_button_rect.width)
    #print(720 - start_button_rect.height)
    
pygame.quit()