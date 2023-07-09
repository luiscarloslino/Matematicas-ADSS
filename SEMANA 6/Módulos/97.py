# Los modules te permite crear aplicaciones reales pues podemos utilizar lo que otros ya
# han creado y validado por mucho tiempo y que solo debemos descargarlos los que estan
# disponibles en funcion de lo que deseamos trabajar y aprovechar el criterio multiproposito
# de python ya sea para aplicaciones de escritorio, web, IoT, ciberseguridad, juegos etc.
#
# Hay 3 tipos de modulos:
# 1: Modulos que podamos crear
# 2: Modulos descargados de terceros o internet
# 3: Modulos nativos de Python

# Empecemos con los modulos preconcebidos que viene con python que se realizan con import
# Vea el banco de modulos de python: https://docs.python.org/3/py-modindex.html
# Vea uno de los principales bancos de modulos de terceros: https://pypi.org/
import datetime  # De esta forma se invoca a todo el modulo
fecha = datetime.date.today()  # Se debe invocar modulo y su funcion
hora_minuto = datetime.timedelta(minutes=70)
print(fecha)
print(type(fecha))
print(hora_minuto)
# 2019-11-02
# <class 'datetime.date'>
# 1:10:00
