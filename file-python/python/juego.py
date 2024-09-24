import random
def lst():
    lst=["piedra","papel","tigera"]
    return random.choice(lst)
print("bienvenido al juego piedra, papel o tigera")
palabra=input("digite su opcion: ")
if palabra==lst():
    print ("opcion aleatoria:",lst())
    print("empate")
elif palabra=="piedra" and lst()=="papel":
    print ("opcion aleatoria:",lst())
    print("perdiste")
elif palabra=="piedra" and lst()=="tigera":
    print ("opcion aleatoria:",lst())
    print("ganaste")
elif palabra=="papel" and lst()=="piedra":
    print ("opcion aleatoria:",lst())
    print("ganaste")
elif palabra=="papel" and lst()=="tigera":
    print ("opcion aleatoria:",lst())
    print("perdiste")
elif palabra=="tigera" and lst()=="piedra":
    print ("opcion aleatoria:",lst())
    print("perdiste")
elif palabra=="tigera" and lst()=="papel":
    print ("opcion aleatoria:",lst())
    print("ganaste")