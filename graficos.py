import pygame
import sys

pygame.init()

#configuración pantalla
ancho = 800
alto = 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Elegir Opción en Pygame")
#paltea de colores

Blanco = (255,255,255)
Rojo = (255,0,0)
Verde = (0,255,0)
Azul = (0,0,255)
Negro = (0,0,0)

#fuente texto
fuente = pygame.font.Font(None, 48)
color_texto = (255, 255, 255)

#opciones
opciones = [
    "Información del juego",
    "Elegir equipo"
]

# Fondo de un juego de fútbol
fondo_juego = pygame.image.load("fondo_futbol.jpg")
fondo_juego = pygame.transform.scale(fondo_juego, (ancho, alto))

# Variable para almacenar el número ingresado
numero_ingresado = ""
opcion_seleccionada = None

#bucle juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.unicode.isnumeric():
                numero_ingresado += evento.unicode
            elif evento.key == pygame.K_RETURN:
                if numero_ingresado:
                    indice_opcion = int(numero_ingresado) - 1  
                    if 0 <= indice_opcion < len(opciones):
                        opcion_seleccionada = opciones[indice_opcion]
                    numero_ingresado = ""

    pantalla.blit(fondo_juego, (0, 0)) 

    texto_y = 200
    for i, opcion in enumerate(opciones, start=1):
        texto_opcion = fuente.render(f"{i}. {opcion}", True, color_texto)
        pantalla.blit(texto_opcion, (50, texto_y))
        texto_y += 70

    if opcion_seleccionada is not None:
        texto_renderizado = fuente.render(f"Opción seleccionada: {opcion_seleccionada}", True, color_texto)
        pantalla.blit(texto_renderizado, (50, alto - 100))

    pygame.display.flip()



