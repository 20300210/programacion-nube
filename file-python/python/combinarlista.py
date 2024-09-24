def problema2(lst1,lst2):
    lst_final=[]
    for i in range(0,min(len(lst1),len(lst2))):
        lst_final.append(lst1[i])
        lst_final.append(lst2[i])
    return lst_final
resultado=problema2([1,3,5,7,9], [2,4,6,8,0])
print(resultado)