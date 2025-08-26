def or_gate(a, b):
    # Definimos los pesos y el umbral
    w_a, w_b = 1, 1
    threshold = 1
    # Calculamos la suma ponderada de las entradas
    total = a * w_a + b * w_b
    # Si la suma es mayor o igual al umbral, retorna 1 si no 0
    return int(total >= threshold)

# Imprimimos la tabla de verdad de la compuerta OR
print("Entrada A | Entrada B | Salida (A OR B)")
for entrada_a in [0, 1]:
    for entrada_b in [0, 1]:
        resultado = or_gate(entrada_a, entrada_b)
        print(f"    {entrada_a}     |     {entrada_b}     |       {resultado}")