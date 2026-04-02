# Encuentra el primer carácter no repetido en un texto

def caracter_no_repetido(texto):
    for letra in texto:
        contador = 0
        for otra_letra in texto:
            if letra == otra_letra:
                contador = contador + 1
        if contador == 1:
            return letra
    return None


print(caracter_no_repetido("abacddbec"))

# Utilizando metodos


def caracter_no_repetido_metodos(texto):
    for letra in texto:
        if texto.count(letra) == 1:
            return letra
    return None


print(caracter_no_repetido_metodos("abacddbec"))
