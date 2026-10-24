import random
import string

from palabras import PALABRAS
from monigote import ETAPAS

VIDAS = 6


def elegir_palabra():
    """Devuelve una palabra aleatoria de la lista."""
    return random.choice(PALABRAS)


def mostrar_palabra(palabra, usadas):
    """Palabra con _ en las letras aún no adivinadas."""
    return " ".join(c if c in usadas else "_" for c in palabra)


def jugar():
    palabra = elegir_palabra()
    print(mostrar_palabra(palabra, set()))
    entrada = input("Ingrese una letra: ").strip().upper()
    if len(entrada) != 1:
        print("Debe ingresar solo 1 letra")
    else:
        print("Letra recibida:", entrada)

if __name__ == "__main__":
    jugar()
