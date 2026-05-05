# 1. Creiamo la lista iniziale
fila = ["Mario", "Giulia", "Tonino", "Rosa"]

# 2. Il macellaio chiama il primo cliente (posizione 0)
# pop(0) rimuove l'elemento e lo salva nella variabile 'servito'
servito = fila.pop(0)
print(f"Servo: {servito}")

# 3. Arriva un nuovo cliente (va in fondo alla lista)
fila.append("Enzo")

# 4. Quante persone mancano?
print(f"Persone ancora in fila: {len(fila)}")

print("-" * 20)

# 5. Servi tutti i rimanenti fino a chiusura
# Finché la lunghezza della lista è maggiore di 0
while len(fila) > 0:
    prossimo = fila.pop(0)
    print(f"Servo: {prossimo}")

print("Macelleria chiusa!")