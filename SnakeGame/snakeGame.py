import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.15)
musica_fundo = pygame.mixer.music.load('musica/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

musica_score = pygame.mixer.Sound('musica/smw_coin.wav')
musica_score.set_volume(1)

x_controle = 10
y_controle = 0
velocidade = 10

largura = 640
altura = 480
x_snake = int(largura/2)
y_snake = int(altura/2)

x_food = randint(40, 600)
y_food = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

background = (255, 255, 255)
cor_food = (255, 0, 0)
cor_snake = (0, 255, 0)
cor_texto = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake - O Jogo')
relogio = pygame.time.Clock()
lista_snake = []
comprimento_inicial = 5
dead = False

def corpo_snake(lista_snake):
    for XeY in lista_snake:
        pygame.draw.rect(tela, cor_snake, (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_snake, y_snake, lista_snake, snake_head, x_food, y_food, dead
    pontos = 0
    comprimento_inicial = 5
    x_snake = int(largura / 2)
    y_snake = int(altura / 2)
    lista_snake = []
    snake_head = []
    x_food = randint(40, 600)
    y_food = randint(50, 430)
    dead = False

while True:
    relogio.tick(30)
    tela.fill((background))
    mensagem = f'Score: {pontos}'
    texto_format = fonte.render(mensagem, True, cor_texto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if (pygame.key.get_pressed()[K_w]) or (pygame.key.get_pressed()[K_UP]):
        if y_controle == velocidade:
            pass
        else:
            y_controle = -velocidade
            x_controle = 0
    if (pygame.key.get_pressed()[K_a]) or (pygame.key.get_pressed()[K_LEFT]):
        if x_controle == velocidade:
            pass
        else:
            x_controle = -velocidade
            y_controle = 0
    if (pygame.key.get_pressed()[K_s]) or (pygame.key.get_pressed()[K_DOWN]):
        if y_controle == -velocidade:
            pass
        else:
            y_controle = velocidade
            x_controle = 0

    if (pygame.key.get_pressed()[K_d]) or (pygame.key.get_pressed()[K_RIGHT]):
        if x_controle == -velocidade:
            pass
        else:
            x_controle = velocidade
            y_controle = 0

    x_snake = x_snake + x_controle
    y_snake = y_snake + y_controle

    snake = pygame.draw.rect(tela, cor_snake, (x_snake, y_snake, 20, 20))
    food = pygame.draw.rect(tela, cor_food, (x_food, y_food, 10, 10))

    if snake.colliderect(food):
        x_food = randint(40, 600)
        y_food = randint(50, 430)
        pontos = pontos + 1
        musica_score.play()
        comprimento_inicial = comprimento_inicial + 1

    snake_head = []
    snake_head.append(x_snake)
    snake_head.append(y_snake)

    lista_snake.append(snake_head)

    if lista_snake.count(snake_head) > 1:
        fonte_game_over = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'GAME OVER!! Pressione ESPAÇO para jogar novamente!!'
        texto_format = fonte_game_over.render(mensagem, True, cor_texto)
        ret_texto = texto_format.get_rect()

        dead = True
        while dead:
            tela.fill(background)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if pygame.key.get_pressed()[K_SPACE]:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_format, ret_texto)
            pygame.display.update()

    if x_snake > largura:
        x_snake = 0
    if x_snake < 0:
        x_snake = largura
    if y_snake < 0:
        y_snake = altura
    if y_snake > altura:
        y_snake = 0


    if len(lista_snake) > comprimento_inicial:
        del lista_snake[0]

    corpo_snake(lista_snake)

    tela.blit(texto_format, (450, 40))
    pygame.display.update()