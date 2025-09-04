import pygame
import os

# Inicializando o Pygame
pygame.init()

# Definido o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela com imagem")

# Definindo a imagem
BG_COLOR = (30, 30, 40) # cor de fundo (um tom escuro)

# Carregar a imagem
image_file = "player.png" # coloque o nome da sua imagem
if os.path.exists(image_file):
    img = pygame,image,load(image_file).convert_alpha() # Carregar a 
    img_rect = img.get_rect

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()