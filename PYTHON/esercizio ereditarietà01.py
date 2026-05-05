class persona:
    def __init__(self,nome,cognome,eta):
     self.nome = nome
     self.cognome = cognome      
     self.eta = eta 
class dottore(persona):
    def __init__(self,nome,cognome,eta,professione,stipendio):
        super().__init__(nome,cognome,eta)
        self.professione = professione
        self.stipendio = stipendio 
class paziente(persona):
    def __init__(self,nome,cognome,eta,gruppo_sanguigno):
        super().__init__(nome,cognome,eta)
        self.gruppo_sanguigno = gruppo_sanguigno
 
doc = dottore ("Andrea" , "Palermo", 28 ,"chirurgo" , 100000)
malato = paziente("Dario" , "Spadola", 22, "A1")  

print(f"il Dottor {doc.cognome} (Età:{doc.eta}) percepisce uno stipendio di {doc.stipendio}")    
print(f"il Paziente {malato.cognome} (Età: {malato.eta}) ha il gruppo sanguigno : {malato.gruppo_sanguigno}")