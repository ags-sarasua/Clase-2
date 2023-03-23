print("Probando Github")

# punto1

def punto1():
    lista1 = [0, 1, 2]
    print("Lista antes de modificarse: ",lista1)
    lista1.clear()
    print("Lista después de modificarse: ",lista1)

    lista2 = [0, 10, 20, 30, 40, 50]
    print("Lista antes de modificarse: ",lista2)
    lista2.pop(1)
    print("Lista después de modificarse: ",lista2)

    print()

    lista2 = [0, 10, 20, 30, 40, 50]
    print("Lista antes de modificarse: ",lista2)
    lista2.insert(1,0)
    print("Lista después de modificarse: ",lista2)

    lista = list("Hola mundo")
    lista.reverse()
    cadena = "".join(lista)
    print(cadena)


# punto 2
# un numero complejo pertenece a un campo ajeno al de los numeros reales. el mismo cuenta con una parte real y una parte imaginaria, compuesta por un numero real multiplicado por la unidad imaginaria representada como i.

def punto2():
    complejo1 = complex(1,2)

# punto 3
def punto3():
    print(id(complejo1))
    complejo1=complex(1,3)
    print(id(complejo1))


# punto 4
def funcioninser(lista,valor,posicion): 
    lista.insert(posicion,valor)
    print(lista)

lista1=["ignacio","come","palomitas"]
valor1="tamaki"
posicion1=1
funcioninser(lista1,valor1,posicion1)



# punto 5
def punto5():
    profe= "Agostina"
    mi_profe= "Agostina"
    print(profe is mi_profe)    ##True


    pro= "Agostina?"
    pro_Agos= "Agostina?"
    print(pro is pro_Agos)       ##False

    a="a"
    b="b"
    print(a is b)      #False

    ver="!"
    ver_mas="!"
    print(ver is ver_mas)     #True


    numero1=120
    numero2=120
    print(numero1 is numero2)      #True


    numero1=12000000
    numero2=12000000
    print(numero1 is numero2)     #False


    #Comun=misma direccion    is compara Ids

# punto 6

help('mutable')

#8
#Realizar una función que reciba como parámetros una lista de elementos y un elemento que se deseaeliminar de la lista y retorne la lista con los elementos eliminados si coinciden con el parámetro que paso elusuario. El id de la lista antes de eliminar elementos ¿Debería ser el mismo id luego de que se eliminenelementos?¿Por qué sí o por qué no


def remove_total(lista, elemento):
    while elemento in lista:
        lista.remove(elemento)
    return lista

listax = [1,2,3,2,4,5,2,6,24]     
listax=remove_total(listax, 2)
print(listax)



#Si, va a ser el mismo ID porque las listas son mutables

# Punto 9

remove_total("Hola", "o")

# punto 10

def probar():
    a = (1, 2, [1, 2, 3])
    a[2].append(4)
    print(a)

probar()

##########3#######

print("Tamaki se la come")
