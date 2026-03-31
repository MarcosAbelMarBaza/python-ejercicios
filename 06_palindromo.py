# Verifica si un texto es un palíndromo ignorando mayúsculas y espacios

def palindromo(texto):
    texto = texto.lower()
    palabra = ""
    texto_sin_espacio = ""
    for letra in texto:
        if letra != " ":
            texto_sin_espacio = texto_sin_espacio + letra

    for letra in texto_sin_espacio:
        palabra = letra + palabra
    return palabra == texto_sin_espacio


print(palindromo("anita lava la tina"))

# utiliza slicing para invertir la cadena


def palindromo_slicing(texto):
    texto = texto.lower()
    texto_sin_espacio = ""
    for letra in texto:
        if letra != " ":
            texto_sin_espacio = texto_sin_espacio + letra

    texto_invertido = texto_sin_espacio[::-1]

    return texto_sin_espacio == texto_invertido


print(palindromo_slicing("anita lava la tina"))
