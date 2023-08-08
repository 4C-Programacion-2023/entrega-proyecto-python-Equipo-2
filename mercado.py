from planteles2 import *
import random
import random as rd
import os
#En un futuro terminar la parte de eleccion de jugadores en formacion.
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
        goles_local = random.randint(0, 5)
        goles_visitante = random.randint(0, 5)
        resultado = {
            'Equipo Local': equipo_local,
            'Goles Local': goles_local,
            'Equipo Visitante': equipo_visitante,
            'Goles Visitante': goles_visitante
        }
        resultados_fecha.append(resultado)
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
    valoracion_local = calcular_valoracion_equipo(equipo_local, equipos20)
    valoracion_visitante = calcular_valoracion_equipo(equipo_visitante, equipos20)
        
    max_goles_local = 3  # Valoración menor a 40
    if valoracion_local > 40:
        max_goles_local = 4
    if valoracion_local > 60:
        max_goles_local = 6
    if valoracion_local > 100:
        max_goles_local = 8
        
    max_goles_visitante = 3  # Valoración menor a 40
    if valoracion_visitante > 40:
        max_goles_visitante = 4
    if valoracion_visitante > 60:
        max_goles_visitante = 6
    if valoracion_visitante > 100:
        max_goles_visitante = 8
    
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
    tabla_posiciones = {equipo: {'Puntos': 0, 'GF': 0, 'GC': 0} for equipo in equipos}
    while not salir_menu1:
        print("-----Menu de partidos.-----")
        print("1_Jugar partido.")
        print("2_Armar formacion.")
        print("3_Volver al menu principal.")
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
                                    formacion_armada = False
                    else:
                        print("¡Primero debes armar la formación para poder jugar el partido!")
                        salir_menu1 = True
        elif respuesta == 3:
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
        print("4. Volver al menú principal")

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
        print("2. Salir al Menú Principal")
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
                        print(jugador)  # Mostrar jugadores disponibles para entrenar
                        print("Edad:", atributos["Edad"])
                        print("Posición:", atributos["Posición"])
                        print("Valoración:", atributos["Valoración"])
                        print("---------------------")

                if not jugadores_entrenar:
                    print("No hay jugadores disponibles para entrenar.")
                else:
                    num_entrenar = min(4, len(jugadores_entrenar))  # Máximo 4 jugadores a entrenar

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
                            valoracion_jugador += 0.20
                        elif edad_jugador <= 26:
                            valoracion_jugador += 0.15
                        elif edad_jugador < 30:
                            valoracion_jugador += 0.10

                        respuesta2[jugador]["Valoración"] = min(10, valoracion_jugador)  # Limitar la valoración máxima a 10

                    print("Entrenamiento completado.")
                    print("Valoración de los jugadores después del entrenamiento:")
                    for jugador, atributos in respuesta2.items():
                        print(jugador)
                        print("Valoración:", atributos["Valoración"])
                        print("---------------------")
                    entrenado = True

        elif entrenamiento == 2:
            salir_menu1 = True

        else:
            print("¡Opción inválida! Intente nuevamente.")
    
    return entrenado

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
                print("6. Mostrar goleadores")
                print("7. Mostrar tabla de posiciones")
                print("8. Mostrar fixture")
                print("9. Mostrar vitrina del club")
                print("10. Volver al menú principal")
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
                elif respuesta3 == 8:
                    jugar_partido=True
                    for fecha, partidos in enumerate(fixture, start=1):
                        print(f"Fecha {fecha}:")
                        for partido in partidos:
                            equipo_local, equipo_visitante = partido
                            print(f"{equipo_local} vs. {equipo_visitante}")
                        print()
                elif respuesta3 == 10:
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