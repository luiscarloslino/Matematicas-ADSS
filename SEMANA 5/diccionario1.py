# Permite armar informacion mas completa e integrada y es ampliamente utilizada
producto = {
    'tipo': 'book',  # No olvidar colocar coma luego de cada dato del diccionario
    'cantidad': 3,
    'precio': 19.90
}

persona = {
    'nombre': 'Daniel',
    'apellido': 'Saavedra',
    'RUC': '10056749724',
    'edad': 27
}
# Para visualizar los metodos aplicamos dir
print(type(producto))  # Mostrara que es de tipo dict
# print(dir(persona))         #Recomendamos luego comentar esta linea
# Presenta a las etiquetas que contienen informacion en el diccionario
print(persona.keys())
print(persona.items())  # Presenta a todos los keys y su valor
persona.clear()  # Limpia la variable de todos los items
print(persona)
# <class 'dict'>
# dict_keys(['nombre', 'apellido', 'RUC', 'edad'])
# dict_items([('nombre', 'Daniel'), ('apellido', 'Saavedra'), ('RUC', '10056749724'), ('edad', 27)])
# {}
