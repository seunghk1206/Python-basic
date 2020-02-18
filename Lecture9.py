import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 1
        if 50 < x < 66:
            if pressed[pygame.K_UP]:
                y -= 1
        elif x < 21 or y < 21:
            x = 350
            y = 250
    if pressed[pygame.K_DOWN]: 
        y += 1
        if 50 < x < 66:
            if pressed[pygame.K_UP]:
                y -= 1
        elif x < 21 or y < 21:
            x = 350
            y = 250
    if pressed[pygame.K_LEFT]: 
        x -= 1
        if 50 < x < 66:
            if pressed[pygame.K_UP]:
                y -= 1
        elif x < 21 or y < 21:
            x = 350
            y = 250
    if pressed[pygame.K_RIGHT]: 
        x += 1
        if 50 < x < 66:
            if pressed[pygame.K_UP]:
                y -= 1
        elif x < 21 or y < 21:
            x = 350
            y = 250
    screen.fill((0, 0, 0))
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 6, 6))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, 20, 10000, 1))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, 20, 1, 10000))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 20, 16, 2))
    pygame.display.flip()
    clock.tick(60)