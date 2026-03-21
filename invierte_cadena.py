# Invierte una cadena de texto

def invertir_cadena(texto):
    resultado = ""
    for letra in texto:
        resultado = letra + resultado
    return resultado


print(invertir_cadena("Hola"))

# Utilizando metodos


def invertir_cadena_metodos(texto_metodo):
    return "".join(reversed(texto_metodo))


print(invertir_cadena_metodos("Hola Mundo"))
