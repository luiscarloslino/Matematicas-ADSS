# Un objeto es una entidad que tiene atributos(caracteristicas) y acciones(metodos)
# Ejemplo podemos tener un objeto Humano y sus atributos serian su nacionalidad, estatura, edad
# y los metodos del objeto Humano serian caminar, hablar, correr, levantarse, dormir etc.
# Por lo tanto una clase es un molde o plantilla del cual proviene nuestro objeto y en ella
# representaremos sus atributos y metodos. Ahora entendido esto crearemos una clase y un objeto
# Revisar el siguiente enlace: https://www.youtube.com/watch?v=VYXdpjCZojA

class Humano1:  # Por standarizacion se acostumbra iniciar nombre de clase con mayuscula
    def __init__(self):  # Metodo init y en self se guarda la referencia del objeto que se esta creando
        print('soy un nuevo objeto')


pedro = Humano1()  # Ambas instancias invocan a la clase(plantilla) Humano1 y la ejecuta
raul = Humano1()


class Humano2:
    def __init__(self):
        print('soy un nuevo objeto')

    def hablar(self, mensaje):
        print(mensaje)


pedro = Humano2()
maria = Humano2()
pedro.hablar('Hola')
maria.hablar('Hola Pedro')


class Humano3:
    def __init__(self, edad):
        self.edad = edad

    def hablar(self, mensaje):
        print(mensaje)


pedro = Humano3(25)
maria = Humano3(20)

print('Soy Pedro y mi edad es', pedro.edad)
print('Soy Maria y mi edad es', maria.edad)
pedro.hablar('Hola')
maria.hablar('Hola Pedro')

# Recomendamos continuar revisando herencia
# En el siguiente enlace: https://www.youtube.com/watch?v=6dE57aXaChg


# soy un nuevo objeto
# soy un nuevo objeto
# soy un nuevo objeto
# soy un nuevo objeto
# Hola
# Hola Pedro
# Soy Pedro y mi edad es 25
# Soy Maria y mi edad es 20
# Hola
# Hola Pedro
