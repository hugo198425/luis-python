
class Vehiculo:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def mostrarInformacionVehiculo(self):
        print("====Imformacion del Vehiculo====\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidad: {self.velocidad}")
        
    def acelerarVehiculo(self,divtiempo,velocidadFinal):
        
        return (velocidadFinal- self.velocidad)/ divtiempo

def main():
        vehiculo1 = Vehiculo("toyota", "corolla", 30)
        vehiculo1.mostrarInformacionVehiculo()
        aceleracion = vehiculo1.acelerarVehiculo(30,110)
        print(f"tu nueva aceleracion es : {aceleracion} m/s")


        vehiculo2 = Vehiculo("ford", "mustang", 50)
        vehiculo2.mostrarInformacionVehiculo()
        aceleracion = vehiculo2.acelerarVehiculo(30,130)
        print(f"Tu nueva aceleracion es : {aceleracion} m/s")
        
            
if __name__ == "__main__": 
    main()








