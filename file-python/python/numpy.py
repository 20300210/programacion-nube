import numpy as np
# sample_list=[1,2,3]
# np.array(sample_list)

# my_matriz=[[1,2,3],[4,5,6],[7,8,9]]
# np.array(my_matriz)
# print(my_matriz)

# np.arange(1,11,2)

# np.linspace(0,1,10)

# np.eye(1)

# np.eye(2)

# np.eye(50)

# numero_entero=np.random.randint(0,11)
# print("numeros enteros aleatorios: ", numero_entero)

# numero_decimal=np.random.rand()
# print("numero decimal aleatorio: ",numero_decimal)

# matriz_enteros=np.random.randint(0,101,size=(3,3))
# print("matriz de enteros aleatorios:\n",matriz_enteros)

# from numpy import random as r
# print(r.choice(['andres','juan','pedro','mateo'],size=r.choice([1,2],p=[0.1,0.9]),p=[0.5,0.2,0.2,0.1],replace=False))

# a=np.array([34,25,7])
# print(type(a))
# print(a.shape)
# print(a[0],a[1],a[2])

# matriz=np.zeros((3,3))
# print(matriz)

# b=np.ones((1,2))
# print(b)

# c=np.full((2,2),7)
# print(c)

# matriz=np.zeros((3,3))
# print(matriz)

# b=np.ones((1,2))
# print(b)

# c=np.full((2,2),7)
# print(c)
# d=np.eye(2)
# print(d)
# e=np.random.random((2,2))
# print(e)

a=np.array([[1,2,3],[5,6,7],[9,10,11]])
print(a)
b=a[:2,1:3]
print(b)
print(np.fliprl(a))
print(a[0,1])
b[0,0]=77
print(a[0,1])
a=np.array([[1,2,3,4],[5,6,7,8,],[9,10,11,12]])
row_r1=a[1,:]
print(row_r1)
row_r2=a[1:2,:]
print(row_r2)