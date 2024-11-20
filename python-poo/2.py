# Ejercicio 2
# Crear una clase “Persona” con atributos nombre y edad. 
# Además, el método “cumpleaños” debe aumentar en 1 la edad de la persona.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1


p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))
p.cumpleaños()  
p.cumpleaños()  
print(f"{p.nombre} cumple {p.edad} años")
