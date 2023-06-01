import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
COR_COBRA = (255, 255, 255)
COR_COMIDA = (252, 0, 0)

# Definição do tamanho da tela
largura_tela = 800
altura_tela = 600

# Criação da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Carregando a imagem de fundo
fundo = pygame.image.load("3134834.jpg")
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

# Função para desenhar a cobrinha
def desenhar_cobrinha(cobrinha):
    for posicao in cobrinha:
        pygame.draw.rect(tela, COR_COBRA, (posicao[0], posicao[1], 20, 20))

# Função para desenhar a comida
def desenhar_comida(comida):
    imagem_comida = pygame.image.load("candy1.png") #====LEVYBRAGA
    tamanho_comida = (35, 35)
    imagem_comida = pygame.transform.scale(imagem_comida, tamanho_comida)
    tela.blit(imagem_comida, (comida[0], comida[1]))

# Função principal do jogo
def jogo():
    # Posição inicial da cobrinha
    x = largura_tela / 2
    y = altura_tela / 2

    # Velocidade inicial da cobrinha
    velocidade_x = 0
    velocidade_y = 0

    # Inicialização da cobrinha
    cobrinha = []
    tamanho_inicial = 1
    for i in range(tamanho_inicial):
        cobrinha.append([x, y])

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_tela - 20) / 30) * 30
    comida_y = round(random.randrange(0, altura_tela - 20) / 30) * 30

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x = -10
                    velocidade_y = 0
                elif event.key == pygame.K_RIGHT:
                    velocidade_x = 10
                    velocidade_y = 0
                elif event.key == pygame.K_UP:
                    velocidade_y = -10
                    velocidade_x = 0
                elif event.key == pygame.K_DOWN:
                    velocidade_y = 10
                    velocidade_x = 0
                break

        x += velocidade_x
        y += velocidade_y
    
        if x >= largura_tela or x < 0 or y >= altura_tela or y < 0:
            pygame.quit()
            quit()

        tela.blit(fundo, (0, 0))

        desenhar_cobrinha(cobrinha)
        desenhar_comida((comida_x, comida_y))

        pygame.display.update()
#verificar se a area da cabeça da cobra colide com a comida
        if x + 20 >= comida_x and x <= comida_x + 20 and y + 20 >= comida_y and y <= comida_y + 20:
            comida_x = round(random.randrange(0, largura_tela - 20) / 20) * 20
            comida_y = round(random.randrange(0, altura_tela - 20) / 20) * 20
            tamanho_inicial += 1

        cobrinha.append([x, y])

        if len(cobrinha) > tamanho_inicial:
            del cobrinha[0]

        for segmento in cobrinha[:-1]:
            if segmento == [x, y]:
                pygame.quit()
                quit()
            
        pygame.time.Clock().tick(15)

# Execução do jogo
jogo()