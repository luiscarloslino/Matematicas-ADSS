# Mostraremos como interactua Python con archivos externos
# open(name,[mode])
# Opciones para [mode]
# r - read the file (default mode if mode is omitted).
# w - write over the file, replacing the content of the file.
# a - append to the file.
archivo = open("marca_autos_grupo1.txt", "r")
for item in archivo:
    print(item)  # Muestra el contenido del archivo dejando linea entre ellos
archivo.close()

print('--------------------------', '\n')

archivo = open("marca_autos_grupo1.txt", "r")
for item in archivo:
    item = item.strip()
    print(item)  # Muestra el contenido del archivo sin dejar linea entre ellos
archivo.close()

# Copiando el contenido del archivo en una lista
print('--------------------------', '\n')
lista_autos = []
archivo = open('marca_autos_grupo1.txt', 'r')
for item in archivo:
    item = item.strip()
    lista_autos.append(item)
archivo.close()
print(lista_autos)

print('--------------------------', '\n')
