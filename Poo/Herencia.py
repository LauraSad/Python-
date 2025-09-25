class Vehicle:
    def __init__(self,brand,model,price):
        #Encapsulacion  Se refiere a mantener los datos privados dentro de una clase y acceder a ellos solo mediante los metodos publicos (ABSTRACCION)
        # 
        # 
        # estas son las variables de intancia
        self.brand = brand
        self.model = model
        self.price = price
        self.is_avaible = True

    def sell(self):
        if self.is_avaible:
            self.is_avaible = False
            print(f"El vehículo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehículo {self.brand}. No está disponible")
    #ABSTRACCION  
    # #
    def get_price(self):
        return self.price
    
    def check_available(self):
        return self.is_avaible
        
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def stop_engine(self):

        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
#Crear la clase auto,bicicleta y camión 
#HERENCIA
class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else: 
            return f"El coche{self.brand} no está disponible"
#poliformismo  que diferentes clases respondan a los mismos métodos de maneras distintas
    def stop_engine(self):
        if  self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else: 
            return f"El coche{self.brand} no está disponible"    
                
class Bike(Vehicle):
        
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else: 
            return f"La bicicleta {self.brand} no está disponible"
    def stop_engine(self):
        if  self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else: 
            return f"La bicicleta {self.brand} no está disponible"    
            
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camion {self.brand} está en marcha"
        else: 
            return f"El camion {self.brand} no está disponible"
    def stop_engine(self):
        if  self.is_available:
            return f"El motor del camion {self.brand} se ha detenido"
        else: 
            return f"El camion{self.brand} no está disponible"
                
class Customer:
    def __init__(self,name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self,vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
             print(f"Lo siento {vehicle.brand} no esta disponible")
    
    def inquire_vehicle(self,vehicle: Vehicle):
        if vehicle.check_available():
             availability = "Disponible"
        else:
             availability = " No disponible"
        print(f"El {vehicle.brand} esta {availability} y cuesta {vehicle.get_price()}")

class DealerShip:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido agregado al inventario")

    def register_customer(self,customer):
        self.customers.append(customer)
        print(f"{customer.name} ha sido agregado")
    
    def show_avaible_vehicle(self):
        print("Los vehiculos disponibles son:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"-{vehicle.brand} por {vehicle.get_price()}")


# Crear las instancias de clases
car1= Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07",7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Marlon")

dealership = DealerShip()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)
dealership.register_customer(customer1)

#Mostrar vehiculos disponibles

dealership.show_avaible_vehicle()

#Cliente consulta un vehiculo
customer1.inquire_vehicle(car1)

#Cliente compra un vehiculo

customer1.buy_vehicle(car1)

customer1.buy_vehicle(car1)



     
    



        
        
