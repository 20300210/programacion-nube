# def cifrado_cesar(texto, rotaciones):
#     resultado = ""
#     for caracter in texto:
#         if caracter.isalpha():
#             # Determinar si es mayúscula o minúscula
#             alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if caracter.isupper() else "abcdefghijklmnopqrstuvwxyz"
#             indice = alfabeto.index(caracter)
#             # Realizar la rotación
#             nuevo_indice = (indice + rotaciones) % len(alfabeto)
#             nuevo_caracter = alfabeto[nuevo_indice]
#             resultado += nuevo_caracter
#         else:
#             # Conservar caracteres no alfabéticos
#             resultado += caracter
#     return resultado

# # Ejemplo de uso
# mensaje_original = "Hola, mundo!"
# rotaciones = 3
# mensaje_cifrado = cifrado_cesar(mensaje_original, rotaciones)
# print("Mensaje cifrado:", mensaje_cifrado)

# def cifrado_cesar_ascii(mensaje, distancia):
#     cifrado = ""
#     for char in mensaje:
#         valor = ord(char) + distancia
#         cifrado += chr(valor % 128)  # Usamos 128 para ASCII
#     return cifrado

# # Ejemplo de uso
# mensaje_original = "Hola, mundo!"
# rotaciones = 3
# mensaje_cifrado = cifrado_cesar_ascii(mensaje_original, rotaciones)
# print("Mensaje cifrado:", mensaje_cifrado)

# ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def cifrado_cesar(texto, desplazamiento):
#     cifrado = ""
#     for c in texto:
#         if c.isalpha():
#             cifrado += ABC[(ABC.index(c) + desplazamiento) % len(ABC)]
#         else:
#             cifrado += c
#     return cifrado

# # Ejemplo de uso
# mensaje_original = "Hola, mundo!"
# rotaciones = 3
# mensaje_cifrado = cifrado_cesar(mensaje_original, rotaciones)
# print("Mensaje cifrado:", mensaje_cifrado)

# def cifrado_cesar(texto, rotaciones):
#     resultado = ""
#     for caracter in texto:
#         if caracter.isalpha():
#             # Determinar si es mayúscula o minúscula
#             alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if caracter.isupper() else "abcdefghijklmnopqrstuvwxyz"
#             indice = alfabeto.index(caracter)
#             # Realizar la rotación
#             nuevo_indice = (indice + rotaciones) % len(alfabeto)
#             nuevo_caracter = alfabeto[nuevo_indice]
#             resultado += nuevo_caracter
#         else:
#             # Conservar caracteres no alfabéticos
#             resultado += caracter
#     return resultado

# # Solicitar entrada al usuario
# mensaje_original = input("Ingresa el mensaje a cifrar: ")
# rotaciones = int(input("Ingresa el número de rotaciones: "))
# mensaje_cifrado = cifrado_cesar(mensaje_original, rotaciones)
# print("Mensaje cifrado:", mensaje_cifrado)

# def cifrado_cesar(rotaciones):
#     mensaje_original = input("Ingresa el mensaje a cifrar: ")
#     resultado = ""
#     for caracter in mensaje_original:
#         if caracter.isalpha():
#             # Determinar si es mayúscula o minúscula
#             alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if caracter.isupper() else "abcdefghijklmnopqrstuvwxyz"
#             indice = alfabeto.index(caracter)
#             # Realizar la rotación
#             nuevo_indice = (indice + rotaciones) % len(alfabeto)
#             nuevo_caracter = alfabeto[nuevo_indice]
#             resultado += nuevo_caracter
#         else:
#             # Conservar caracteres no alfabéticos
#             resultado += caracter
#     return resultado

# # Solicitar número de rotaciones al usuario
# rotaciones = int(input("Ingresa el número de rotaciones: "))
# mensaje_cifrado = cifrado_cesar(rotaciones)
# print("Mensaje cifrado:", mensaje_cifrado)

# def cifrado_cesar(rotaciones):
#     mensaje_original = "Hola, mundo!"  # Puedes cambiar esto si deseas
#     resultado = ""
#     for caracter in mensaje_original:
#         if caracter.isalpha():
#             # Determinar si es mayúscula o minúscula
#             alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if caracter.isupper() else "abcdefghijklmnopqrstuvwxyz"
#             indice = alfabeto.index(caracter)
#             # Realizar la rotación
#             nuevo_indice = (indice + rotaciones) % len(alfabeto)
#             nuevo_caracter = alfabeto[nuevo_indice]
#             resultado += nuevo_caracter
#         else:
#             # Conservar caracteres no alfabéticos
#             resultado += caracter
#     return resultado

# # Solicitar número de rotaciones al usuario
# rotaciones = int(input("Ingresa el número de rotaciones: "))
# mensaje_cifrado = cifrado_cesar(rotaciones)
# print("Mensaje cifrado:", mensaje_cifrado)

# def cifrado_cesar(rotaciones):
#     resultado = ""
#     alfabeto = "abcdefghijklmnopqrstuvwxyz"
#     for caracter in alfabeto:
#         indice = alfabeto.index(caracter)
#         # Realizar la rotación
#         nuevo_indice = (indice + rotaciones) % len(alfabeto)
#         nuevo_caracter = alfabeto[nuevo_indice]
#         resultado += nuevo_caracter
#     return resultado

# # Solicitar número de rotaciones al usuario
# rotaciones = int(input("Ingresa el número de rotaciones: "))
# mensaje_cifrado = cifrado_cesar(rotaciones)
# print("Mensaje cifrado:", mensaje_cifrado)

def cifrado_cesar(rotaciones):
    resultado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for caracter in alfabeto:
        indice = alfabeto.index(caracter)
        # Realizar la rotación
        nuevo_indice = (indice + rotaciones) % len(alfabeto)
        nuevo_caracter = alfabeto[nuevo_indice]
        resultado += nuevo_caracter
    return resultado

# Solicitar número de rotaciones al usuario
rotaciones = int(input("Ingresa el número de rotaciones: "))
mensaje_cifrado = cifrado_cesar(rotaciones)
print("Mensaje cifrado:", mensaje_cifrado)
