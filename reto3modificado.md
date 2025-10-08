# Reto Unidad #3 Modificado con Diccionarios y Listas

## Código del ejercicio 1 

    RHO = 1.225

    print("=== EJERCICIO 1: ESTABILIDAD EN TURBULENCIA ===")
    print("Seleccione un avión:")
    print("1. Cessna 172 Skyhawk")
    print("2. Airbus A320")
    print("3. Boeing 747-8")

    opcion = int(input("Ingrese opción (1-3): "))

    if opcion == 1:
        nombre = "Cessna 172 Skyhawk"
        peso = 10000.0
        area = 16.2
        v = 65.0
        cl_base = 0.4
        aoa_inicial = 5.0
    elif opcion == 2:
        nombre = "Airbus A320"
        peso = 600000.0
        area = 122.6
        v = 130.0
        cl_base = 0.5
        aoa_inicial = 5.0
    elif opcion == 3:
        nombre = "Boeing 747-8"
        peso = 3500000.0
        area = 554.0
        v = 250.0
        cl_base = 0.6
        aoa_inicial = 5.0
    else:
        print("Opción inválida. Debe seleccionar 1, 2 o 3.")
        return

    aoa = aoa_inicial
    estado_final = "Exitoso"

    print("Avión seleccionado:", nombre)
    for segundo in range(1, 9):
        print("Segundo", segundo)
        print("Ángulo de ataque actual:", aoa, "°")

        eleccion_aoa = input("¿Ángulo de ataque: (a)umentar, (d)isminuir o (m)antener? ")

        if eleccion_aoa == "a":
            aoa = aoa + 1.0
            print("El ángulo de ataque aumentó a:", aoa, "°")
        elif eleccion_aoa == "d":
            aoa = aoa - 1.0
            print("El ángulo de ataque disminuyó a:", aoa, "°")
        elif eleccion_aoa == "m":
            print("El ángulo de ataque se mantiene en:", aoa, "°")
        else:
            print("Opción inválida → se mantiene el ángulo de ataque.")

        cl_actual = cl_base + 0.1 * (aoa - aoa_inicial)
        sustentacion = 0.5 * RHO * (v * v) * cl_actual * area

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
        decision_v = input("¿Velocidad: (a)umentar, (d)isminuir o (m)antener? ")

        if decision_v == "a":
            v = v + 10.0
            print("Velocidad aumentó a:", v, "m/s")
        elif decision_v == "d":
            v = v - 10.0
            print("Velocidad disminuyó a:", v, "m/s")
        elif decision_v == "m":
            print("Velocidad se mantiene en:", v, "m/s")
        else:
            print("Opción inválida → se mantiene la velocidad.")

    if estado_final == "Exitoso":
        print("El avión logró atravesar la turbulencia con éxito.")
    else:
        print("El avión no logró superar la turbulencia.")

## Partes a modificar con diccionarios y listas
---
### Antes del diccionario
```
    opcion = int(input("Ingrese opción (1-3): "))

    if opcion == 1:
        nombre = "Cessna 172 Skyhawk"
        peso = 10000.0
        area = 16.2
        v = 65.0
        cl_base = 0.4
        aoa_inicial = 5.0
    elif opcion == 2:
        nombre = "Airbus A320"
        peso = 600000.0
        area = 122.6
        v = 130.0
        cl_base = 0.5
        aoa_inicial = 5.0
    elif opcion == 3:
        nombre = "Boeing 747-8"
        peso = 3500000.0
        area = 554.0
        v = 250.0
        cl_base = 0.6
        aoa_inicial = 5.0
    else:
        print("Opción inválida. Debe seleccionar 1, 2 o 3.")
        return
```

### Después del diccionario 
```
aviones = {
    1: {"nombre": "Cessna 172 Skyhawk", "peso": 10000.0,  "area": 16.2,  "v": 65.0,  "cl_base": 0.4, "aoa_inicial": 5.0},
    2: {"nombre": "Airbus A320",        "peso": 600000.0, "area": 122.6, "v": 130.0, "cl_base": 0.5, "aoa_inicial": 5.0},
    3: {"nombre": "Boeing 747-8",       "peso": 3500000.0,"area": 554.0, "v": 250.0, "cl_base": 0.6, "aoa_inicial": 5.0}
}

opcion = int(input("Ingrese opción (1-3): "))

if opcion in aviones:
    avion = aviones[opcion]
    nombre = avion["nombre"]
    peso = avion["peso"]
    area = avion["area"]
    v = avion["v"]
    cl_base = avion["cl_base"]
    aoa_inicial = avion["aoa_inicial"]
else:
    print("Opción inválida. Debe seleccionar 1, 2 o 3.")
    return
```
**Por qué se implementó este diccionario?**

- Reemplaza los bloques repetitivos if/elif por una estructura centralizada que guarda todos los parámetros de cada avión.

