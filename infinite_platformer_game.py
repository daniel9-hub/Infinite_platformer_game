import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
game_running = False

portal_x = random.randint(-25000, 25000)
portal_y = random.randint(200, 500)
original_portal_x = portal_x
original_portal_y = portal_y

while running:
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

    start_button = pygame.image.load("platform.png")
    start_button_rect = start_button.get_rect()
    
    portal = pygame.image.load("portal.png")
    portal_rect = portal.get_rect()
    
    lightning = pygame.image.load("lightning.png")
    lightning_rect = lightning.get_rect()
    
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
        
        
        
        touching_ground = False
        
        
        
        
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
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                    
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
            else:
                x -= 7
            
            
            
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
            else:
                x += 7
            
            
        if keys[pygame.K_SPACE] and touching_ground:
            jump = True
            touching_ground = False
            
                                                                                    # PLATFORM RESPAWN
        for platform in platforms[:]:
            if platform.rect.right < 0:
                py = random.randint(500, 680)
                newx = max(platform.rect.left for platform in platforms) + 550
                
                platforms.remove(platform)
                
                platforms.append(
                Platform(newx, py)
            )   
                score += 1
        
        for platform in platforms[:]:
            if platform.rect.left > 1280:
                py = random.randint(500, 710)
                newx = min(platform.rect.left for platform in platforms) - 550
                
                platforms.remove(platform)
                
                platforms.append(
                Platform(newx, py)
            )   
                score -= 1
        
        
        
        
                                                                        # JUMP
        
        if jump == True:
                if jumpc > 0:
                        y -= jumpc
                        jumpc -= 1
                else:
                    jumpc = 20
                    jump = False
                    
        
        
        if jump == False and touching_ground == False:
            y += yv
            yv += 1
            
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
        
        
        
            
        if y > 720:
            died = True
            game_running = False
        
        
                                                            # LIGHTNING
        if lightning_strike == False:
            lightning_chance = random.randint(1, 20)
            if lightning_chance == 1:
                lightning_strike = True
                
                lightning_x = random.randint(0, 1280)
                for platform in platforms:
                    if platform.rect.x < lightning_x < (platform.rect.x - platform.rect.width):
                        lightning_y = (platform.rect.y - 800)
                    else:
                        lightning_y = 0
                lightning_rect.x = lightning_x
                lightning_rect.y = lightning_y
                
                
        
        
        
                                                        # END
        for platform in platforms:
            platform.update()
        
        screen.fill((0,0,0))
        
        
                                                                                                    # LIGHTNING 2
        if lightning_strike == True:
            if lightning_blit == True:              # START
                screen.blit(lightning, (lightning_x, lightning_y))
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
                    print("collision")
                    
            if lightning_time == 55:
                screen.blit(lightning, (-100, 800))
                lightning_strike = False
                lightning_time = 0
                lightning_blit = True
        
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
        
        
        print(lightning_time)
        print(lightning_strike)
        
        screen.blit(player, (x, y))
        screen.blit(portal, (portal_x, portal_y))
        
        
        clock.tick(60)
        pygame.display.flip()
    
    portal_x = original_portal_x
    portal_y = original_portal_y
    
    screen.fill((0,0,0))
    if died == True:
        print("died")
        game_running = True
    if died == False:
        game_running = False
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                running = False
                game_running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = True
                
    
    screen.blit(start_button, (490, 320))
    
    
    pygame.display.flip()
    
    print(1280 - start_button_rect.width)
    print(720 - start_button_rect.height)
    
pygame.quit()