"""Juego del ahorcado por consola. Ejecutar: python hangman.py"""

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
    vidas = VIDAS

    print("\n=== JUEGO DEL AHORCADO ===")
    print(mostrar_palabra(palabra, usadas))

    while vidas > 0 and not all(c in usadas for c in palabra):
        letra, error = validar_letra(input("\nIngrese una letra: "), usadas)
        if error:
            print(error)
            continue
        usadas.add(letra)

        if letra not in palabra:
            vidas -= 1
            print(f"La letra {letra} no está en la palabra. Vidas: {vidas}")
            print(ETAPAS[VIDAS - vidas - 1])
        else:
            print(f"¡Bien! La letra {letra} está en la palabra. Vidas: {vidas}")

        print(mostrar_palabra(palabra, usadas))
        print("Letras usadas:", " ".join(sorted(usadas)))

    if vidas == 0:
        print(f"\nHas perdido. Vidas: 0. La palabra era: {palabra}")
    else:
        print("\n¡Ganaste!")


def menu():
    while True:
        jugar()
        while True:
            op = input("\n1) Jugar de nuevo  2) Finalizar: ").strip()
            if op in ("1", "2"):
                break
            print("Opción inválida")
        if op == "2":
            print("¡Hasta pronto!")
            break


if __name__ == "__main__":
    menu()
