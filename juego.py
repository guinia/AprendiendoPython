import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual



def obtener_palabra(lista_palabras):
    # seleccionar una palabra al azar de la lista de palabras
    palabra = random.choice(palabras)

    while "-" in palabra or "ñ" in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()


def ahorcado():
    print("***************************************")
    print("   Bienvenido al juego del ahorcado   ")
    print("***************************************")
    # obtener una palabra d una lista de palabras validas
    palabra = obtener_palabra(palabras)

    letras_faltantes = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)   #no contiene la ñ

    vidas = 7
    while len(letras_faltantes) > 0 and vidas > 0:
        print(f" Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        # metodo join une todos los elementos del conjunto en una secuencia con el caracter especificado antes del .

        # mostrar estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else "_" for letra in palabra]   #list comprehension
        # mostrar horca
        print(vidas_diccionario_visual[vidas])
        # mostrar palabra
        print(f" Estado de la palabra: {' '.join(palabra_lista)}")

        letra_usuario = input(" Elige una letra: ").upper()

        # si la letra no esta entre las adivinadas se añade al mismo
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # la letra esta en la palabra?
            # si esta, la saco del conjunto de pendientes
            # si no esta saco una vida
            if letra_usuario in letras_faltantes:
                letras_faltantes.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\nLa letra {letra_usuario} no está en la palabra.")
        # si la letra elegida ya habia sido ingresada:
        elif letra_usuario in letras_adivinadas:
            print("\n Ya habias elegido esta, tenes que elegir una nueva letra")
        else:
            print("\n Esta letra no es válida")

    # el juego llega a esta linea cuando se adivino la palabra o se quedo sin vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print("¡PERDISTE!")
        print(f"\nLa palabra era: {palabra}")
    else:
        print(f"¡GANASTE! Adivinaste la palabra: {palabra}")


ahorcado()