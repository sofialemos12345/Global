# Mutantes
Es un proyecto de entrada a Mercado Libre.

# Datos

Nombre y apellido: Sofia Lemos

Legajo: 51583

Email: sofialemos091@gmail.com

# Objetivo del Código:

Este código que he desarrollado tiene como propósito principal identificar si una matriz de ADN, proporcionada por el usuario, contiene secuencias genéticas mutantes

# ¿Cómo lo hice?

En la entrada use un bucle para pedir al usuario que ingrese cada fila de ADN. Se espera que cada fila tenga exactamente 6 caracteres, y estos caracteres deben ser válidos (A, T, C, G). Si la entrada no cumple con estos requisitos, emito un mensaje de error y salgo de la función.Las filas de ADN válidas se almacenan en 'entrada', y cada fila se convierte a mayúsculas para garantizar uniformidad en el análisis.


def es_mutante():
    entrada = []

    for _ in range(6):
        fila = input("Ingrese una fila de ADN (6 caracteres): ")
        if len(fila) != 6 or not all(base in "ATCG" for base in fila):
            print("La fila debe contener exactamente 6 caracteres válidos (A, T, C, G). Intenta de nuevo.")
            return
        entrada.append(fila.upper())
        
A continuación, defino una lista de secuencias mutantes que se buscarán en la matriz: ["AAAA", "TTTT", "CCCC", "GGGG"]. Luego, inicializo una lista llamada 'resultados' con las filas de ADN ingresadas. Por ejemplo, si el usuario ha ingresado dos filas 'ATCGAT' y 'TGCAGT', la lista 'resultados' se verá así: ['ATCGAT', 'TGCAGT'].

      adn = ["AAAA", "TTTT", "CCCC", "GGGG"]
      resultados = []

Posteriormente, extiendo la lista de resultados agregando las secuencias obtenidas al transponer la matriz (usando la función 'agregar_vertical') y las secuencias de las diagonales y contradiagonales (con la función 'agregar_diagonales_contradiagonales'). 
 De esta manera, 'resultados' incluye una representación completa de todas las posibles secuencias en diversas direcciones.


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


Utilizo una expresión generadora para contar cuántas secuencias mutantes hay en 'resultados'. Si encuentro más de una, concluyo que la matriz es mutante. Finalmente, presento la matriz ingresada por el usuario y comunico si se detectaron secuencias de ADN mutante o no.
   
   es_mutante = sum(1 for secuencia in resultados if any(subcadena in secuencia for subcadena in adn)) > 1

    print("Matriz ingresada: ")
    for fila in entrada:
        print(fila)

    if es_mutante:
        print("Es mutante.")
    else:
        print("No es mutante.")
        

En resumen, mi código implementa un enfoque meticuloso para determinar la presencia de mutaciones en una matriz de ADN, considerando todas las posibles orientaciones de las secuencias.

# Ejemplo

1 

  CATCAT

  GCTATC
  
  CCTGAT
  
  AGGCCT
  
  GTCGTT
  
  GCTATC

NO ES MUTANTE


2 

  AAAGAT

  GGGGTT
  
  CCTTGG
  
  CTCTCT
  
  GTAGTA
  
  CGTTTT

ES MUTANTE



