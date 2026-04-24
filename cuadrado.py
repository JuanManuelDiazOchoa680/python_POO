class Coordenada:
    # Método constructor
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    def getX(self):
        return self.__X
    def getY(self):
        return self.__Y
    def setX(self, x):
        self.__X = x
    def setY(self, y):
        self.__Y = y

    def mostrarCoordenada(self):
        print("(",self.__X,",",self.__Y, ")")
#-----------------------
class Cuadrado:
    # Método constructor
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4


    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices:")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()

def main():
    v1 = Coordenada(0,0)
    v2 = Coordenada(0,1)
    v3 = Coordenada(1,1)
    v4 = Coordenada(1,0)
    cuadrado = Cuadrado(v1,v2,v3,v4)
    cuadrado.mostrarVertices()

if __name__ == "__main__":
    main()