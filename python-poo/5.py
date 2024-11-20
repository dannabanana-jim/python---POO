#Ejercicio 5
#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más
#que hereden de Fabrica, las cuales son Moto y Carro.
#Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes.
#Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.

class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio



class Moto(Fabrica):
    def mostrar_atributos(self):
        print(f"La cantidad de llantas: {self._llantas}")
        print(f"El color es: {self._color}")
        print(f"El precio es: {self._precio}")



class Carro(Fabrica):
    def mostrar_atributos(self):
        print(f"La cantidad de llantas: {self._llantas}")
        print(f"El color es: {self._color}")
        print(f"El precio es: {self._precio}")



print("OBJETO = moto")
moto = Moto(2, "Gris", "$200")
moto.mostrar_atributos()


print("\nOBJETO = carro")
carro = Carro(4, "Negro", "$600")
carro.mostrar_atributos()
