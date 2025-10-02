# Ejercicio 1

def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada

# - Objetos mutables (listas, diccionarios, conjuntos) se modifican directamente,
##  los cambios hechos en una función afectan la variable original.
# - Objetos inmutables (enteros, flotantes, strings, tuplas) no se modifican,
##   dentro de la función se crea una copia y la variable original no cambia.
