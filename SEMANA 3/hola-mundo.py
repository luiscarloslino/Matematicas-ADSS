print('hello world')
# hello world


print('Hola mundo')
print('''hola mundo''')
print("Hola MuNdO")
# Hola mundo
# hola mundo
# Hola MuNdO


print('\n', 'Deja una linea y con coma concatena dejando un espacio', 'como ven')
print('\n'+'Deja una linea y con + concatena sin dejar espacios'+'como aqui no')
print('Segun donde se ubique en este caso deja una linea al terminar', '\n')
print('Veamos otros ejemplo \n que pasara aqui-1')
print('Ahora si colocamos \\n que pasara aqui-2')
print('\n')
#  Deja una linea y con coma concatena dejando un espacio como ven
# Deja una linea y con + concatena sin dejar espacioscomo aqui no
# Segun donde se ubique en este caso deja una linea al terminar
# Veamos otros ejemplo
#  que pasara aqui-1
# Ahora si colocamos \n que pasara aqui-2


print('Ahora comprobamos', end=' ')
print('como concatenar', end=' varias lineas ')
print('aqui lo comprobamos')
print('Otros casos con end veamos que pasa', end='\n')
print('deberia ...')
print('Por ultimo, veamos este caso adicional', '\n')
print('cuantas lineas dejo...')
# Ahora comprobamos como concatenar varias lineas aqui lo comprobamos
# Otros casos con end veamos que pasa
# deberia ...
# Por ultimo, veamos este caso adicional

# cuantas lineas dejo...


# Al ejecutar muestra los números separados con -
print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='-')
print('------------------------')
print('Aqui', 'ejemplo1', 'con end y sep', sep='%')
print('Aqui', 'ejemplo2', 'end y sep', sep='/')
print('Aqui', 'ejemplo3', 'con end y sep', sep='_')
print('Aqui', 'ejemplo4', 'con end y sep', sep='*')
print(1, 2, 3, 4, 'cinco', 6, 'siete', 8, 9, sep='-')
# 1-2-3-4-5-6-7-8-9
# ------------------------
# Aqui%ejemplo1%con end y sep
# Aqui/ejemplo2/end y sep
# Aqui_ejemplo3_con end y sep
# Aqui*ejemplo4*con end y sep
# 1-2-3-4-cinco-6-siete-8-9


print('Aqui', 'ejemplo5', 'con end y sep', sep='_', end='&')
print('continua', 'con relacion', 'a linea anterior')
print('Aqui', 'ejemplo6', 'end y sep', sep='_', end='&')
print('continua', 'con relacion', 'linea anterior', sep='*')
print('------------------------')
# Aqui_ejemplo5_con end y sep&continua con relacion a linea anterior
# Aqui_ejemplo6_end y sep&continua*con relacion*linea anterior
# ------------------------


print('Aqui', 'ejemplo7', 'con end y sep', sep='_', end='*')
print('continua', 'con relacion', 'a linea anterior', sep='*', end='&\n')
print('Aqui', 'ejemplo8', 'con end y sep', sep='_', end='*')
print('continua con relacion a linea anterior', sep='*', end='\n')
# Aqui_ejemplo7_con end y sep*continua*con relacion*a linea anterior&
# Aqui_ejemplo8_con end y sep*continua con relacion a linea anterior
