print('\n'+'Tambien considerar la tabla de precedencia')
# https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/operadores_aritmeticos.html
# http://www.mclibre.org/consultar/python/lecciones/python-salida-pantalla.html
# Agrupacion:()
# Unario: +-   # el operador afecta solo a un operador
# Exponente: **
# Multiplicación, División, División entera, Módulo: *, /, //, %
# Suma, Resta: +, -
print()
print('-2=', -2)  # Resultado es -3
print('+2=', +2)  # Resultado es 1
print('-2+2*3=', -2+2*3)
print('(20+10)*5/2**2=', (20+10)*5/2**2)
# end concatena 2 print colocando su contenido entre ellos
print('(20+10)*5/2**2', end='=')
print((20+10)*5/2**2)
print('La secuencia es: () sigue ** luego * y termina con / siendo el resultado', 150/4)
print('9 % 6 % 3=', 9 % 6 % 3)   # opera normal de izq a derecha
print('2 ** 2 **3=', 2 ** 2 ** 3)  # en este caso unico solo de derecha a izq
print('\n'+'Operaciones previo al ingreso de un numero')
# El curso queda en espera hasta que ingrese informacion
edad = input('Ingrese su edad:')
print(type(edad))  # Importante input registra una variable tipo string
# Entonces para hacerle operaciones debe convertirse a int o float
nueva_edad = int(edad)+5
print('Su edad + 5 es igual a', nueva_edad)
# Tambien considerar la tabla de precedencia

# -2= -2
# +2= 2
# -2+2*3= 4
# (20+10)*5/2**2= 37.5
# (20+10)*5/2**2=37.5
# La secuencia es: () sigue ** luego * y termina con / siendo el resultado 37.5
# 9 % 6 % 3= 0
# 2 ** 2 **3= 256

# Operaciones previo al ingreso de un numero
# <class 'str'>
# Su edad + 5 es igual a 45
