# set refiere a una coleccion desordenada de datos y que no tiene un indice
# Se reconoce porque estan cotenidos entre {}
colores = {'Red', 'Green', 'Blue'}
print(colores)  # recalcamos los datos contenidos no tienen un indice que los posicione
print(type(colores))  # Comprobamos que muestra el tipo set
# Aun asi se puede hacer reconocimiento si contiene un dato especifico
print('Red' in colores)
# Lo adiciona pero comprobamos que lo coloca en cualquier posicion
colores.add('Violet')
print(colores)
colores.add('Black')
print(colores)  # Lo adiciona pero comprobamos que lo coloca en cualquier posicion
colores.add('White')
print(colores)  # Lo adiciona pero comprobamos que lo coloca en cualquier posicion
# Prueba ejecutando 2 veces sin limpiar pantalla veras que los 3 colores adicionados tienen
# diferente posicion cada vez que lo ejecutamos

colores.remove('Red')  # Podemos tambien remover componentes
print(colores)
colores.clear()  # Remueve todos los datos de set
print(colores)
del colores  # Este comando lo elimina por completo
# print(colores)               #Daria error porque colores fue eliminado


# {'Blue', 'Green', 'Red'}
# <class 'set'>
# True
# {'Blue', 'Green', 'Violet', 'Red'}
# {'Blue', 'Violet', 'Red', 'Black', 'Green'}
# {'Blue', 'Violet', 'Red', 'Black', 'White', 'Green'}
# {'Blue', 'Violet', 'Black', 'White', 'Green'}
# set()
