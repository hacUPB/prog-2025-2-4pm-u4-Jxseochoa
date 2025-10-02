#**Ejercicio 3: Análisis de trayectoria**

## Desarrolle una función que analice una trayectoria de vuelo y detecte desviaciones significativas del rumbo planeado.

def analizar_trayectoria(rumbo_planeado, rumbo_real, umbral_desviacion=5):
    desviaciones = []
    i = 1
    for rp, rr in zip(rumbo_planeado, rumbo_real):
        diferencia = rr - rp
        if diferencia < 0:
            diferencia = -diferencia
        if diferencia > umbral_desviacion:
            desviaciones.append(i)
        i += 1
    return desviaciones


planeado = [45, 45, 45, 90, 90, 90, 180, 180, 225, 225, 270]
real     = [43, 47, 48, 86, 91, 95, 183, 176, 222, 230, 265]

print(analizar_trayectoria(planeado, real, 5))

