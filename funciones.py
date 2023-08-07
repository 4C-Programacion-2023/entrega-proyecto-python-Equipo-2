import random
from planteles2 import *

def mostrar_fixture(fixture):
    print("-----Fixture del Equipo-----")
    for partido in fixture:
        equipo_local, equipo_visitante = partido
        print(f"{equipo_local.title()} vs {equipo_visitante.title()}")

def generar_fixture(equipo_seleccionado, equipos):
    if equipo_seleccionado not in equipos:
        print(f"El equipo '{equipo_seleccionado}' no se encuentra en la lista de equipos.")
        return None

    equipos_sin_seleccionado = [equipo for equipo in equipos if equipo != equipo_seleccionado]

    fixture = []
    num_equipos = len(equipos_sin_seleccionado)
    num_partidos = num_equipos * 2

    for i in range(num_partidos):
        if i % 2 == 0:
            fixture.append((equipo_seleccionado, equipos_sin_seleccionado[i % num_equipos]))
        else:
            fixture.append((equipos_sin_seleccionado[i % num_equipos], equipo_seleccionado))

    return fixture
def menu_entrenamiento(respuesta2):
    salir_menu1 = False

    while not salir_menu1:
        print("Bienvenido al Menú de Entrenamiento.")
        print("1. Entrenar Jugadores")
        print("2. Salir al Menú Principal")
        entrenamiento = int(input("Seleccione una opción: "))

        if entrenamiento == 1:
            for jugador, atributos in respuesta2.items():
                print(jugador)
                print("Edad:", atributos["Edad"])
                print("Posición:", atributos["Posición"])
                print("Valoración:", atributos["Valoración"])
                print("---------------------")

            jugadores_entrenar = set()
            num_entrenar = min(4, len(respuesta2))  # Máximo 4 jugadores a entrenar

            while len(jugadores_entrenar) < num_entrenar:
                eleccion_entrenamiento = input("Elija un jugador para entrenar (ingrese el nombre): ")

                if eleccion_entrenamiento in respuesta2:
                    jugadores_entrenar.add(eleccion_entrenamiento)
                else:
                    print("¡Jugador no válido! Intente nuevamente.")

            for jugador in jugadores_entrenar:
                edad_jugador = respuesta2[jugador]["Edad"]
                valoracion_jugador = respuesta2[jugador]["Valoración"]

                if edad_jugador <= 22:
                    valoracion_jugador += 0.20
                elif edad_jugador <= 26:
                    valoracion_jugador += 0.15
                elif edad_jugador < 30:
                    valoracion_jugador += 0.10

                respuesta2[jugador]["Valoración"] = valoracion_jugador

            print("Entrenamiento completado.")
            print("Valoración de los jugadores después del entrenamiento:")
            for jugador, atributos in respuesta2.items():
                print(jugador)
                print("Valoración:", atributos["Valoración"])
                print("---------------------")

def mostrar_plantel(equipo_elegido, presupuesto_equipos):
    equipos2 = {
        "boca juniors": boca_plantel,
        "river plate": river_plantel,
        "racing club": racing_club_plantel,
        "independiente": independiente_plantel,
        "vélez sarsfield": velez_plantel,
        "san lorenzo": san_lorenzo_plantel,
        "huracán": huracan_plantel,
        "argentinos juniors": argentinos_juniors_plantel,
        "central córdoba": central_cordoba_plantel,
        "belgrano": belgrano_plantel,
        "platense": platense_plantel,
        "barracas central": barracas_central_plantel,
        "godoy cruz": godoy_cruz_plantel,
        "banfield": banfield_plantel,
        "gimnasia": gimnasia_plantel,
        "atlético tucumán": atletico_tucuman_plantel,
        "sarmiento": sarmiento_plantel,
        "tigre": tigre_plantel,
        "colón": colon_plantel,
        "lanús": lanus_plantel,
        "talleres": talleres_plantel,
        "arsenal": arsenal_plantel,
        "unión": union_plantel,
        "newells": newells_plantel,
        "rosario central": rosario_central_plantel,
        "instituto": instituto_plantel,
        "defensa y justicia": defensa_y_justicia_plantel,
        "estudiantes": estudiantes_plantel,
    }

    equipo_elegido = equipo_elegido.lower()

    if equipo_elegido not in equipos2:
        print("El equipo elegido no se encuentra en la lista.")
        return

    plantel = equipos2[equipo_elegido]

    print(f"Plantel de {equipo_elegido.capitalize()}:")
    for jugador, caracteristicas in plantel.items():
        print(f"{jugador.capitalize()}")
        for caracteristica, valor in caracteristicas.items():
            print(f"{caracteristica.capitalize()}: {valor}")
        print("-" * 10)  # Línea de puntos entre jugadores

    if equipo_elegido in presupuesto_equipos:
        print(f"Presupuesto del equipo {equipo_elegido.capitalize()}: ${presupuesto_equipos[equipo_elegido]}")
    else:
        print("El equipo seleccionado no tiene un presupuesto definido.")

