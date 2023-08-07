import random as rd
def armar_fixture(equipos):
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

equipo_usuario = "boca juniors"
equipos = ["boca juniors", "river plate", "racing club", "independiente", "vélez sarsfield",
           "san lorenzo", "huracán", "argentinos juniors", "central córdoba", "belgrano",
           "platense", "barracas central", "godoy cruz", "banfield", "gimnasia",
           "atlético tucumán", "sarmiento", "tigre", "colón", "lanús", "talleres",
           "arsenal", "unión", "newells", "rosario central", "instituto", "defensa y justicia",
           "estudiantes"]

fixture = armar_fixture(equipos)
fechas = fixture

def jugar_proximo_partido(equipo_usuario, fechas):
    for i, fecha in enumerate(fechas):
        if any(equipo_usuario in partido for partido in fecha):
            print(f"Fecha {i + 1}:")
            for partido in fecha:
                equipo_local, equipo_visitante = partido
                print(f"{equipo_local} vs. {equipo_visitante}")

            # Pedir confirmación al usuario
            while True:
                respuesta = input("¿Deseas jugar esta fecha? (s/n): ").lower()
                if respuesta == "s":
                    for partido in fecha:
                        equipo_local, equipo_visitante = partido
                        resultado = simular_partido(equipo_local, equipo_visitante)
                        print(f"Resultado: {resultado}")
                    print("-" * 40)
                    break
                elif respuesta == "n":
                    print("Fecha no jugada.")
                    print("-" * 40)
                    break
                else:
                    print("Respuesta no válida. Ingresa 's' para jugar o 'n' para no jugar.")

def simular_partido(equipo_local, equipo_visitante):
    goles_local = rd.randint(0, 3)
    goles_visitante = rd.randint(0, 3)
    return f"{equipo_local} {goles_local} - {goles_visitante} {equipo_visitante}"

# Ejecutamos la simulación de la fecha actual
jugar_proximo_partido(equipo_usuario, fechas)