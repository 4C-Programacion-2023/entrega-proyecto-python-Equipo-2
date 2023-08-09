import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("LPF - Manager")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Bucle principal
while True:
    screen.fill(white)

    # Dibujar opciones del menú
    menu_text = font.render("1. Información del juego", True, black)
    screen.blit(menu_text, (100, 200))

    menu_text = font.render("2. Elegir equipo", True, black)
    screen.blit(menu_text, (100, 250))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if 100 < x < 500 and 200 < y < 250:
                print("Opción 1 seleccionada")  # Aquí puedes implementar la lógica de la opción 1

            if 100 < x < 500 and 250 < y < 300:
                print("Opción 2 seleccionada")  # Aquí puedes implementar la lógica de la opción 2

