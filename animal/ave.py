from animal import Animal

class Ave(Animal):
    def __init__(self, Nombre, Peso, Año_Nacimiento, Propietario):
        super().__init__(Nombre, Peso)
        self.Año_Nacimiento = Año_Nacimiento
        self.Propietario = Propietario
        
        
    def calcularedad(self):
        edad = 2024-self.Año_Nacimiento
        if edad >= 5:
            print("Mayor de edad")
        elif edad <=4:
            print("Menor de edad")     

    def __str__(self):
        return f"Ave: {self.Nombre}, Peso: {self.Peso} kg, Año de Nacimiento: {self.Año_Nacimiento}, Propietario: {self.Propietario}"   
    
ave1 = Ave("paco",2,2015,"yisus")
print(ave1)
ave1.calcularedad()