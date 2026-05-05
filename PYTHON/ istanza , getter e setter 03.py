class Studente:
    def __init__(self, nome,eta):   
        self.nome = nome
        self.eta = eta
    def get_eta (self,):
        return f"l età dello studente è : {self.eta}"
    def set_eta(self,valore):
        self.eta = valore
    def saluta (self):
        return f"Ciao, sono : {self.nome}!"
    def get_nome(self):
        return f"il nome dello studente è : {self.nome}"
s = Studente("Salvo", 20)    
print(s.get_nome())
print(s.get_eta())
s.set_eta(90)
print(s.get_eta())
