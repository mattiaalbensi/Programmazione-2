class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left   = None   # figlio sinistro — valori minori
        self.right  = None   # figlio destro — valori maggiori


class BST:
    def __init__(self):
        self.__radice = None

    def insert(self, valore):
        if self.__radice is None:
            self.__radice = NodoBST(valore)
        else:
            # partiamo dalla radice e scendiamo nell'albero
            # la funzione chiamerà se stessa finché non trova un posto libero
            self.__insertRicorsivo(self.__radice, valore)


    def __insertRicorsivo(self, nodo, valore):
        if valore < nodo.valore:
            # il valore è minore — dobbiamo andare a sinistra
            if nodo.left is None:
                # CASO BASE: posto libero a sinistra — inseriamo qui
                nodo.left = NodoBST(valore)
            else:
                # CASO RICORSIVO: c'è già un nodo a sinistra
                # richiamiamo la stessa funzione sul figlio sinistro
                # il problema si riduce: scendiamo di un livello
                self.__insertRicorsivo(nodo.left, valore)
        else:
            # il valore è maggiore — dobbiamo andare a destra
            if nodo.right is None:
                # CASO BASE: posto libero a destra — inseriamo qui
                nodo.right = NodoBST(valore)
            else:
                # CASO RICORSIVO: c'è già un nodo a destra
                # richiamiamo la stessa funzione sul figlio destro
                self.__insertRicorsivo(nodo.right, valore)

    def search(self, valore):
        # partiamo dalla radice
        return self.__searchRicorsivo(self.__radice, valore)

    def __searchRicorsivo(self, nodo, valore):
        # CASO BASE 1: nodo inesistente — il valore non è nell'albero
        if nodo is None:
            return False

        # CASO BASE 2: trovato — il valore corrisponde
        if nodo.valore == valore:
            return True

        if valore < nodo.valore:
            # il valore è minore — non può essere a destra
            # CASO RICORSIVO: cerchiamo solo nel sottoalbero sinistro
            return self.__searchRicorsivo(nodo.left, valore)
        else:
            # il valore è maggiore — non può essere a sinistra
            # CASO RICORSIVO: cerchiamo solo nel sottoalbero destro
            return self.__searchRicorsivo(nodo.right, valore)

    def inOrder(self):
        # inOrder restituisce i valori in ordine crescente
        # perché visita prima sinistra, poi radice, poi destra
        elementi = []
        self.__inOrderRicorsivo(self.__radice, elementi)
        return elementi

    def __inOrderRicorsivo(self, nodo, elementi):
        # CASO BASE: nodo inesistente — non c'è nulla da visitare
        if nodo is None:
            return

        # CASO RICORSIVO:
        # 1. visita prima tutto il sottoalbero sinistro (valori minori)
        self.__inOrderRicorsivo(nodo.left, elementi)

        # 2. poi aggiungi il valore del nodo corrente
        elementi.append(nodo.valore)

        # 3. poi visita tutto il sottoalbero destro (valori maggiori)
        self.__inOrderRicorsivo(nodo.right, elementi)

    def isEmpty(self):
        return self.__radice is None

    def __repr__(self):
        return f"BST(inOrder={self.inOrder()})"

import random
import time

# --- 1. DEFINIZIONE DELLA LISTA COLLEGATA CIRCOLARE ---
class NodoLista:
    def __init__(self, valore):
        self.valore = valore
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.__testa = None

    def insertLast(self, valore):
        nuovo = NodoLista(valore)
        if not self.__testa:
            self.__testa = nuovo
            nuovo.next = self.__testa
        else:
            corrente = self.__testa
            while corrente.next != self.__testa:
                corrente = corrente.next
            corrente.next = nuovo
            nuovo.next = self.__testa

    def search(self, valore):
        if not self.__testa: return False
        corrente = self.__testa
        while True:
            if corrente.valore == valore:
                return True
            corrente = corrente.next
            if corrente == self.__testa:
                break
        return False

# --- 2. IL TUO CODICE BST (Assicurati che la classe BST sia qui sopra) ---
# [Qui ci va la classe BST che hai postato prima]

# --- 3. IL TEST DEI TEMPI (Punti 1-6) ---

# 1) Genera 1000 numeri casuali
numeri_casuali = [random.randint(1000000, 1000000000) for _ in range(1000)]

# 2) Inserisci nelle strutture
albero = BST()
lista_linkata = CircularLinkedList()

for n in numeri_casuali:
    albero.insert(n)
    lista_linkata.insertLast(n)

# 3) Scegli il 500esimo elemento da cercare
target = numeri_casuali[999]

# 4) Misura tempo Lista
start_l = time.perf_counter()
lista_linkata.search(target)
end_l = time.perf_counter()
tempo_lista = end_l - start_l

# 5) Misura tempo BST
start_b = time.perf_counter()
albero.search(target)
end_b = time.perf_counter()
tempo_bst = end_b - start_b

# 6) Stampa risultati
print(f"Risultati per il numero: {target}")
print(f"Tempo Lista: {tempo_lista:.10f}s")
print(f"Tempo BST:   {tempo_bst:.10f}s")

if tempo_bst > 0:
    print(f"\nIl BST è {tempo_lista/tempo_bst:.2f} volte più veloce!")