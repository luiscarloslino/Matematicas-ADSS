my_dato0 = (70)  # Cuidado NO podemos trabajar juntos un numerico con string
my_dato1 = ('70')  # sin previa conversion a int o str

my_string1 = ('HolaMundo')
# Tampoco podemos trabajarlo porque es una tupla
my_string2 = ('hola', 'mundo', 'otra', 'vez')
# Tampoco podemos trabajarlo porque es una lista
my_string3 = ['hola', 'mundo', 'otra', 'vez']

print(my_dato0)
print(my_dato1)
print(my_dato0+int(my_dato1))
print(str(my_dato0)+my_dato1)
print(my_string1)
print(my_string2)
print(my_string3)
print(my_dato1.isnumeric())  # Consulta si es numerico
# Consulta si es alfanumerico encuentra un espacio False
print(my_string1.isalpha())
print(my_string1.isalpha())  # Consulta si es alfanumerico solo son letras True
# 70
# 70
# 140
# 7070
# HolaMundo
# ('hola', 'mundo', 'otra', 'vez')
# ['hola', 'mundo', 'otra', 'vez']
# True
# False
# True
