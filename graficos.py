import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("LPF - Manager")

# Cargar el fondo
fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (screen_width, screen_height))

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Estado actual del juego
estado = "menu_principal"

# Equipos disponibles
equipos20 = ["equipo1", "equipo2", "equipo3"]  # Agrega tus equipos disponibles aquí

# Texto para la entrada de nombre de equipo
input_text = ""
input_rect = pygame.Rect(250, 300, 300, 40)
active = False
mensaje_info_juego = """
-----Información General-----
El juego consiste en un simulador de gestión de un equipo de fútbol
al estilo FIFA. El jugador asume el papel de entrenador y tiene la opción
de elegir uno de los equipos disponibles, como Boca Juniors, River Plate,
Independiente, etc. Una vez seleccionado el equipo, el jugador puede
acceder a un menú con varias opciones.
¡Sé el gestor de tu equipo favorito! ;)
Presiona ENTER para volver al menú principal.
"""
# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = not active
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    # Verificar si el nombre de equipo es válido
                    equipo_elegido = input_text.lower()
                    if equipo_elegido in equipos20:
                        estado = "menu_equipo"
                        active = False
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    screen.blit(fondo, (0, 0))  # Dibujar el fondo

    if estado == "menu_principal":
        menu_text = font.render("-----LPF - Manager-----", True, black)
        screen.blit(menu_text, (150, 100))

        menu_text = font.render("1. Información del juego", True, black)
        screen.blit(menu_text, (100, 200))

        menu_text = font.render("2. Elegir equipo", True, black)
        screen.blit(menu_text, (100, 250))

        respuesta1 = pygame.key.get_pressed()

        if respuesta1[pygame.K_1]:
            estado = "info_juego"
        elif respuesta1[pygame.K_2]:
            estado = "elegir_equipo"
    elif estado == "info_juego":
        info_text = font.render(mensaje_info_juego, True, black)
        screen.blit(info_text, (50, 100))

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            estado = "menu_principal"
    elif estado == "elegir_equipo":
        equipos_text = font.render("Equipos disponibles:", True, black)
        screen.blit(equipos_text, (100, 100))

        for i, equipo in enumerate(equipos20, start=1):
            equipo_text = font.render(f"{i}. {equipo.title()}", True, black)
            screen.blit(equipo_text, (100, 150 + i * 50))

        # Dibujar cuadro de entrada de nombre de equipo
        txt_surface = font.render(input_text, True, black)
        width = max(200, txt_surface.get_width() + 10)
        input_rect.w = width
        screen.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(screen, black, input_rect, 2)

        pygame.display.update()

    pygame.display.update()
