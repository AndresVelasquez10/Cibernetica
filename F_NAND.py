def puerta_nand(a, b):
    # Pesos para las entradas
    w1, w2 = -1, -1
    # Umbral de activación
    umbral = -1.5

    # Suma ponderada de las entradas
    suma = a * w1 + b * w2

    # Si la suma supera el umbral, retorna 1 si no, retorna 0
    if suma >= umbral:
        return 1
    else:
        return 0

# Lista de todas las combinaciones posibles de entradas binarias
entradas = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("A B | Salida (A NAND B)")
# Prueba la función con todas las combinaciones y muestra los resultados
for a, b in entradas:
    salida = puerta_nand(a, b)
    print(f"{a} {b} | {salida}")