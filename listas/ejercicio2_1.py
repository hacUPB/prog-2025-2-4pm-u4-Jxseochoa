# **Ejercicio 1: Análisis de eficiencia de combustible**

##Desarrolle una función que calcule la eficiencia de combustible de una aeronave a lo largo de diferentes etapas de vuelo.

def analizar_eficiencia(distancias, combustibles):
    eficiencias = []
    for d, c in zip(distancias, combustibles):
        eficiencia = d / c
        eficiencias.append(eficiencia)

    max_eficiencia = eficiencias[0]
    min_eficiencia = eficiencias[0]
    tramo_max = 1
    tramo_min = 1

    tramo = 1
    for e in eficiencias:
        if e > max_eficiencia:
            max_eficiencia = e
            tramo_max = tramo
        if e < min_eficiencia:
            min_eficiencia = e
            tramo_min = tramo
        tramo += 1

    suma = 0
    contador = 0
    for e in eficiencias:
        suma += e
        contador += 1
    promedio = suma / contador

    return [eficiencias, [tramo_max, max_eficiencia], [tramo_min, min_eficiencia], [promedio]]


distancias = [800, 1200, 1000, 750]
combustibles = [2400, 3000, 2800, 2000]

print(analizar_eficiencia(distancias, combustibles))
