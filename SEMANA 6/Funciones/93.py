# Ahora las funciones tambien pueden recibir un parametro
def saludo_inicial2(dato1=''):  # Asi creamos una funcion2 con parametro
    print('Hola', dato1, 'bienvenido.')


# Como dato1 tiene asignado algo aun haciendo enter no dara error
nombre = input('Ingresa tu nombre: ')
saludo_inicial2(nombre)  # Luego invocamos la funcion2 dando un parametro

print('\n')
# Hola Daniel bienvenido.
