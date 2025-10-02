tiempo = [0, 1, 2, 3, 4, 5]
altitud = [0, 100, 300, 800, 1500, 2000]
velocidad = [0, 150, 250, 400, 550, 600]
estado = ["en tierra", "despegue", "ascenso", "ascenso", "ascenso", "crucero"]

print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")

# Calcular velocidad promedio
suma = 0
for v in velocidad:
    suma += v
promedio = suma / len(velocidad)
print(f"Velocidad promedio: {promedio}")

# Imprimir velocidades que superan el promedio
for v in velocidad:
    if v > promedio:
        print(v)
else:
    print("Ninguno supera el promedio")
