# De esta forma solo se invoca una funcion del modulo
# Tambien se puede invocar mas de una funcion
from datetime import timedelta, date
from datetime import timedelta
# La diferencia es que ahora solo se invoca a la funcion
hora_minuto = timedelta(minutes=140)
print('\n', hora_minuto)
print(timedelta(minutes=90))

print('\n', timedelta(minutes=90))
print(date.today())

# Para crear nuestros propios modulos y su invocacion trabajaremos a continuacion con:
# miModulo1.py - Donde definiremos nuestros propias funciones (los nombres no deben iniciar con numeros)
# miPrograma1.py - Que invocara a miModulo1

#  2:20:00
# 1:30:00

#  1:30:00
# 2019-11-02
