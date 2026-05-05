from abc import ABC, abstractmethod
class Animale(ABC):
    @abstractmethod
    def parla(self) -> str:
        pass
    def descrizione(self) -> str: 
        return f"{self.__class__.__name__} dice: {self.parla()}"

class Cane(Animale):
    def __init__(self, nome: str):
        self.__nome = nome                
        self.__energia = 100
 
    @property
    def nome(self): return self.__nome     
 
    @property
    def energia(self): return self.__energia
 
    def corri(self):
        self.__energia -= 17            
        return f"{self.__nome} corre! (energia: {self.__energia})"
 
    def parla(self) -> str: return "Bau!"
 
class Gatto(Animale):
    def __init__(self, nome: str):
        self.__nome = nome
 
    def parla(self) -> str: return "Miao~"
 
class Pappagallo(Animale):
    def __init__(self, nome: str, frase: str):
        self.frase = frase
 
    def parla(self) -> str: return self.frase
 
def fai_parlare(animale: Animale):
    print(" ", animale.descrizione())
rex   = Cane("Rex")
micio = Gatto("Micio")
polly = Pappagallo("Polly", "Voglio mangiare!")
print("=== POLIMORFISMO ===")
for a in [rex, micio, polly]:
    fai_parlare(a)
 
print("\n=== INCAPSULAMENTO ===")
print(" ", rex.corri())
try:    print(rex.__nome)
except: print(" il nome è privato e non e' accessibile!")
 
print("\n=== ASTRAZIONE ===")
try:    Animale()
except: print("Animale non si può istanziare direttamente!")
 