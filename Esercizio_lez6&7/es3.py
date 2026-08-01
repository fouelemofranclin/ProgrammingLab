import csv

class CSVFile:
    def __init__(self, name):
        # 1. Alza un'eccezione se il nome del file non è una stringa
        if not isinstance(name, str):
            raise TypeError("Errore: Il nome del file deve essere una stringa!")
        self.name = name

    def get_data(self, start=None, end=None):
        data = []
        
        # Apertura del file con gestione dell'errore (Esercizio 1)
        try:
            with open(self.name, mode='r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Errore: Il file '{self.name}' non esiste.")
            return []

        # Se il file è vuoto, ritorniamo una lista vuota
        if not data:
            return []

        # 2. SANITIZZAZIONE E CONTROLLO DI START ED END
        # Il testo specifica che si parte da riga "1" (indice umano) ed estremi inclusi.
        
        # --- Sanitizzazione di 'start' ---
        if start is None:
            start_idx = 0
        else:
            try:
                start = int(start)
                if start < 1:
                    start_idx = 0  # Se minore della prima riga, partiamo dall'inizio
                else:
                    start_idx = start - 1  # Trasformiamo in indice Python (0-based)
            except (ValueError, TypeError):
                start_idx = 0  # Se non è un numero valido, usiamo il default

        # --- Sanitizzazione di 'end' ---
        if end is None:
            end_idx = len(data)
        else:
            try:
                end = int(end)
                if end > len(data):
                    end_idx = len(data)  # Se oltre la fine del file, ci fermiamo alla fine
                elif end < start_idx + 1:
                    end_idx = start_idx  # Se end è minore di start, restituisce lista vuota
                else:
                    end_idx = end  # Lo slicing esclude l'estremo destro. Poiché l'utente ragiona 
                                   # in 1-based ed include l'estremo, il valore 'end' coincide 
                                   # perfettamente con il punto di stop di Python.
                                   # Esempio: start=1, end=2 -> data[0:2] (prende indici 0 e 1)
            except (ValueError, TypeError):
                end_idx = len(data)

        # Ritorna l'intervallo richiesto sfruttando lo slicing di Python
        return data[start_idx:end_idx]
    




    # 1. Test Eccezione nell'__init__
try:
    file_fallito = CSVFile(12345) # Passiamo un intero invece di una stringa
except TypeError as e:
    print(f"Test superato! Eccezione intercettata: {e}\n")

# Creiamo un file di test al volo con 5 righe
with open("test_intervallo.csv", "w", encoding="utf-8") as f:
    f.write("riga1,intestazione\n")
    f.write("riga2,valore1\n")
    f.write("riga3,valore2\n")
    f.write("riga4,valore3\n")
    f.write("riga5,valore4\n")

f = CSVFile("test_intervallo.csv")

# 2. Test intervallo normale (dalla riga 2 alla riga 4 incluse)
print("Righe da 2 a 4:", f.get_data(start=2, end=4))
# Output atteso: [['riga2', 'valore1'], ['riga3', 'valore2'], ['riga4', 'valore3']]

# 3. Test sanitizzazione (start negativo e end gigante)
print("Parametri fuori scala (start=-5, end=100):", f.get_data(start=-5, end=100))
# Output atteso: restituisce l'intero file autosanitizzandosi su [0:5]

# 4. Test con stringhe non numeriche passate a start ed end
print("Parametri errati (start='ciao', end=None):", f.get_data(start="ciao"))
# Output atteso: ignora 'ciao', lo imposta a default (0) e mostra tutto il file