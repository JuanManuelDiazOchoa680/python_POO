class Persona:
    def __init__(self,nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

# Metodo para mostrar la informacion de la persona
    def mostrarPersona(self):
        print("Nombre: ", self.nombre)
        print("Apellidos: ", self.apellidos)
        print("Edad: ", self.edad)

"""
def main():
    print("Vamos a aprender POO...")
    persona_1 = Persona("Lorenzo", "Perez", 18)
    persona_1.mostrarPersona()

if __name__ == "__main__":
    main()"""