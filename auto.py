# https://atareao.es/pyldora/clases-abstractas-interfaces-y-polimorfismo/
import abc
class Vehiculo(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def star_engine(self):
        pass
    
    def stop_engine(selef):
        pass
    
class Car(Vehiculo):
    def star_engine(self):
        print("Car engine started")
        
    def stop_engine(self):
        print("Car engine stopped")
        
    
        
class Truck(Vehiculo):
    def star_engine(self):
        print("Truck engine started")
        
    def stop_engine(self):
        print("Truck engine stopped")
        
car = Car()
car.star_engine()
car.stop_engine()

truck = Truck()
truck.star_engine()
truck.stop_engine()

   