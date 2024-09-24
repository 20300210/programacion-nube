import random
def clave_binaria(longitud):
    bts=[random.choice(['0','1'])for _ in range(longitud)]
    clave=''.join(bts)
    return clave
def obtener_clave_binaria():
    while True:
        try:
            longitud=int(input('longitud de la clave'))
            if longitud <= 0:
                print("error, ingrese el numero positivo")
            else:
                return longitud
        except ValueError:
            print('ingrese un numero entero valido')
longitud_clave=obtener_clave_binaria()
clave_generada= clave_binaria(longitud_clave)
print(f'clave binaria generada: {clave_generada}')