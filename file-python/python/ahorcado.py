import random

def obtener_palabra():
    palabras = ["python", "programacion", "codigo", "computadora", "desarrollo"]
    return random.choice(palabras)

def mostrar_muñeco(intentos):
    muñeco = [
       " ________     ",
        "|        |    ",
        "|        {}    ",
        "|       /|\\  ",
        "|____   / \\  ",
        
            
]
    for i in range(intentos):
        print(muñeco[i])

def jugar_ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = ["_"] * len(palabra)
    intentos = 5
    letras_intentadas = []

    print("Bienvenido al juego del ahorcado!")
    print("Adivina la palabra:", " ".join(letras_adivinadas))

    while intentos > 0 and "_" in letras_adivinadas:
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_intentadas:
            print("Ya has intentado esta letra antes.")
            continue

        letras_intentadas.append(letra)

        if letra in palabra:
            print("¡Bien hecho! La letra '{}' está en la palabra.".format(letra))
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    letras_adivinadas[i] = letra
        else:
            print("¡Incorrecto! La letra '{}' no está en la palabra.".format(letra))
            intentos -= 1

        print("Letras intentadas:", " ".join(letras_intentadas))
        print("Intentos restantes:", intentos)
        print("Palabra:", " ".join(letras_adivinadas))
        mostrar_muñeco(5 - intentos)

    if "_" not in letras_adivinadas:
        print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
    else:
        print("Lo siento, te has quedado sin intentos. La palabra era '{}'.".format(palabra))

if __name__ == "__main__":
    jugar_ahorcado()