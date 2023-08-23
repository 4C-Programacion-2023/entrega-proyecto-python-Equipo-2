from planteles2 import *
import random
import random as rd
from collections import Counter
import os
#En un futuro terminar la parte de eleccion de jugadores en formacion.Terminar bien jugar partidos!!!!!!!
def vitrina_atletico_tucuman():
    return """
PALMARES DE ATLÉTICO TUCUMÁN:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_sarmiento():
    return """
PALMARES DE SARMIENTO:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_banfield():
    return """
PALMARES DE BANFIELD:

Torneos Nacionales (1)
    - 1 Primera División

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_godoy_cruz():
    return """
PALMARES DE GODOY CRUZ:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_boca(): 
    return """
PALMARES DE BOCA JUNIORS:
Torneos nacionales (52)

    -29 ligas profesionales
    -6 ligas amateurs
    -2 Copa Competencia Jockey Club
    -5 Copa Carlos Ibarguren
    -1 Copa Estímulo
    -1 Copa Competencia “George VI”
    -4 Copa Argentina
    -2 Supercopa Argentina
    -1 Copa Diego Maradona
    -1 Copa de la Liga 
    
    
Certámenes internacionales (22)

    -6 Copa Libertadores
    -3 Copa Intercontinental
    -2 Copa Sudamericana
    -1 Supercopa
    -4 Recopa Sudamericana
    -2 Copa Confraternidad
    -1 Tie Cup Competition
    -1 Copa de Honor Cousenier
    -1 Master
    -1 Copa de Oro Nicolás Leoz"""
def vitrina_river(): 
    return """
PALMARES DE RIVER PLATE:
Torneos Nacionales (54)

    -36 Torneos Nacionales
    -6 Copa de Competencia Jockey Club
    -3 Copa Ibarguren
    -1 Copa Adrián C. Escobar
    -4 Copa Carlos Ibarguren
    -3 Copa Argentina
    -1 Supercopa Argentina

Copas Internacionales  (15)

    -4 Copa Libertadores.
    -3 Copa Intercontinental.
    -1 Supercopa Sudamericana.
    -2 Copa Sudamericana.
    -4 Recopa Sudamericana.
    -1 Copa Suruga Bank. """
def vitrina_sanlorenzo(): 
    return """ 
PALMARES DEL CLUB ATLETICO SAN LORENZO DE ALMAGRO:
Torneos Nacionales (19)

    -15 títulos de Primera División.
    -1 título de Copa Campeonato.
    -1 título de Supercopa Argentina.
    -2 títulos de Copa Competencia.
    -3 títulos de Copa de Honor.
    -1 título de Copa de la República.
    -1 título de Copa Río de la Plata.

Copas Intrenacionales (5)

    -1 título de Copa Libertadores.
    -1 título de Copa Sudamericana.
    -1 título de Recopa Sudamericana.
    -1 título de Copa Mercosur.
    -2 títulos de Copa Aldao."""
def vitrina_racing(): 
    return """ 
PALMARES DE RACING CLUB DE AVELLANEDA:
Torneos Nacionales (27)

    -18 Ligas Argentina
    -6 Copas Competencia
    -1 Copa de honor
Copas Internacionales (4)

    -1 Copa Libertadores
    -1 Copa Intercontinental
    -1 Supercopa Sudamericana
    -1 Copa Sudamericana"""
def vitrina_independiente():
    return """
PALMARES DE INDEPENDIENTE:

Torneos Nacionales (23)
    -14 Ligas Argentina
    -9 Copas Nacionales

Copas Internacionales (19)

    -7 Copas Libertadores
    -2 Copas Intercontinentales
    -3 Copas Interamericanas
    -1 Supercopa Sudamericana
    -2 Copas Sudamericanas
    -1 Recopa Sudamericana"""
def vitrina_velez(): 
    return """
PALMARES VELEZ SARFIELD:
Torneos Nacionales (10)

    -10 Ligas Argentinas

Títulos Internacionales (4):

    1 Copa Libertadores
    1 Copa Intercontinental
    1 Supercopa Sudamericana
    1 Recopa Sudamericana
 """
