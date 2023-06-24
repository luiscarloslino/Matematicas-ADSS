# Las tuplas a diferencia de listas contienen informacion que no se va a alterar
trimestre1 = (1, 2, 3)
print(trimestre1)
print(type(trimestre1))

# Asignando una tupla a una variable
meses_trimestre1 = tuple(('Ene', 'Feb', 'Mar'))
print(meses_trimestre1, '\n')

# Visualizando los metodos que podemos aplicar a una tupla tenemos:
# print(dir(trimestre1))     #retirar comentario para ver todos los metodos

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', 'count', 'index']


# (1, 2, 3)
# <class 'tuple'>
# ('Ene', 'Feb', 'Mar')
