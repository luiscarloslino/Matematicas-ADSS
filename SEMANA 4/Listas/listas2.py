# Podemos hacer uso del constructor de lista con list()
print('\n'+'Aplicando la funcion list() en una variable=list((dato1,dato2,n))')
number_list = list((1, 2, 3, 4))  # importante observar el (())
print(number_list)  # Una variable solo acepta un dato
print(type(number_list))  # asi que para guardar la lista como unidad
vocales_list = list(('a', 'e', 'i', 'o', 'u'))  # se debe agrupar como tupla
print(vocales_list)
print(type(number_list), type(vocales_list))
# Aplicando la funcion list() en una variable=list((dato1,dato2,n))
# [1, 2, 3, 4]
# <class 'list'>
# ['a', 'e', 'i', 'o', 'u']
# <class 'list'> <class 'list'>
