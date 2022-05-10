
def orden(num):
    num = str(num)
    primer_digito = num[0]
    segundo_digito = num[1]
    tercer_digito = num[2]
    primer_digito = int(primer_digito)
    segundo_digito = int(segundo_digito)
    tercer_digito = int(tercer_digito)

    if primer_digito == segundo_digito-1 == tercer_digito-2:
        return True
    if tercer_digito == segundo_digito-1 == primer_digito-2:
        return True
    else: return False


def suma(num):
    num = str(num)
    primer_digito = num[0]
    segundo_digito = num[1]
    tercer_digito = num[2]
    primer_digito = int(primer_digito)
    segundo_digito = int(segundo_digito)
    tercer_digito = int(tercer_digito)

    if primer_digito + segundo_digito == tercer_digito:
        return True
    if primer_digito + tercer_digito == segundo_digito:
        return True
    if tercer_digito + segundo_digito == primer_digito:
        return True
    else: return False


def impar(num):
    num = str(num)
    primer_digito = num[0]
    segundo_digito = num[1]
    tercer_digito = num[2]
    primer_digito = int(primer_digito)
    segundo_digito = int(segundo_digito)
    tercer_digito = int(tercer_digito)
    num = int(num)

    if (num % 2 != 0) and ((primer_digito + segundo_digito + tercer_digito) % 3 == 0):
        return True
    else: return False


def matriz_cambiada(matriz):
    if orden(matriz) and suma(matriz) and impar(matriz):
        return True
    else:
        return False




if __name__=="__main__":
    matriz = [[123, 321, 242],
              [523, 837, 102],
              [342, 756, 123]]


    matriz_nueva = []

    for fila in matriz:
        nueva_fila = []
        for celda in fila:

            nueva_fila.append(matriz_cambiada(celda))
        matriz_nueva.append(nueva_fila)


    # Muestra la matriz por consola
    for fila in matriz_nueva:
        for celda in fila:
            print(celda, end=", ")
        print()