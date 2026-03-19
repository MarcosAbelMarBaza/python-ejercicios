# Filtrar numeros pares de una lista de enteros


def numeros_pares_basico(lista):
    nueva_lista = []
    for n in lista:
        if n % 2 == 0:
            nueva_lista = nueva_lista + [n]
    return nueva_lista


print(numeros_pares_basico([1, 2, 3, 4, 5, 6]))

# Utilizando metodos


def numeros_pares_metodos(lista):
    nueva_lista = []
    for n in lista:
        if n % 2 == 0:
            nueva_lista.append(n)
    return nueva_lista


print(numeros_pares_metodos([11, 20, 33, 46, 55, 66]))
