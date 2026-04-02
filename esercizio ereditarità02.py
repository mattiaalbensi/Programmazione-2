class persona:
    def __init__(self,nome,cognome,eta):
     self.nome = nome
     self.cognome = cognome      
     self.eta = eta 
class dottore(persona):
    def __init__(self,nome,cognome,eta,specializzazione,stipendio,matricola,reparto ):
        super().__init__(nome,cognome,eta)
        self.specializzazione = specializzazione
        self.stipendio = stipendio 
        self.matricola = matricola
        self.reparto = reparto
        self.pazienti_in_cura =[]
    def prendi_in_cura(self,nuovo_paziente):
        self.pazienti_in_cura.append(nuovo_paziente)
class paziente(persona):
    def __init__(self,nome,cognome,eta,gruppo_sanguigno):
        super().__init__(nome,cognome,eta)
        self.gruppo_sanguigno = gruppo_sanguigno
        self.allergie = []
        self.patologie = []
    def aggiungi_patologia(self,patologia):
        self.patologie.append(patologia)
    def aggiungi_allergia(self,allergia):
        self.allergie.append(allergia)
    
doc = dottore("Andrea","Palermo",28,"Oncologia",100000,"B34","Oncologia:Padiglione B")
paz1 = paziente("Dario","Spadola",22,"A1")
paz1.aggiungi_patologia("melanoma")
paz1.aggiungi_allergia("polline")
doc.prendi_in_cura(paz1)

print(f"Il Dottor {doc.cognome},Età :{doc.eta},Laureato in : {doc.specializzazione},Numero matricola :{doc.matricola}, Nel reparto di :{doc.reparto} ,ha in cura:")
for p in doc.pazienti_in_cura:
    print(f"- {p.nome} {p.cognome} {p.eta} anni  , Gruppo sanguigno : {p.gruppo_sanguigno} ")
    print(f"  Patologie: {', '.join(p.patologie)}")
    print(f"  Allergie: {', '.join(p.allergie)}")
