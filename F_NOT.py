def puerta_not(a):
    # Peso negativo para invertir la entrada
    peso = -1
    # Umbral para la activación
    umbral = 0

    # Calcula la suma ponderada
    resultado = a * peso

    # Si la suma es mayor o igual al umbral, retorna 1; de lo contrario, retorna 0
    if resultado >= umbral:
        return 1
    else:
        return 0

# Lista de posibles entradas para la puerta NOT
valores_entrada = [0, 1]

print("A | Salida (NOT A)")
# Itera sobre cada entrada y muestra el resultado de la puerta NOT
for valor in valores_entrada:
    salida = puerta_not(valor)
    print(f"{valor} | {salida}")