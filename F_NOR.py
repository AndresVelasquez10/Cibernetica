def mcp_nor(x1, x2):
    # Pesos y umbral para la compuerta NOR
    pesos = [-1, -1]
    umbral = -1
    # Calcula la suma ponderada de las entradas
    suma = x1 * pesos[0] + x2 * pesos[1]
    # Devuelve 1 si la suma es mayor o igual al umbral, si no devuelve 0
    return int(suma >= umbral)

# Imprime la tabla de verdad de la compuerta NOR
print("Entrada A | Entrada B | Salida (A NOR B)")
for entrada_a in [0, 1]:
    for entrada_b in [0, 1]:
        resultado = mcp_nor(entrada_a, entrada_b)
        print(f"    {entrada_a}     |     {entrada_b}     |        {resultado}")