# Agrupa palabras en un diccionario según su longitud

def agrupar_palabras(palabras):
    diccionario = {}
    for palabra in palabras:
        contador = 0
        for letra in palabra:
            contador = contador + 1
        if contador in diccionario:
            diccionario[contador] = diccionario[contador] + [palabra]
        else:
            diccionario[contador] = [palabra]
    return diccionario


print(agrupar_palabras(["hola", "sol", "adios", "luz"]))


# Utilizando metodos


def agrupar_palabras_metodos(palabras):
    diccionario = {}
    for palabra in palabras:
        contador = 0
        for letra in palabra:
            contador = contador + 1
        diccionario.setdefault(contador, [])
        diccionario[contador].append(palabra)
    return diccionario


print(agrupar_palabras_metodos(["hola", "sol", "adios", "luz"]))
