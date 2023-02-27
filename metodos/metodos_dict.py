diccionario  = {
#   "keys": "valor"
    "Nombre": "Irvin",
    "Alias": "¿?",
    "Edad":  17
}

# Nos devuelve un objeto dict_item
# Devuelve las claves (Tambien nos sirve para iterar)
claves = diccionario.keys()

# Obteniendo un elemento con get() (No me lanza una excepción y si no encuentra el programa continua)
# Devuelve el valor de una clave
claves = diccionario.get("Edad")

# Eliminando todo del diccionario
#diccionario.clear()

# Eliminando un elemento del diccionario
diccionario.pop("Nombre") # Para borrar mas elementos ponerlos separados por ","

# Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)