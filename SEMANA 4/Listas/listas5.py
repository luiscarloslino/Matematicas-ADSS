colores = ['red', 'yellow', 'blue']

colores.append('violet')  # Con append podemos adicionar 1 dato a la lista
print(colores)
# Con extend podemos adicionar varios datos a la lista como tupla
colores.extend(('green', 'orange'))
print(colores)
# Con extend podemos adicionar varios datos a la lista o como lista
colores.extend(['blank', 'white'])
print(colores)
colores.insert(1, 'pink')  # Insertando un color en una posicion dada
print(colores)
# Insertando un color al ultimo de la lista - nota -1 coloca en penultimo
colores.insert(len(colores), 'brown')
colores.remove('violet')  # Metodo remove() remueve un dato especifico
print(colores)
colores.sort()  # Metodo sort ordena a - z o menor a mayor
print(colores)
print('Color green quedo ahora en posicion', colores.index('green'))
colores.sort(reverse=True)  # Metodo sort ordena z - a o mayor a menor
print(colores)
print('Ahora color green quedo en posicion', colores.index('green'))
print('Tambien contar cuantos green existen', colores.count('green'))
colores.clear()  # Metodo clear limpia todos los datos de la lista
print(colores)
# ['red', 'yellow', 'blue', 'violet']
# ['red', 'yellow', 'blue', 'violet', 'green', 'orange']
# ['red', 'yellow', 'blue', 'violet', 'green', 'orange', 'blank', 'white']
# ['red', 'pink', 'yellow', 'blue', 'violet', 'green', 'orange', 'blank', 'white']
# ['red', 'pink', 'yellow', 'blue', 'green', 'orange', 'blank', 'white', 'brown']
# ['blank', 'blue', 'brown', 'green', 'orange', 'pink', 'red', 'white', 'yellow']
# Color green quedo ahora en posicion 3
# ['yellow', 'white', 'red', 'pink', 'orange', 'green', 'brown', 'blue', 'blank']
# Ahora color green quedo en posicion 5
# Tambien contar cuantos green existen 1
# []
