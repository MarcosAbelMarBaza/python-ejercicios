# Elimina duplicados de una lista manteniendo el orden original

def duplicados(lista):
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista = nueva_lista + [elemento]
    return nueva_lista


print(duplicados([1, 2, 2, 3, 4, 3, 5]))

# Usando Metodos


def duplicados_metodos(lista):
    nueva_lista = list(dict.fromkeys(lista))
    return nueva_lista


print(duplicados_metodos([1, 2, 2, 3, 4, 3, 5]))