def vitrina_estudiantes(): 
    return """ 
PALMARES DE ESTUDIANTES DE LA PLATA:

Torneos Nacionales (7)

    -6 Ligas Argentina
    -1 Copa Argentina

Copas Internacionales (10)

    -4 Copas Libertadores
    -1 Copa Intercontinental
    -3 Copas Interamericanas
    -1 Supercopa Sudamericana
    -1 Recopa Sudamericana
"""
def vitrina_huracan(): 
    return """ 
PALMARES DE HURACAN:

Torneos Nacionales (6)
    -5 Ligas Argentina
    -1 Copa Argentina

"""
def vitrina_atletico_tucuman():
    return """
PALMARES DE ATLÉTICO TUCUMÁN:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_lanus():
    return """
PALMARES DE LANÚS:

Torneos Nacionales (2)
    - 1 Torneo de Primera División
    - 1 Copa del Bicentenario

Copas Internacionales (2)
    - 1 Copa Conmebol Sudamericana
    - 1 Copa Suruga Bank
"""
def vitrina_colon():
    return """
PALMARES DE COLÓN:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_tigre():
    return """
PALMARES DE TIGRE:

Torneos Nacionales (2)
    - 2 Copas de la Liga Profesional

Copas Internacionales (1)
    - 1 Copa de la Superliga Argentina
"""
def vitrina_sarmiento():
    return """
PALMARES DE SARMIENTO:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_gimnasia():
    return """
PALMARES DE GIMNASIA:

Torneos Nacionales (1)
    - 1 Campeonato de Primera División

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_belgrano():
    return """
PALMARES DE BELGRANO:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_talleres():
    return """
PALMARES DE TALLERES:

Torneos Nacionales (1)
    - 1 Torneo Nacional

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_arsenal():
    return """
PALMARES DE ARSENAL:

Torneos Nacionales (2)
    - 1 Torneo Clausura
    - 1 Copa Argentina

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_rosario_central():
    return """
PALMARES DE ROSARIO CENTRAL:

Torneos Nacionales (3)
    - 1 Torneo Nacional
    - 1 Torneo Argentino A
    - 1 Primera B Nacional

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_union():
    return """
PALMARES DE UNIÓN:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_defensa_y_justicia():
    return """
PALMARES DE DEFENSA Y JUSTICIA:

Torneos Nacionales (2)
    - 1 Liga Profesional de Fútbol
    - 1 Copa Sudamericana

Copas Internacionales (1)
    - 1 Recopa Sudamericana
"""
def vitrina_instituto():
    return """
PALMARES DE INSTITUTO:

Torneos Nacionales (1)
    - 1 Primera B Nacional

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_barracas_central():
    return """
PALMARES DE BARRACAS CENTRAL:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_platense():
    return """
PALMARES DE PLATENSE:

