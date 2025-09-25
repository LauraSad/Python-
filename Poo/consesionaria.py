#Vehiculo
#compra y venta
class Auto:
    def __init__(self, brand,model,price):
       
        self.brand = brand
        self.model = model
        self.price = price
        self.avaible = True
    #vender
    def sell(self):
        if self.avaible:
            self.avaible = False
            print(f"El auto {self.brand}{self.model} ha sido vendido")
        else: 
            print(f"El auto {self.brand}{self.model} no está disponible")

    def check_availability(self):
        return self.avaible
    
    def get_price(self):
        return self.price
class Client:
    def __init__(self,name,dni):
        self.name = name
        self.dni = dni
        self.purchased_autos = []   

    def purchase_car(self, auto):
        if auto.avaible:
            auto.sell()
            self.purchased_autos.append(auto)
        
        else:
            print(f"El auto {auto.brand} no está disponible")


    def inquire_car(self,auto):
        availability = "disponible" if auto.check_availability() else "no disponible"
        print(f"El coche {auto.brand}{auto.model} está {availability} y cuesta {auto.price}")
   

class Concessionary:
    def __init__(self):
        self.clients = []
        self.autos = []
    def register_client(self,client):
        self.clients.append(client)
        print(f"{client.name} con numero de identificacion {client.dni} ha sido registrado")
    
    def add_autos(self,auto):
        self.autos.append(auto)
        print(f"el automovil{auto.brand} {auto.model} ha sido añadido al inventario")
    
    def show_avaible_autos(self):
        print("Los automoviles disponibles son:")
        for auto in self.autos:
            if auto.check_availability():
                print(f"-{auto.brand}{auto.model} por {auto.price}")
    


#Crear la instancia de coches
car1 = Auto("Mazda", "Mazda 3","1000")
car2 = Auto("Renault", "2005","500")

#Create instance of client
client1 = Client("Laura", "1002458538")

# Create instance of concessionary and register cars and clients
concessionary = Concessionary()
concessionary.add_autos(car1)
concessionary.add_autos(car2)
concessionary.register_client(client1)

#show price
Auto.get_price(car1)

#Show avaible autos
concessionary.show_avaible_autos()

# Client inquire a car
client1.inquire_car(car1)

#client buy a car
client1.purchase_car(car1)

#Show again avaible autos
concessionary.show_avaible_autos()


client1.purchase_car(car1)


            

        

        