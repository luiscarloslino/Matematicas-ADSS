my_string = "Hola mundo"

print(my_string.split())  # Separa la informacion en una lista basado en espacio
# Separa la informacion en una lista basado en la letra o
print(my_string.split('o'))
print(my_string.splitlines())  # Hace que toda la informacion este en una lista
print(my_string.splitlines(), 'presente')
# Muestra la posicion de la mas proxima letra o empezando desde cero
print(my_string.find('o'))
print(my_string.find('H'))  # En este caso H la encuentra en la posicion cero
# Precisa la longitud del contenido en la variable contando todo y espacios
print(len(my_string))
print(my_string.index('o'))  # Brinda la posicion en la que se encuentra
print(my_string[1])  # Precisa el valor que esta en la posicion 1
print(my_string[0])
print(my_string[-2])  # Lee al string al inverso empieza desde el final
# ['Hola', 'mundo']
# ['H', 'la mund', '']
# ['Hola mundo']
# ['Hola mundo'] presente
# 1
# 0
# 10
# 1
# o
# H
# d
