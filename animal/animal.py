class Animal:
    def __init__(self,Nombre, Peso):
        self.Nombre = Nombre
        self.Peso = Peso
        
    def __str__(self):
        return f"El nombre es: {self.Nombre}, Peso: {self.Peso}"
