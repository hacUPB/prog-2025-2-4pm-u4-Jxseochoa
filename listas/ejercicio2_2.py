# Ejercicio 2: Selección de cajas para carga en una aeronave

##En una operación de carga aérea, se tiene una lista de cajas, cada una con un peso diferente. La aeronave tiene un límite máximo de peso que no debe ser superado por la suma de los pesos de las cajas seleccionadas. Debes escribir una función que recorra la lista de pesos de las cajas y agregue cada caja mientras no se exceda el peso máximo permitido. La función debe mostrar en pantalla los índices de las cajas seleccionadas y el peso total cargado.

def cargar_cajas(pesos, peso_maximo):
    seleccion = []
    peso_total = 0
    i = 1
    for p in pesos:
        if peso_total + p <= peso_maximo:
            seleccion.append(i)
            peso_total += p
        else:
            break
        i += 1

    print("Cajas seleccionadas:", seleccion)
    print("Peso total cargado:", peso_total, "kg")


pesos_cajas = [120, 400, 300, 180, 450, 200]
peso_max_avion = 1000

cargar_cajas(pesos_cajas, peso_max_avion)


