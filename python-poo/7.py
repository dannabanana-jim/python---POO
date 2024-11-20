#Ejercicio 7
#Desarrollar un programa con tres clases:
#La primera debe ser Universidad, con atributos 
#(Donde se almacena el nombre de la Universidad).
#La segunda llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante).
#Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. 
#El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
class Universidad:
    def __init__(self, nombre):
        self.nombre_universidad = nombre



class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad



class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera

    def mostrar_datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, "
                f"su especialidad es {self.carrera.especialidad}. "
                f"Estudia en la Universidad {self.universidad.nombre_universidad}.")



universidad = Universidad("Harvard")
carrera = Carrera("Ingeniería Mecatrónica")
persona = Estudiante("Mike", 19, universidad, carrera)
persona.mostrar_datos()