Torneos Nacionales (0)
    - No ha ganado ligas nacionales.

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_central_cordoba():
    return """
PALMARES DE CENTRAL CÓRDOBA:

Torneos Nacionales (3)
    - 1 Primera B Nacional
    - 1 Torneo Argentino A
    - 1 Torneo Federal A

Copas Internacionales (0)
    - No ha ganado copas internacionales.
"""
def vitrina_newells():
    return """
PALMARES DE NEWELL'S OLD BOYS:

Torneos Nacionales (6)
    - 6 Torneos de Primera División

Copas Internacionales (1)
    - 1 Copa Libertadores
"""
presupuesto_equipos = {
    "boca juniors": 23000000,
    "river plate": 25000000,
    "argentinos juniors": 12000000,
    "san lorenzo": 15000000,
    "platense": 5000000,
    "instituto": 7000000,
    "talleres": 8000000,
    "belgrano": 6000000,
    "racing club": 18000000,
    "independiente": 20000000,
    "vélez sarsfield": 15000000,
    "huracán": 9000000,
    "barracas central": 3000000,
    "godoy cruz": 5000000,
    "banfield": 7000000,
    "gimnasia": 6000000,
    "atlético tucumán": 1000000,
    "sarmiento": 4000000,
    "tigre": 8000000,
    "colón": 8000000,
    "lanús": 12000000,
    "arsenal": 5500000,
    "unión": 7000000,
    "newells": 6000000,
    "rosario central": 10000000,
    "defensa y justicia": 10000000,
    "estudiantes": 11000000,
    "central córdoba": 9000000,
    "atletico tucuman": 1000000,
}
def mostrar_plantel(equipo_elegido, presupuesto_equipos):
    clear_screen()
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
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
equipos20 = {
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
equipos = ["boca juniors", "river plate", "racing club", "independiente", "vélez sarsfield",
           "san lorenzo", "huracán", "argentinos juniors", "central córdoba", "belgrano",
           "platense", "barracas central", "godoy cruz", "banfield", "gimnasia",
           "atlético tucumán", "sarmiento", "tigre", "colón", "lanús", "talleres",
           "arsenal", "unión", "newells", "rosario central", "instituto", "defensa y justicia",
           "estudiantes"]
def armar_fixture(equipos):
    clear_screen()
    fixture = []
    equipos_copy = equipos.copy()
    
    if len(equipos_copy) % 2 != 0:
        equipos_copy.append("descansa")
    
    rd.shuffle(equipos_copy)
    
    num_equipos = len(equipos_copy)
    num_rondas = num_equipos - 1
    partidos_por_fecha = num_equipos // 2
    
    for ronda in range(num_rondas):
        fecha_actual = []
        for i in range(partidos_por_fecha):
            equipo_local = equipos_copy[i]
            equipo_visitante = equipos_copy[num_equipos - 1 - i]
            fecha_actual.append((equipo_local, equipo_visitante))
        fixture.append(fecha_actual)
        
        equipos_copy = [equipos_copy[0]] + [equipos_copy[-1]] + equipos_copy[1:-1]
    return fixture
def jugar_fecha(equipo_usuario, fecha):
    clear_screen()
    print("Resultados de la fecha:")
    resultados_fecha = []
    for partido in fecha:
        equipo_local, equipo_visitante = partido
        resultado_partido = simular_partido(equipo_local, equipo_visitante, equipos20)
        resultados_fecha.append(resultado_partido)
        
        goles_local = resultado_partido['Goles Local']
        goles_visitante = resultado_partido['Goles Visitante']
        
        print(f"{equipo_local.title()} vs. {equipo_visitante.title()}: {goles_local}-{goles_visitante}")
    return resultados_fecha
def calcular_valoracion_equipo(nombre_equipo, equipos20):
    equipo = equipos20.get(nombre_equipo.lower())
    
    if equipo is None:
        return None
    
    valoracion_total = 0
    for jugador, info in equipo.items():
        valoracion_jugador = info.get("Valoración", 0)
        valoracion_total += valoracion_jugador
    
    return valoracion_total
def simular_partido(equipo_local, equipo_visitante, equipos20):
    valoracion_local = calcular_valoracion_equipo(nombre_equipo=equipo_local, equipos20=equipos20)
    valoracion_visitante = calcular_valoracion_equipo(nombre_equipo=equipo_visitante, equipos20=equipos20)
    
    # Ajustar máximos de goles según valoraciones
    if valoracion_local > 140:
        max_goles_local = 8
    elif valoracion_local > 130:
        max_goles_local = 7
    elif valoracion_local > 120:
        max_goles_local = 6
    elif valoracion_local > 100:
        max_goles_local = 5
    elif valoracion_local > 90:
        max_goles_local = 4
    else:
        max_goles_local = 3
    
    if valoracion_visitante > 140:
        max_goles_visitante = 8
    elif valoracion_visitante > 130:
        max_goles_visitante = 7
    elif valoracion_visitante > 120:
        max_goles_visitante = 6
    elif valoracion_visitante > 100:
        max_goles_visitante = 5
    elif valoracion_visitante > 90:
        max_goles_visitante = 4
    else:
        max_goles_visitante = 3
    
    goles_local = random.randint(0, max_goles_local)
    goles_visitante = random.randint(0, max_goles_visitante)
    
    jugadores_local = list(equipos20[equipo_local].keys())
    jugadores_visitante = list(equipos20[equipo_visitante].keys())
    
    goleadores = []

    for _ in range(goles_local):
        jugador_gol = random.choice(jugadores_local)
        goleadores.append(jugador_gol)

    for _ in range(goles_visitante):
        jugador_gol = random.choice(jugadores_visitante)
        goleadores.append(jugador_gol)
    
    resultado = {
        'Equipo Local': equipo_local,
        'Goles Local': goles_local,
        'Equipo Visitante': equipo_visitante,
        'Goles Visitante': goles_visitante,
        'Goleadores': goleadores  
    }
    
    return resultado
fixture = armar_fixture(equipos)
fechas = fixture
fecha_actual = 0
tabla_posiciones = {equipo: {'Puntos': 0, 'GF': 0, 'GC': 0} for equipo in equipos}
resultados_fecha = []
goleadores = []

def jugar_partidos(respuesta2, equipos20):
    clear_screen()
    global fecha_actual 
    respuesta2 = respuesta2.lower()
    salir_menu1 = False
    formacion_armada = False
    tabla_posiciones = {equipo: {'Puntos': 0, 'GF': 0, 'GC': 0, 'Partidos Jugados': 0} for equipo in equipos}
    while not salir_menu1:
        print("-----Menu de partidos.-----")
        print("1_Jugar partido.")
        print("2_Armar formacion.")
        print("3_Mostrar goleadores.")
        print("4_Mostrar tabla de posiciones.")
        print("5_Volver al menu principal.")
        respuesta = int(input("--Ingrese opcion:"))
        if respuesta == 2 :
            print(f"Bienvenido a la formacion de {respuesta2.title()}.")
            equipo_formacion=equipos20[respuesta2]
            defensores = []
            delanteros = []
            porteros = []
            volantes=[]
            valoracion_final_equipo= 0
            for nombre, info_jugador in equipo_formacion.items():
                posicion = info_jugador["Posición"]
                if posicion == "Defensor":
                    defensores.append(nombre)
                elif posicion == "Delantero":
                    delanteros.append(nombre)
                elif posicion == "Portero":
                    porteros.append(nombre)
                elif posicion == "Volante":
                    volantes.append(nombre)
            print("Vamos a formar la formacion!.")
            print(porteros)
            jugadores_porteros= min(1, len (porteros))
            porteros1=[]
            while len(porteros1) < jugadores_porteros:
                eleccion_porteros = input("Elija un jugador para colocar como portero (ingrese el nombre): ")
                valoracion_jugador = equipos20.get(respuesta2, {}).get(eleccion_porteros, {}).get("Valoración", None)
                if eleccion_porteros in porteros:
                    porteros1.append(eleccion_porteros)
                    valoracion_final_equipo += valoracion_jugador
                    porteros.remove(eleccion_porteros)
                else:
                     print("¡Jugador no válido! Intente nuevamente.")
            print(defensores)
            jugadores_defensores = min(4, len(defensores))
            defensores1 = []
            eleccion_defensores = None  
            while len(defensores1) < jugadores_defensores:
                eleccion_defensores = input("Elija un jugador para colocar como defensor (ingrese el nombre): ")
                if eleccion_defensores in defensores:
                    defensores1.append(eleccion_defensores)
                    defensores.remove(eleccion_defensores)
                else:
                    print("¡Jugador no válido! Intente nuevamente.")
            print(volantes)
            jugadores_volantes = min(3, len(volantes))
            volantes1 = []
            valoracion_jugador2 = equipos20.get(respuesta2, {}).get(eleccion_porteros, {}).get("Valoración", None)

            while len(volantes1) < jugadores_volantes:
                eleccion_volantes = input("Elija un jugador para colocar como volante (ingrese el nombre): ")
                if eleccion_volantes in volantes:
                    volantes1.append(eleccion_volantes)
                    valoracion_final_equipo+=valoracion_jugador2
                    volantes.remove(eleccion_volantes)
                else:
                     print("¡Jugador no válido! Intente nuevamente.")
            print(delanteros)
            jugadores_delanteros= min(3, len (delanteros))
            delanteros1=[]
            valoracion_jugador3 = equipos20.get(respuesta2, {}).get(eleccion_porteros, {}).get("Valoración", None)

            while len(delanteros1) < jugadores_delanteros:
                eleccion_Delanteros = input("Elija un jugador para colocar como delantero (ingrese el nombre): ")
                if eleccion_Delanteros in delanteros:
                    delanteros1.append(eleccion_Delanteros)
                    valoracion_final_equipo+=valoracion_jugador3
                    delanteros.remove(eleccion_Delanteros)
                else:
                     print("¡Jugador no válido! Intente nuevamente.")
            print("Formacion: 4-3-3")
            print("Delanteros:",delanteros1)
            print("Volantes:",volantes1)
            print("Defensores",defensores1)
            print("Portero:",porteros1)
            print("Valoracion final:",valoracion_final_equipo)
            formacion_armada = True
        elif respuesta == 1 :
            if formacion_armada:
                print("¡Jugando el partido!")
                fecha_actual = fechas.pop(0)
                resultados_fecha = jugar_fecha(equipos, fecha_actual)
                goleadores_partidos = []  
                for partido in resultados_fecha:
                     goleadores_partidos.extend(partido.get('Goleadores', []))  
                goleadores.extend(goleadores_partidos)
                for partido in resultados_fecha:
                    equipo_local = partido['Equipo Local']
                    equipo_visitante = partido['Equipo Visitante']
                    goles_local = partido['Goles Local']
                    goles_visitante = partido['Goles Visitante']
                
                    tabla_posiciones[equipo_local]['GF'] += goles_local
                    tabla_posiciones[equipo_local]['GC'] += goles_visitante
                    tabla_posiciones[equipo_visitante]['GF'] += goles_visitante
                    tabla_posiciones[equipo_visitante]['GC'] += goles_local
                        
                    if goles_local > goles_visitante:
                        tabla_posiciones[equipo_local]['Puntos'] += 3
                    elif goles_local < goles_visitante:
                        tabla_posiciones[equipo_visitante]['Puntos'] += 3
                    else:
                        tabla_posiciones[equipo_local]['Puntos'] += 1
                        tabla_posiciones[equipo_visitante]['Puntos'] += 1
                            
                    tabla_posiciones[equipo_local]['Partidos Jugados'] += 1
                    tabla_posiciones[equipo_visitante]['Partidos Jugados'] += 1
                tabla_ordenada = sorted(tabla_posiciones.items(), key=lambda x: (x[1]['Puntos'], x[1]['GF'], x[0]), reverse=True)
                
                print("Tabla de Posiciones:")
                print("-" * 65)
                print(f"{'Equipo':<20}{'Puntos':<10}{'GF':<10}{'GC':<10}{'Partidos Jugados':<15}")
                print("-" * 65)
                for equipo, datos in tabla_ordenada:
                    puntos = datos['Puntos']
                    goles_favor = datos['GF']
                    goles_contra = datos['GC']
                    partidos_jugados = datos['Partidos Jugados']
                    print(f"{equipo:<20}{puntos:<10}{goles_favor:<10}{goles_contra:<10}{partidos_jugados:<15}")
                print("-" * 65)
                
                input("Presiona Enter para continuar...")
                clear_screen()
                
                if not fechas:
                    campeon = max(tabla_ordenada, key=lambda x: (x[1]['Puntos'], x[1]['GF']))[0]
                    print(f"¡Campeón de la liga: {campeon}!")
                    tabla_posiciones = {equipo: {'Puntos': 0, 'GF': 0, 'GC': 0, 'Partidos Jugados': 0} for equipo in equipos}
                    formacion_armada = False
            else:
                 print("¡Primero debes armar la formación para poder jugar el partido!")
                 salir_menu1 = True
        elif respuesta == 3:
            print("-----Goleadores-----")
            counter_goleadores = Counter(goleadores)
            for jugador, goles in counter_goleadores.most_common(10):
                print(f"{jugador}: {goles} goles")
        elif respuesta == 4:
                print("Tabla de Posiciones:")
                print("-" * 65)
                print(f"{'Equipo':<20}{'Puntos':<10}{'GF':<10}{'GC':<10}{'Partidos Jugados':<15}")
                print("-" * 65)
                for equipo, datos in tabla_ordenada:
                    puntos = datos['Puntos']
                    goles_favor = datos['GF']
                    goles_contra = datos['GC']
                    partidos_jugados = datos['Partidos Jugados']
                    print(f"{equipo:<20}{puntos:<10}{goles_favor:<10}{goles_contra:<10}{partidos_jugados:<15}")
                print("-" * 65)
        elif respuesta == 5:
            return
        else:
            print("*****Valor incorrecto.Ingrese valor valido.*****")

                
def comprar_jugador(respuesta2, presupuesto_equipos, equipos20):
    clear_screen()
    while True:
        print("---Menu de transferencia de", respuesta2.title())
        print("1. Mostrar presupuesto")
        print("2. Mostrar jugadores")
        print("3. Comprar jugador")
        print("4. Informacion general")
        print("5. Volver al menú principal")

        respuesta4 = int(input("--Ingrese opción:"))

        if respuesta4 == 1:
            presupuesto_equipo = presupuesto_equipos[respuesta2]
            print("Presupuesto de", respuesta2, ": $", presupuesto_equipo)

        elif respuesta4 == 2:
            print("Equipos disponibles:")
            for equipo in equipos20:
                print(f"*{equipo.title()}*")

            while True:
                respuesta5 = input("--Ingrese el equipo del cual desea conocer sus jugadores: ").lower()
                if respuesta5 in equipos20:
                    equipo_elegido1 = equipos20[respuesta5]
                    for jugador, atributos in equipo_elegido1.items():
                        print(f"Jugador: {jugador}")
                        for atributo, valor in atributos.items():
                            print(f"{atributo.capitalize()}: {valor}")
                        print("--------------------")
                    break
                else:
                    print("*****Equipo inexistente. Ingrese un equipo válido.*****")

        elif respuesta4 == 3:
            print("Equipos disponibles:")
            for equipo in equipos20:
                print(f"*{equipo.title()}*")

            while True:
                respuesta6 = input("--Ingrese el equipo al cual desea comprar un jugador: ").lower()
                if respuesta6 in equipos20:
                    equipo_elegido2 = equipos20[respuesta6]
                    print("Jugadores disponibles en", respuesta6.title(), ":")
                    for jugador, atributos in equipo_elegido2.items():
                        print(f"*{jugador.title()}*")

                    while True:
                        jugador_a_comprar = input("--Ingrese el jugador que desea comprar: ").title()
                        if jugador_a_comprar in equipo_elegido2:
                            jugador_info = equipo_elegido2[jugador_a_comprar]
                            valor_mercado = jugador_info["Valor de Mercado"]
                            presupuesto_equipo = presupuesto_equipos[respuesta2]
                            presupuesto_equipo2 = presupuesto_equipos[respuesta6]

                            if valor_mercado < presupuesto_equipo:
                                seguridad1 = input(f"¿Está seguro de comprar a {jugador_a_comprar}? (s/n): ").lower()
                                if seguridad1 == "s":
                                    # Realizar la transferencia del jugador entre los equipos
                                    equipo_destino = equipos20[respuesta2]
                                    equipo_destino[jugador_a_comprar] = jugador_info
                                    del equipo_elegido2[jugador_a_comprar]
                                    # Actualizar presupuestos
                                    presupuesto_equipo -= valor_mercado
                                    presupuesto_equipo2 += valor_mercado
                                    presupuesto_equipos[respuesta2] = presupuesto_equipo
                                    presupuesto_equipos[respuesta6] = presupuesto_equipo2
                                    print(f"El jugador {jugador_a_comprar} ha sido comprado exitosamente.")
                                    return
                                elif seguridad1 == "n":
                                    print("No se realizará la compra del jugador.")
                                else:
                                    print("*****Opción inválida. Ingrese 's' o 'n'.*****")
                            else:
                                print("*****El precio del jugador supera el del presupuesto. Fondos insuficientes.*****")
                                return
                        else:
                            print("*****Jugador no existente en ese plantel. Ingrese un jugador válido.*****")
                else:
                    print("*****Equipo inexistente. Ingrese un equipo válido.*****")
        elif respuesta4 == 4:
            print("¡Bienvenido al menú de compra de jugadores!")
            print("En esta sección, podrás adquirir jugadores de otros equipos para reforzar tu plantilla.")
            print("Recuerda que solo puedes comprar un jugador si tienes suficiente presupuesto.")
            print("Además, ten en cuenta que el precio de un jugador está relacionado con su valor de mercado.")
            print("Si el precio supera tu presupuesto, no podrás realizar la compra.")
            print("¡Buena suerte en tus decisiones de compra!")
            print()
        elif respuesta4 == 5:
            return

        else:
            print("*****Opción incorrecta. Ingrese una opción válida.*****")
def vender_jugadores(respuesta2, presupuesto_equipos, equipos20):
    clear_screen()
    mostrar_plantel(respuesta2.lower(), presupuesto_equipos)
    plantel = equipos20[respuesta2.lower()]
    equipo_elegido = respuesta2.lower()
    presupuesto_equipo1 = presupuesto_equipos[equipo_elegido]

    cant_arqueros = sum(1 for jugador in plantel.values() if jugador['Posición'] == 'Portero')
    cant_defensores = sum(1 for jugador in plantel.values() if jugador['Posición'] == 'Defensor')
    cant_volantes = sum(1 for jugador in plantel.values() if jugador['Posición'] == 'Volante')
    cant_delanteros = sum(1 for jugador in plantel.values() if jugador['Posición'] == 'Delantero')

    if len(plantel) > 11 and cant_arqueros > 1 and cant_defensores > 4 and cant_volantes > 3 and cant_delanteros > 3:
        while True:
            jugador_a_vender = input("--Ingrese jugador que desea vender: ")
            if jugador_a_vender in plantel:
                seguridad22 = input("¿Está seguro que desea vender este jugador? (s/n): ").lower()
                if seguridad22 == "s":
                    valor_mercado_jugador_a_vender = plantel[jugador_a_vender]["Valor de Mercado"]

                    equipos_restantes = [equipo for equipo in equipos20 if equipo != equipo_elegido]
                    equipos_posibles = []

                    for equipo in equipos_restantes:
                        presupuesto_equipo_destino = presupuesto_equipos[equipo]
                        if valor_mercado_jugador_a_vender < presupuesto_equipo_destino:
                            equipos_posibles.append(equipo)

                    if equipos_posibles:
                        equipo_aleatorio = random.choice(equipos_posibles)
                        equipo_destino = equipos20[equipo_aleatorio]

                        jugador_info = plantel[jugador_a_vender]
                        equipo_destino[jugador_a_vender] = jugador_info
                        del plantel[jugador_a_vender]

                        presupuesto_equipo1 += valor_mercado_jugador_a_vender
                        presupuesto_equipos[equipo_elegido] = presupuesto_equipo1
                        presupuesto_equipos[equipo_aleatorio] -= valor_mercado_jugador_a_vender

                        print(f"El jugador {jugador_a_vender} ha sido vendido exitosamente.")
                        return
                    else:
                        print("No hay equipos con suficiente presupuesto para comprar al jugador.")
                elif seguridad22 == "n":
                    return
                else:
                    print("Opción inválida. Ingrese 's' o 'n'.")
            else:
                print("Jugador no existente en ese plantel. Ingrese un jugador válido.")
    else:
        print("No se puede vender jugadores. El plantel no tiene más de 11 jugadores o no cumple con la cantidad adecuada en cada posición.")
        return
def menu_entrenamiento(respuesta2, entrenado):
    clear_screen()
    salir_menu1 = False

    while not salir_menu1:
        print("Bienvenido al Menú de Entrenamiento.")
        print("1. Entrenar Jugadores")
        print("2. Informacion general")
        print("3.Salir al menú principal")
        entrenamiento = int(input("Seleccione una opción: "))

        if entrenamiento == 1:
            if entrenado:
                print("Ya has entrenado a tus jugadores. Debes jugar el próximo partido antes de entrenar nuevamente.")
            else:
                print("Plantel actual:")
                jugadores_entrenar = set()

                for jugador, atributos in respuesta2.items():
                    if atributos["Edad"] < 30:
                        jugadores_entrenar.add(jugador)
                        print(jugador)  
                        print("Edad:", atributos["Edad"])
                        print("Posición:", atributos["Posición"])
                        print("Valoración:", atributos["Valoración"])
                        print("---------------------")

                if not jugadores_entrenar:
                    print("No hay jugadores disponibles para entrenar.")
                else:
                    num_entrenar = min(4, len(jugadores_entrenar))  

                    jugadores_a_entrenar = set()

                    while len(jugadores_a_entrenar) < num_entrenar:
                        eleccion_entrenamiento = input("Elija un jugador para entrenar (ingrese el nombre): ")

                        if eleccion_entrenamiento in jugadores_entrenar:
                            jugadores_a_entrenar.add(eleccion_entrenamiento)
                        else:
                            print("¡Jugador no válido! Intente nuevamente.")

                    for jugador in jugadores_a_entrenar:
                        edad_jugador = respuesta2[jugador]["Edad"]
                        valoracion_jugador = respuesta2[jugador]["Valoración"]

                        if edad_jugador <= 22:
                            valoracion_jugador += 0.15
                        elif edad_jugador <= 26:
                            valoracion_jugador += 0.10
                        elif edad_jugador < 30:
                            valoracion_jugador += 0.5

                        respuesta2[jugador]["Valoración"] = min(10, valoracion_jugador)  

                    print("Entrenamiento completado.")
                    print("Valoración de los jugadores después del entrenamiento:")
                    for jugador, atributos in respuesta2.items():
                        print(jugador)
                        print("Valoración:", atributos["Valoración"])
                        print("---------------------")
                    entrenado = True
        elif entrenamiento == 2 :
            print("Bienvenido a la información general acerca del menú de entrenamientos.")
            print("En este menú tendrás la oportunidad de entrenar a tus jugadores y llevarlos al 100% para tu próximo partido.")
            print("Recuerda que solamente habrá 1 entrenamiento por partido, por lo que mi recomendación es que siempre aproveches las oportunidades para entrenar.")
            print("También ten en cuenta que los entrenamientos son solo para 4 jugadores a la vez, y a medida que la edad aumenta, la valoración del jugador no mejorará tanto, llegando al punto en que al cumplir los 30 años dejará de aumentar su media.")
        elif entrenamiento == 3 :
            salir_menu1 = True

        else:
            print("¡Opción inválida! Intente nuevamente.")
    
    return entrenado
def vitrina(equipo_nombre):
    equipos201 = {
        "boca juniors": vitrina_boca,
        "river plate": vitrina_river,
        "racing club": vitrina_racing,
        "independiente": vitrina_independiente,
        "vélez sarsfield": vitrina_velez,
        "san lorenzo": vitrina_sanlorenzo,
        "huracán": vitrina_huracan,
        "central córdoba": vitrina_central_cordoba,
        "belgrano": vitrina_belgrano,
        "platense": vitrina_platense,
        "barracas central": vitrina_barracas_central,
        "godoy cruz": vitrina_godoy_cruz,
        "banfield": vitrina_banfield,
        "gimnasia": vitrina_gimnasia,
        "atlético tucumán": vitrina_atletico_tucuman,
        "sarmiento": vitrina_sarmiento,
        "tigre": vitrina_tigre,
        "colón": vitrina_colon,
        "lanús": vitrina_lanus,
        "talleres": vitrina_talleres,
        "arsenal": vitrina_arsenal,
        "unión": vitrina_union,
        "newells": vitrina_newells,
        "rosario central": vitrina_rosario_central,
        "instituto": vitrina_instituto,
        "defensa y justicia": vitrina_defensa_y_justicia,
        "estudiantes": vitrina_estudiantes,
    }

    equipo_nombre_lower = equipo_nombre.lower()
    
    if equipo_nombre_lower in equipos201:
        print(equipos201[equipo_nombre_lower]())
    else:
        print("Equipo no encontrado en la lista.")

entrenado = False 
jugar_partido=False
while True:
    print("-----LPF - Manager-----")
    print("1. Información del juego")
    print("2. Elegir equipo")
    
    respuesta1 = int(input("--Ingrese opción:"))

    if respuesta1 == 2:
        print("Equipos disponibles:")
        for equipo in equipos20:
            print(f"*{equipo.title()}*")

        respuesta2 = input("--Ingrese su opción: ").lower()
        if respuesta2 in equipos20:
            while True:
                print(f"-----Menu del equipo {respuesta2.title()}-----")
                print("1. Mostrar plantel")
                print("2. Realizar compra de jugador")
                print("3. Vender jugador")
                print("4. Realizar entrenamiento")
                print("5. Jugar siguiente partido")
                print("6. Mostrar fixture")
                print("7. Mostrar vitrina del club")
                print("8. Volver al menú principal")
                respuesta3 = int(input("--Ingrese opción:"))

                if respuesta3 == 1:
                    mostrar_plantel(respuesta2.lower(), presupuesto_equipos)
                elif respuesta3 == 2:
                    comprar_jugador(respuesta2, presupuesto_equipos, equipos20)
                elif respuesta3 == 3:
                    vender_jugadores(respuesta2, presupuesto_equipos, equipos20)
                elif respuesta3 == 4:
                    entrenado = menu_entrenamiento(equipos20[respuesta2], entrenado)
                elif respuesta3 == 5:
                    if jugar_partido == True:     
                        jugar_partidos(respuesta2,equipos20)
                    else:
                        print("Debes armar el fixture antes para eso, debes dirigerte a la opcion armar fixture.")
                elif respuesta3 == 6:
                    jugar_partido=True
                    for fecha, partidos in enumerate(fixture, start=1):
                        print(f"Fecha {fecha}:")
                        for partido in partidos:
                            equipo_local, equipo_visitante = partido
                            print(f"{equipo_local} vs. {equipo_visitante}")
                        print()
                elif respuesta3 == 7:
                    vitrina(equipo_nombre=respuesta2)
                elif respuesta3 == 8:
                    break
                    

                else:
                    print("*****Valor incorrecto. Ingrese un valor correcto.*****")

        else:
            print("*****Valor incorrecto. Ingrese un valor correcto.*****")

    elif respuesta1 == 1:
        print("")
        print("-----Información General-----")
        print("El juego consiste en un simulador de gestión de un equipo de fútbol al estilo FIFA. El jugador asume el papel de entrenador y tiene la opción de elegir uno de los equipos disponibles, como Boca Juniors, River Plate, Independiente, etc.\nUna vez seleccionado el equipo, el jugador puede acceder a un menú con varias opciones.")
        print("¡Sé el gestor de tu equipo favorito! ;)")
        print("")

    else:
        print("*****Valor incorrecto. Ingrese un valor correcto.*****")