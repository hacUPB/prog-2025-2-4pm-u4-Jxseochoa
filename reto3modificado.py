def ejercicio1():
    aviones = {
        1: {
            "nombre": "Cessna 172 Skyhawk",
            "peso": 10000.0,
            "area": 16.2,
            "v": 65.0,
            "cl_base": 0.4,
            "aoa_inicial": 5.0
        },
        2: {
            "nombre": "Airbus A320",
            "peso": 600000.0,
            "area": 122.6,
            "v": 130.0,
            "cl_base": 0.5,
            "aoa_inicial": 5.0
        },
        3: {
            "nombre": "Boeing 747-8",
            "peso": 3500000.0,
            "area": 554.0,
            "v": 250.0,
            "cl_base": 0.6,
            "aoa_inicial": 5.0
        }
    }

    texto_inicial = [
        "=== EJERCICIO 1: ESTABILIDAD EN TURBULENCIA ===",
        "Seleccione un avión:",
        "1. Cessna 172 Skyhawk",
        "2. Airbus A320",
        "3. Boeing 747-8"
    ]

    acciones_aoa = {"a": 1.0, "d": -1.0, "m": 0.0}
    acciones_vel = {"a": 10.0, "d": -10.0, "m": 0.0}
    RHO = 1.225

    def calcular_sustentacion(RHO, v, cl, area):
        return 0.5 * RHO * (v ** 2) * cl * area

    for linea in texto_inicial:
        print(linea)

    opcion = int(input("Ingrese opción (1-4): "))

    if opcion in aviones:
        avion = aviones[opcion]
        nombre = avion["nombre"]
        peso = avion["peso"]
        area = avion["area"]
        v = avion["v"]
        cl_base = avion["cl_base"]
        aoa_inicial = avion["aoa_inicial"]
        aoa = aoa_inicial
        estado_final = "Exitoso"

        print("Avión seleccionado:", nombre)

        for segundo in range(1, 9):
            print("Segundo", segundo)
            print("Ángulo de ataque actual:", aoa, "°")

            eleccion_aoa = input("¿Ángulo de ataque: (a)umentar, (d)isminuir o (m)antener? ").strip().lower()
            if eleccion_aoa in acciones_aoa:
                aoa += acciones_aoa[eleccion_aoa]
                if acciones_aoa[eleccion_aoa] > 0:
                    print("El ángulo de ataque aumentó a:", aoa, "°")
                elif acciones_aoa[eleccion_aoa] < 0:
                    print("El ángulo de ataque disminuyó a:", aoa, "°")
                else:
                    print("El ángulo de ataque se mantiene en:", aoa, "°")
            else:
                print("Opción inválida → se mantiene el ángulo de ataque.")

            cl_actual = cl_base + 0.1 * (aoa - aoa_inicial)
            sustentacion = calcular_sustentacion(RHO, v, cl_actual, area)
            print("Velocidad =", v, "m/s | Cl =", cl_actual, "| Sustentación =", sustentacion, "N")

            if sustentacion >= peso:
                print("Estado: Estable")
            elif sustentacion < 0.5 * peso:
                print("Estado: Pérdida - Fin de simulación")
                estado_final = "Perdida"
                break
            elif sustentacion < 0.8 * peso:
                print("Estado: Crítico")

            print("Velocidad actual:", v, "m/s")
            decision_v = input("¿Velocidad: (a)umentar, (d)isminuir o (m)antener? ").strip().lower()
            if decision_v in acciones_vel:
                v += acciones_vel[decision_v]
                if acciones_vel[decision_v] > 0:
                    print("Velocidad aumentó a:", v, "m/s")
                elif acciones_vel[decision_v] < 0:
                    print("Velocidad disminuyó a:", v, "m/s")
                else:
                    print("Velocidad se mantiene en:", v, "m/s")
            else:
                print("Opción inválida → se mantiene la velocidad.")

        if estado_final == "Exitoso":
            print("El avión logró atravesar la turbulencia con éxito.")
        else:
            print("El avión no logró superar la turbulencia.")
    else:
        print("Opción inválida. Debe seleccionar 1, 2,3 o 4.")

def mostrar_info():
    aviones = {
        1: {
            "nombre": "Cessna 172 Skyhawk",
            "peso": 10000.0,
            "area": 16.2,
            "v": 65.0,
            "cl_base": 0.4,
            "aoa_inicial": 5.0
        },
        2: {
            "nombre": "Airbus A320",
            "peso": 600000.0,
            "area": 122.6,
            "v": 130.0,
            "cl_base": 0.5,
            "aoa_inicial": 5.0
        },
        3: {
            "nombre": "Boeing 747-8",
            "peso": 3500000.0,
            "area": 554.0,
            "v": 250.0,
            "cl_base": 0.6,
            "aoa_inicial": 5.0
        }
    }

    print("AVIONES Y ESPECIFICACIONES")
    for info_avion, datos in aviones.items():
        print("-----------------")
        print(f"Avión {info_avion}:")
        for info, espec in datos.items():
            print(f"{info}: {espec}")
            
    
def mostrar_aviones():
    texto_inicial = [
        "1. Cessna 172 Skyhawk",
        "2. Airbus A320",
        "3. Boeing 747-8"
    ]
    print("LISTA DE MENSAJES")
    for linea in texto_inicial:
        print(linea)

# Menú de opción ejecución-salir
def menu():
    while True:
        print("=== ELECCIÓN DE PROGRAMA ===")
        print("1. Acceder al ejercicio.")
        print("2. Ver los aviones y sus especifiaciones.")
        print("3. Ver los aviones disponibles.")
        print("4. Salir")

        opcion = input ("Seleccione una opción: 1,2, 3 o 4.")

        if opcion =="1":
            ejercicio1()
        elif opcion =="2":
            mostrar_info()
        elif opcion =="3":
            mostrar_aviones()
        elif opcion == "4":
            print("Salió del programa.")
            break
        else:
            print("Opcion no válida")
menu()