- Hace el código más escalable y limpio, porque si se quiere agregar un nuevo avión, solo se añade otra entrada al diccionario.

- Evita repetir variables y mejora la organización de los datos (cada avión tiene su propio mini diccionario con sus características).

- Permite acceder fácilmente a todos los datos del modelo seleccionado.

----
### Antes de la lista
```
RHO = 1.225

print("=== EJERCICIO 1: ESTABILIDAD EN TURBULENCIA ===")
print("Seleccione un avión:")
print("1. Cessna 172 Skyhawk")
print("2. Airbus A320")
print("3. Boeing 747-8")
```

### Después de la lista

```
RHO = 1.225

texto_inicial = [
    "=== EJERCICIO 1: ESTABILIDAD EN TURBULENCIA ===",
    "Seleccione un avión:",
    "1. Cessna 172 Skyhawk",
    "2. Airbus A320",
    "3. Boeing 747-8"
]

for linea in texto_inicial:
    print(linea)
```

**¿Por qué se implementó esta lista?**

- Permite agrupar todas las líneas de texto que se imprimen al inicio del programa.

- Si se necesita cambiar o agregar texto, solo se modifica la lista, sin duplicar print.

- Hace el código más ordenado y legible.

----
### Antes del diccionario
```
eleccion_aoa = input("¿Ángulo de ataque: (a)umentar, (d)isminuir o (m)antener? ")

if eleccion_aoa == "a":
    aoa = aoa + 1.0
    print("El ángulo de ataque aumentó a:", aoa, "°")
elif eleccion_aoa == "d":
    aoa = aoa - 1.0
    print("El ángulo de ataque disminuyó a:", aoa, "°")
elif eleccion_aoa == "m":
    print("El ángulo de ataque se mantiene en:", aoa, "°")
else:
    print("Opción inválida → se mantiene el ángulo de ataque.")
```

### Después del diccionario 
```
acciones_aoa = {"a": 1.0, "d": -1.0, "m": 0.0}

eleccion_aoa = input("¿Ángulo de ataque: (a)umentar, (d)isminuir o (m)antener? ").strip().lower()

if eleccion_aoa in acciones_aoa:
    delta_aoa = acciones_aoa[eleccion_aoa]
    aoa = aoa + delta_aoa
    if delta_aoa > 0:
        print("El ángulo de ataque aumentó a:", aoa, "°")
    elif delta_aoa < 0:
        print("El ángulo de ataque disminuyó a:", aoa, "°")
    else:
        print("El ángulo de ataque se mantiene en:", aoa, "°")
else:
    print("Opción inválida → se mantiene el ángulo de ataque.")
```

**¿Por qué se implementó este diccionario?**

- El diccionario traduce directamente la entrada del usuario (a, d, m) en un valor numérico de cambio.

- Evita tener múltiples condiciones if/elif y simplifica la lógica.

- Si se desea cambiar el incremento (por ejemplo, +2° en lugar de +1°), se hace en una sola línea.

- Hace que el código sea más legible, compacto y fácil de mantener.

---
### Antes del diccionario 
```
print("Velocidad actual:", v, "m/s")
decision_v = input("¿Velocidad: (a)umentar, (d)isminuir o (m)antener? ")

if decision_v == "a":
    v = v + 10.0
    print("Velocidad aumentó a:", v, "m/s")
elif decision_v == "d":
    v = v - 10.0
    print("Velocidad disminuyó a:", v, "m/s")
elif decision_v == "m":
    print("Velocidad se mantiene en:", v, "m/s")
else:
    print("Opción inválida → se mantiene la velocidad.")
```

### Después del diccionario 
```
print("Velocidad actual:", v, "m/s")
acciones_vel = {"a": 10.0, "d": -10.0, "m": 0.0}

decision_v = input("¿Velocidad: (a)umentar, (d)isminuir o (m)antener? ").strip().lower()

if decision_v in acciones_vel:
    delta_v = acciones_vel[decision_v]
    v = v + delta_v
    if delta_v > 0:
        print("Velocidad aumentó a:", v, "m/s")
    elif delta_v < 0:
        print("Velocidad disminuyó a:", v, "m/s")
    else:
        print("Velocidad se mantiene en:", v, "m/s")
else:
    print("Opción inválida → se mantiene la velocidad.")
```

**¿Por qué se implementó este diccionario?**

- Permite manejar la lógica de cambio de velocidad sin varios if/elif.

- Se puede ajustar el incremento o decremento en un solo lugar (por ejemplo, cambiar +10 a +5).

- Aumenta la claridad del código y reduce la repetición.

- Hace la simulación más flexible si en el futuro se agregan más comandos (por ejemplo, 'r' para reiniciar velocidad).

---
## Código modificado con diccionarios y listas 
```
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

    opcion = int(input("Ingrese opción (1-3): "))

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
        print("Opción inválida. Debe seleccionar 1, 2 o 3.")
```
