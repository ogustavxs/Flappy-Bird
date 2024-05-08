import pygame
import random

pygame.init()
running = True
tela = pygame.display.set_mode((400, 500))

pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
gravidade = 0.3
aceleração = 0
força_pulo = -5  
bird_y = 130

espaço_obstaculos = 85
tubo_y = random.randint(-280, 0)

tubo = pygame.image.load("imagens/cano-verde.png").convert_alpha()
tubo_cima = pygame.transform.rotate(tubo, 180)
flappyimg = pygame.image.load("imagens/flappyimg.png").convert_alpha()
flappyimg = pygame.transform.scale(flappyimg, (68, 68))  
flappy_rect = flappyimg.get_rect()

plano_de_fundo = pygame.image.load("imagens/background.png").convert()
plano_de_fundo = pygame.transform.scale(plano_de_fundo, (400, 600)) 
tubo_x = 400
tubo_velocidade = 3
base = pygame.image.load("imagens/base.png").convert()
base = pygame.transform.scale(base, (400, 60))  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aceleração = força_pulo  

    tela.fill((255, 255, 255))
    flappy_rect.center = (200, bird_y)  
    

    tela.blit(plano_de_fundo, (0, 0))  
    tela.blit(flappyimg, flappy_rect)
    tela.blit(tubo_cima, (tubo_x, tubo_y))
    tela.blit(tubo, (tubo_x, tubo_y+espaço_obstaculos+360 ))
    tela.blit(base, (0, 480))  
   
    aceleração += gravidade
    tubo_x -= tubo_velocidade
    if tubo_x <= -55:
        tubo_x = 400
        tubo_y = random.randint(-280, 0)

    
    bird_y += aceleração

    if bird_y >= 465 or bird_y <= 11: 
        running = False
    
    tubo_superior_rect = pygame.Rect(tubo_x, tubo_y, tubo.get_width()-27, tubo.get_height()-15)
    tubo_inferior_rect = pygame.Rect(tubo_x, (tubo_y + espaço_obstaculos + 360)+13, tubo.get_width()-15, tubo.get_height())

    if flappy_rect.colliderect(tubo_superior_rect) or flappy_rect.colliderect(tubo_inferior_rect):
        running = False

    pygame.display.flip()
    clock.tick(60)
