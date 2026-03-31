# Encuentra el número mayor en una lista

def numero_mayor(lista):
    m = lista[0]
    for n in lista[1:]:
        if m < n:
            m = n
    return m


print(numero_mayor([3, 7, 2, 9, 5]))

# Utilizando metodos


def numero_mayor_metodo(lista_metodo):
    return max(lista_metodo)


print(numero_mayor_metodo([3, 7, 2, 9, 5]))
