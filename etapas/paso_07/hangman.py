import random
import string

from palabras import PALABRAS
from monigote import ETAPAS

VIDAS = 6


def elegir_palabra():
    """Devuelve una palabra aleatoria de la lista."""
    return random.choice(PALABRAS)


def validar_letra(entrada, usadas):
    """Devuelve (letra, None) si es válida o (None, mensaje_de_error)."""
    entrada = entrada.strip().upper()
    if len(entrada) != 1:
        return None, "Debe ingresar solo 1 letra"
    if entrada not in string.ascii_uppercase:
        return None, "Debe ingresar una letra entre A y Z"
    if entrada in usadas:
        return None, "Ya ha utilizado la letra"
    return entrada, None


def mostrar_palabra(palabra, usadas):
    """Palabra con _ en las letras aún no adivinadas."""
    return " ".join(c if c in usadas else "_" for c in palabra)


def jugar():
    palabra = elegir_palabra()
    usadas = set()
    print(mostrar_palabra(palabra, usadas))
    while True:
        letra, error = validar_letra(input("\nIngrese una letra: "), usadas)
        if error:
            print(error)
            continue
        usadas.add(letra)
        print("Letras usadas:", " ".join(sorted(usadas)))

if __name__ == "__main__":
    jugar()
