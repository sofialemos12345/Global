def es_mutante():
    entrada = []
    for _ in range(6):
        fila = input("Ingrese una fila de ADN (6 caracteres): ")
        if len(fila) != 6:
            print("La fila debe contener exactamente 6 caracteres. Intenta de nuevo.")
            return
        entrada.append(fila.upper())

    adn = ["AAAA", "TTTT", "CCCC", "GGGG"]
    resultados = []

    resultados.extend(entrada)
    agregar_vertical(entrada, resultados)
    agregar_diagonales_contradiagonales(entrada, resultados)

    es_mutante = sum(1 for secuencia in resultados if any(subcadena in secuencia for subcadena in adn)) > 1

    print("Matriz ingresada: ")
    for fila in entrada:
        print(fila)

    if es_mutante:
        print("Es mutante.")
    else:
        print("No es mutante.")

def agregar_vertical(entrada, resultados):
    entrada_vertical = [''.join(x) for x in zip(*entrada)]
    resultados.extend(entrada_vertical)

def agregar_diagonales_contradiagonales(entrada, resultados):
    diagonal = [''.join(entrada[i][j] for i, j in enumerate(range(len(entrada))))
                for j in range(len(entrada[0]))]

    contradiagonal = [''.join(entrada[i][j] for i, j in enumerate(range(len(entrada) - 1, -1, -1)))
                for j in range(len(entrada[0]))]

    resultados.extend(diagonal)
    resultados.extend(contradiagonal)

es_mutante()
