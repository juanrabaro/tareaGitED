def es_par(numero):
    return numero % 2 == 0

# Carga valores en formato matriz
matriz = [ [ 1, 2, 3],
           [ 1, 2, 3],
           [ 1, 2, 3] ]

# Creamos una nueva matriz (ojo, solo la lista inicial)
# Será una matriz cuando vayamos añadiéndole listas
pares = [ ]

# Muestra la matriz, pero a la vez crea una nueva matriz con el resultado de la
# función es_par aplicado a cada valor de la matriz original
for fila in matriz:
    nueva_fila = []
    for celda in fila:
        print(celda, end=" ")
        nueva_fila.append(es_par(celda))
    pares.append(nueva_fila)
    print()

# Muestra la matriz por consola
for fila in pares:
    for celda in fila:
        print(celda, end=" ")
    print()



