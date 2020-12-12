from multipledispatch import dispatch

class clsGato:
    def __init__(self):
        self.__pos = 0

    def getPosicion(self):
        return self.__pos

    def caminar(self):
        self.__pos = self.__pos + 10

    @dispatch()#chequear libreria hasta 3.6
    def maullar(self):
        print('Miau Miau')

    @dispatch(int)
    def maullar(self, n):
        for i in range(n):
            print("Miau Miau")

class clsPerro:
    def __init__(self):
        self.__pos = 0

    def getPosicion(self):
        return self.__pos

    def caminar(self):
        self.__pos = self.__pos +4

    def ladrar(self):
        print ("Guau Guau")

# ppal
def pasearMascota(objMascota, n):
    for i in range(n):
        objMascota.caminar()
    print ("La mascota quedo en ",str(objMascota.getPosicion()))

perro=clsPerro()
gato=clsGato()
gato.maullar()
n=10
pasearMascota(perro,n)
pasearMascota(gato,n)
#gato.maullar(n)


#instalar xammp y pyqt5 para el taller del jueves