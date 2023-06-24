# Reasignando valores
# Recordar [] listas pueden cambiar no () tuplas
colores = ['red', 'green', 'blue']
print('Los colores son', colores)
print('En este momento [1] seria:', colores[1])
colores[1] = 'yellow'  # Color yellow reemplaza al que esta en posicion 1
print('ahora lo cambiamos y los colores son', colores)
print('Los colores RGB son: ', len(colores))

# Podemos conocer con funcion dir() metodos adicionales de como trabajar con una lista
# Puede descomentarla para apreciar los metodos posibles
print(dir(colores))
# Los colores son ['red', 'green', 'blue']
# En este momento [1] seria: green
# ahora lo cambiamos y los colores son ['red', 'yellow', 'blue']
# Los colores RGB son:  3
# ['__add__', '__class__', '__contains__', '__delattr__',
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__gt__',
#  '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__',
#  '__subclasshook__', 'append', 'clear', 'copy', 'count',
#  'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
