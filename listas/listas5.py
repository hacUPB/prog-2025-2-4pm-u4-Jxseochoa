# Registro de temperaturas del motor durante un vuelo
temperaturas_motor = [120, 350, 380, 375, 390, 400, 405, 390, 385, 370]

# Añadir nueva lectura
temperaturas_motor.append(360)

# Encontrar temperatura máxima
temp_max = max(temperaturas_motor)
print(f"Temperatura máxima: {temp_max}°C")

# Encontrar posición de la temperatura máxima
pos_max = temperaturas_motor.index(temp_max)
print(f"Temperatura máxima alcanzada en la lectura #{pos_max+1}")

# Ordenar para análisis
temperaturas_ordenadas = sorted(temperaturas_motor)  # No modifica la original
print(f"Temperaturas ordenadas: {temperaturas_ordenadas}")

# Modificar la lista original
temperaturas_motor.sort(reverse=True)  # Orden descendente
print(f"Temperaturas (mayor a menor): {temperaturas_motor}")
