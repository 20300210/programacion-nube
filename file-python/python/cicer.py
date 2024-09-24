from string import ascii_lowercase, ascii_uppercase
def cifrado_cesar(codig,rotar):
    cifrado=[]
    for c in codig:
        if c in ascii_lowercase:
            letra=ascii_lowercase.index(c)
            nuv_letra=(letra+rotar)%len(ascii_lowercase)
            cifrado.append(ascii_lowercase[nuv_letra])
        elif c in ascii_uppercase:
            letra=ascii_uppercase.index(c)
            nuv_letra=(letra+rotar)%len(ascii_uppercase)
            cifrado.apend(ascii_uppercase[nuv_letra])
        else:
            cifrado.append(c)
            
    return ''.join(cifrado)

codig=input("introduce tu cadigo a cifrar: ")
rotar=int("cantida de rotaciones: ")

print("texto cifado: ",cifrado_cesar)
