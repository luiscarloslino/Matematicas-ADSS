# Aplicando la funcion range() podemos construir una lista
rango_number1 = list(range(1, 11))
print('\n'+'Rango de lista desde el 1 al 10 - importante siempre colocar un numero mas en rango')
print(rango_number1)
rango_number2 = list(range(1, 100))
print('\n'+'Rango de lista desde el 1 al 99 - importante siempre colocar un numero mas en rango')
print(rango_number2)

vocales_list = list(('a', 'e', 'i', 'o', 'u'))
# Indica la cantidad de datos en la lista
print('Cantidad de la lista es: ', len(vocales_list))
# Muestra posicion cero osea letra a
print('Primero de la lista es: ', vocales_list[0])
print('Ultimo de la lista es: ', vocales_list[-1])
# Validando existencia de un dato de la lista
vocal_u_esta = ('u' in vocales_list)
print('Validando si existe vocal u: ', vocal_u_esta)
# Rango de lista desde el 1 al 10 - importante siempre colocar un numero mas en rango
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Rango de lista desde el 1 al 99 - importante siempre colocar un numero mas en rango
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# Cantidad de la lista es:  5
# Primero de la lista es:  a
# Ultimo de la lista es:  u
# Validando si existe vocal u:  True
