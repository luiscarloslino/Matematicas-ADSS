# Otra forma de hacer funciones es con lambda
def suma2(numero3, numero4): return int(numero3) + int(numero4)


tercer_numero = input('Ingrese tercer numero: ')
cuarto_numero = input('Ingrese cuarto numero: ')
print('La suma de los 2 numeros es: ', end='')
print(suma2(tercer_numero, cuarto_numero))
# La suma de los 2 numeros es: 140
