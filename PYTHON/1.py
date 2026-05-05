#class Persona :
  #  def __init__(self,nome,eta):
   #     self.nome = nome
    #    self.eta = eta 

#def saluta(self):
 #   return f"Ciao,sono {self.nome} e ho {self.eta} anno. "
import math
class Cerchio:
    def __init__(self,r):
        self.raggio = r
    def area (self):
        return math.pi*(self.raggio**2)     

    def perimetro(self):
        return 2 * math.pi * self.raggio
str(10)    
c= Cerchio(10) 
print(f"Area: {c.area()},Circonferenza: {c.perimetro()}")  