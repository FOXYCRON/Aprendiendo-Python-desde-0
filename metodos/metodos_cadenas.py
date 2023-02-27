cadena = "Hola,soy,alguien"
cadena1 = "Hola soy"
cadena2 = "Hola que tal maquinola"

# METODOS

# Estructura
#           dato.metodo()

# Convierte a mayuscula
resultado = cadena1.upper()

# Convierte a minuscula
resultado1 = cadena1.lower()

# Convierte la primer letra mayuscula
resultado2 = cadena1.capitalize()

# Buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1
busqueda_find = cadena1.find("Hola")

# Buscamos una cadena en otra cadena, si no hay coincidencia lanza una exepción
busqueda_index = cadena1.index("Hola")

# Si es numerico, devolvemos true, sino  devolvemos false
es_numerico = cadena1.isnumeric()

# Si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()


# Contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("o") # Si no se encuentra ninguna letra devolvera 0

# Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

# Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("Hola")

# Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("soy")

# Reemplaza un pedazo de la cadena, por otra
cadena_nueva = cadena1.replace("la", "lo")

# Separar cadenas con la cadena que le pasemos
cadena_separada = cadena.split(",")
#print(type(cadena_separada))


print(cadena_separada)