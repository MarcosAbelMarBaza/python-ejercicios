# Encuentra el segundo número mayor en una lista

def segundo_numero_mayor(lista):
    m = lista[0]
    s = None
    for n in lista[1:]:
        if m < n:
            s = m
            m = n
        elif n != m and (s is None or n > s):
            s = n
    return s


print(segundo_numero_mayor([1, 28, 4, 5, 10, 20, 15, 30, 27]))

# Utilizando metodos


def segundo_numero_mayor_metodos(lista):
    duplicados = set(lista)
    orden = sorted(duplicados, reverse=True)
    if len(orden) < 2:
        s = None
    else:
        s = orden[1]
    return s


print(segundo_numero_mayor_metodos([1, 28, 4, 5, 10, 20, 15, 30, 27]))
