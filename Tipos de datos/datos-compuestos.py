 # Creando una lista (Se pueden modificar)
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]

 # Creando una tupla (No se pueden modificar)
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)

# Esto es valido
lista[3] = "Maquinola"

# Esto no
#tupla[3] = "Maquinola"

# Creando un conjunto (set) (No se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85}

#print(conjunto)

# print(conjunto[3]) -> no puede acceder al elemento

# Creando un diccionario (dict) (La estructura es key : value y separamos con comas)
diccionario = {
 #  "clave"  : "valor",
    "nombre" : "Irvin Adrian",
    "canal" : "Foxycron",
    "esta_feliz" : True,
    "dato_duplicado" : "Foxycron"
}

print(diccionario['canal'])