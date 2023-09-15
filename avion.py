import abc

class Avion():
    @abc.abstractmethod
    def despegando(self):
        pass
    
    @abc.abstractmethod
    def aterrizando(self):
        pass
    
class Boeing(Avion):
    
    def despegando(self):
        print("El Boeing esta despegando")
        
    def aterrizando(self):
        print("El Boeing esta aterrizando")
        
avion =Boeing()
avion.despegando()
avion.aterrizando()