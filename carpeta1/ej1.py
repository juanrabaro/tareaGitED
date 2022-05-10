
def lista_dic(lista_diccionarios):
    lista_nueva = []
    lista_provisional = []
    for diccionarios in lista_diccionarios:
        for claves in diccionarios:
            if claves in lista_provisional:
                if claves not in lista_nueva:
                    lista_nueva.append(claves)
            if claves not in lista_provisional:
                lista_provisional.append(claves)
    return lista_nueva


if __name__=="__main__":
    lista_diccionarios = [{"a":1, "b":2}, {"a":3, "b":4}, {"a":5, "f":3}]
    print(lista_dic(lista_diccionarios))
