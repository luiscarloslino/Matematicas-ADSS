# Tambien los diccionarios pueden ser colocados dentro de una lista
producto = [
    {'codigo': 'ABC100', 'descripcion': 'Libro', 'precio': 29.90},
    {'codigo': 'FGH222', 'descripcion': 'Cuaderno A4', 'precio': 12.50}
]
print(producto)
print(type(producto))
print('\n', 'Trabajemos con listar, consultar, ingresar, modificar, borrar y eliminar en un diccionario')
ipAddress = {'red1': '192.168.1.10',
             'red2': '192.168.1.20', 'red3': '192.168.1.30'}
print(ipAddress)
print('red1' in ipAddress)  # red1 existe en ipAddress
print('red5' in ipAddress)  # red5 NO existe en ipAddress
print(ipAddress['red2'])  # podemos identificar el valor de un componente
ipAddress['red4'] = '192.168.1.90'  # Permite adicionar un nuevo componente
print(ipAddress)
del ipAddress['red3']
print(ipAddress)
# Permite modificar informacion de un componente
ipAddress['red4'] = '192.168.1.120'
print(ipAddress)
red1 = ['192.168.1.200', '192.168.1.202', '192.168.1.204']
ipAddress['red1'] = ['192.168.1.200', '192.168.1.202',
                     '192.168.1.204']  # Permite un componente sea una lista
print(ipAddress)
print(ipAddress['red1'])
# [{'codigo': 'ABC100', 'descripcion': 'Libro', 'precio': 29.9}, {'codigo': 'FGH222', 'descripcion': 'Cuaderno A4', 'precio': 12.5}]
# <class 'list'>

#  Trabajemos con listar, consultar, ingresar, modificar, borrar y eliminar en un diccionario
# {'red1': '192.168.1.10', 'red2': '192.168.1.20', 'red3': '192.168.1.30'}
# True
# False
# 192.168.1.20
# {'red1': '192.168.1.10', 'red2': '192.168.1.20', 'red3': '192.168.1.30', 'red4': '192.168.1.90'}
# {'red1': '192.168.1.10', 'red2': '192.168.1.20', 'red4': '192.168.1.90'}
# {'red1': '192.168.1.10', 'red2': '192.168.1.20', 'red4': '192.168.1.120'}
# {'red1': ['192.168.1.200', '192.168.1.202', '192.168.1.204'], 'red2': '192.168.1.20', 'red4': '192.168.1.120'}
# ['192.168.1.200', '192.168.1.202', '192.168.1.204']
