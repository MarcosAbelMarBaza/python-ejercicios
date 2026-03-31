# Contador de vocales en un texto
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def contador_vocales(texto):
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador = contador + 1
    return contador


print(contador_vocales("Hola mundo"))

# Utilizando metodos

vocales_metodos = ["a", "e", "i", "o", "u"]


def contador_vocales_metodos(texto):
    texto_minuscula = texto.lower()
    contador = 0
    for letra in vocales_metodos:
        contador = contador + texto_minuscula.count(letra)
    return contador


print(contador_vocales_metodos("HOlA mundo"))
