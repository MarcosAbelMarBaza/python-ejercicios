# Cuenta la frecuencia de cada elemento en una lista

def frecuencia(lista):
    diccionario = {}
    for numero in lista:
        if numero in diccionario:
            diccionario[numero] = diccionario[numero] + 1
        else:
            diccionario[numero] = 1
    return diccionario


print(frecuencia([1, 2, 2, 3]))


# Utilizando metodos


def frecuencia_metodo(lista):
    diccionario = {}
    for numero in lista:
        diccionario[numero] = diccionario.get(numero, 0) + 1
    return diccionario


print(frecuencia_metodo([1, 2, 2, 3]))
