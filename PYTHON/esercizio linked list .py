# --- ESECUZIONE ESERCIZIO CRONOLOGIA MODIFICHE ---

# Creiamo l'istanza della LinkedList
cronologia = LinkedList()

# 1. Registra in ordine le prime modifiche: "admin", "mario", "sara"
cronologia.insertLast("admin")
cronologia.insertLast("mario")
cronologia.insertLast("sara")

# 2. Stampa la cronologia
print(f"2. Cronologia iniziale: {cronologia}")

# 3. "guest" ha modificato il file dopo "mario"
cronologia.insertAfter("mario", "guest")

# 4. Stampa la cronologia
print(f"4. Dopo inserimento guest: {cronologia}")

# 5. "root" ha modificato il file per primo — inseriscilo prima di "admin"
cronologia.insertBefore("admin", "root")

# 6. Stampa la cronologia
print(f"6. Dopo inserimento root: {cronologia}")

# 7. "luca" ha modificato il file prima di "sara"
cronologia.insertBefore("sara", "luca")

# 8. Stampa la cronologia
print(f"8. Dopo inserimento luca: {cronologia}")

# 9. La modifica più vecchia è stata archiviata — rimuovi il primo elemento
# (In una lista dove aggiungi in fondo, il primo è il più vecchio)
vecchia = cronologia.removeFirst()
print(f"9. Archiviata modifica di: {vecchia}")

# 10. Stampa la cronologia
print(f"10. Cronologia aggiornata: {cronologia}")

# 11. L'ultima modifica è stata annullata — rimuovi l'ultimo elemento
annullata = cronologia.removeLast()
print(f"11. Annullata modifica di: {annullata}")

# 12. Stampa la cronologia
print(f"12. Cronologia finale: {cronologia}")

# 13. Stampa quante modifiche sono registrate
print(f"13. Numero modifiche registrate: {cronologia.size()}")

# 14. Stampa chi ha effettuato la modifica più recente (la testa attuale) senza rimuoverlo
print(f"14. Prossima modifica da processare: {cronologia.peekFirst()}")