from unittest import result


fruits=[]

# añade nuevos elementos a las colecciones
fruits.append("Kiwi")
fruits.append("Berry")
fruits.append("Melon")

print (fruits)

#ordena alfabeticamente los elementos de la coleccion
fruits.sort()
print(fruits)


#elimina el ultimo elemento de la lista
fruits.pop()
print(fruits)

# inserta elemento en la posicion de la coleccion que le indiquemos
fruits.insert(0, "Apple")
print(fruits)
fruits.insert(1, "Strawberry")
print(fruits)

#elimina elemento de la coleccion por medio del indice que indiquemos
fruits.pop(1)
print(fruits)

#elimina elemento de la coleccion por el valor que le indiquemos
fruits.remove("Apple")
print(fruits)

# -----------Ejemplo Funciones  -------------------------------

def pyramid_sum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks , 0)
        return 0 
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)   # funcion recursiva
        print( blanks, result)
        return result

pyramid_sum(1,4)