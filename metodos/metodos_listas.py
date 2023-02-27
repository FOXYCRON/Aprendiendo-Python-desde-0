# Creando una lista con list()
lista = list(["Hola", "que", "tal", 23, True])
lista2 = list([23, 22, 11, 45, 65, 84, 10])

# Devuelve la cantidad de elementos de una lista
cantidad_elementos = len(lista)

# Agregando elementos a la lista con append
lista.append("ssss")

# Agregando elementos a la lista en un indice espesifico
lista.insert(2, "Toma bro")

# Agregando varios elementos a la lista
lista.extend([True, 2005])

# Eliminando un elemento de la lista (Por su indice)
lista.pop(0) # Con "-1" borramos el ultimo elemento de la lista, y con "-2" nos borra el penultimo y asi sucesivamente, borra los numeros del derecha a izquierda

# Removiendo un elemento de la lista por su valor
lista.remove("Toma bro")

# Eliminando todos los elementos de la lista
#lista.clear()

# Ordenando la lista de mayor a menor (Si usamos reverse=True lo ordena en reversa)
lista2.sort()
# Ejemplo
#lista2.sort(reverse=True)

# Invirtiendo los elementos de una lista
lista2.reverse()

# Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista2.index(10) # Busca el resultado completo

print(elemento_encontrado)