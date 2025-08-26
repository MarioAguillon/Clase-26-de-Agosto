#crear una lista animales domesticos
lista=["Caballo","Perro","Gato","Gallina","oveja","Pato","Conejo","Cabra","Burro","gallo"]

lista[5:8]

lista2=["Perro","Oveja","Gallo","cabra"]
print(lista2)

lista3 = lista[0:5]
print(lista3)

print (lista3[:])

print(lista3[::-1])

print(lista[:: 2])

lista [4]="Ornitorrinco"
print(lista)

lista3 [1]="Tigre"
print (lista3)

lista.append("Leon")
print(lista)

lista.insert(2,"Serpiente")
print(lista)

lista3.extend(["Jirafa","Rinoceronte","búfalo"])
print(lista3)

lista2.extend(["Jirafa","Rinoceronte","búfalo"])
print(lista2)

print(lista[:: 2])

print(lista3[:: 2])

print(lista[::-1])

lista.remove("Pato")
print(lista)

lista.pop(3)
print(lista)

lista.clear()
print(lista)

lista=["Caballo","Perro","Gato","Gallina","oveja","Pato","Conejo","Cabra","Burro","gallo"]
print(lista)

for i in lista:
    print(i)

for i in lista3:
    print(i)

    for indice, listas in enumerate(lista):
        print(indice,":",listas)

#saber range

for i in range(len (lista [2:5]) ):
    print(i)


print(len(lista))

print(len(lista[4]))

for i in range(2,6):
    print(lista[i])

varfv="Gato" in lista
print(varfv)

varfv="ternero" in lista
print(varfv)

varfv="gato" in lista
print(varfv)

var2= "aeiouaeiouaaa"
var3=var2.count("a")
print(var3)

var4=lista.index("Gallina")
print(var4)

