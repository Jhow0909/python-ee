import pygame
import os

# Inicializando o Pygame
pygame.init()

# Definido o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)), pygame.RESIZABLE
pygame.display.set_caption("Mover imagem com setas")

# Definindo a imagem
BG_COLOR = (193, 0, 40) # cor de fundo (um tom escuro)

# Carregar a imagem
image_file = "player.png" # coloque o nome da sua imagem aqui
if os.path.exists(image_file):
    img = pygame,image,load(image_file).convert_alpha() # Carregar a 
    img_rect = img.get_rect (center=(WIDTH // 2, HEIGHT // 2)) #centraliza a imagem
else:
    print("imagem não encontrada!!")
    
    #velocidade de movimento
    SPEED = 1 #pixels por movimento
    
    # Função para centralizar a imagem conforme o tamanho da tela
    def centraliza_image():
        global img_rect, WIDTH, HEIGHT
        img_rect.center = (WIDTH // 2, HEIGTH // 2) # centraliza a imagem no centro da tela
    
    # variaveis para controle de redimensionamento
    last_width, last_height = WIDTH, HEIGHT  
    
    # limite de movimento para nao sair da tela
def limit_movement()
    global ing rect, WIDTH, HEIGHT
Limita a posição da imagen para não sair da tela
if img rect.left < 0:
    img rect.left = 0
if img rect.right > WIDTH:
    ing rect.right = WIDTH
if img rect.top < 0:
    ing rect.top = 0
if img rect.bottom > HEIGHT:
    ing rect.bottom = HEIGHT
    
    # loop principal do jogo
    running = True
    while running:
        for event in pygmae.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    #verifica se o tamanho da janeça foi alterado
    current_widht, current-height = screen.get_size()
    
    # se a janela foi redimensionada, centraliza a imagem
    if current_widht != last_widht or current_height != last-height:
        WIDHT, HEIGHT = current_widht, current_height
        centraliza_image()
        last_WIDHT, last_height = curent_widht, current_height
        
        # Pega as teclas pressionadas
        keys = pygame.key.get_pressed()
        
        # Movementação da imagem
        if keys[pygame.K_LEFT]:
            img_rect.x -= SPEED
        if keys[pygame.K_RIGHT]:
            img_rect.x += SPEED
        if keys[pygame.K_UP]:
            img_rect.x -= SPEED
        if keys[pygame.K_DOWN]:
            img_rect.x += SPEED
            
            # Limita o movimento para não sair da tela
            limit_movement()
            
            # Preencher o fundo
            screen.fill (BG_COLOR)
            
            #desenhar a imagem na tela
            screen.fill (img, img_rect.topleft)
            
            # atulizar a tela
            pygame.display.flip()
            
        #finalizaz o pygame
        pygame.quit()