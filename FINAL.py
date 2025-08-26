
# Definición de la función MCP (Modelo de Celda Perceptrón)
# Recibe los pesos, el umbral y las entradas, retorna 1 si la suma ponderada supera el umbral, 0 en caso contrario
def mcp(weights, threshold, inputs):
    total = sum(w * x for w, x in zip(weights, inputs))
    return int(total >= threshold)

# Funciones lógicas básicas usando el perceptrón
def AND(x, y):    # AND lógico: ambos deben ser 1
    return mcp([1, 1], 2, [x, y])

def OR(x, y):     # Alguno debe de ser 1|
    return mcp([1, 1], 1, [x, y])

def NAND(x, y):   # NAND negacion con el AND
    return mcp([-1, -1], -1, [x, y])


def XOR(x, y):    # XOR pasa si los valores son diferentes
    return AND(OR(x, y), NAND(x, y))

def XNOR(x, y):   # XNOR lógico: verdadero si los valores son iguales
    return NAND(XOR(x, y), XOR(x, y)) # NOT(XOR)

# Imprime la tabla de verdad de las funciones 
print("A B | AND OR NAND XOR XNOR")
for a in [0, 1]:
    for b in [0, 1]:
        resultado = [AND(a, b), OR(a, b), NAND(a, b), XOR(a, b), XNOR(a, b)]
        print(f"{a} {b} | {' '.join(str(r) for r in resultado)}")