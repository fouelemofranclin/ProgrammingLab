import csv

class CSVFile:
    def __init__(self, filepath):
        """
        Inizializza l'oggetto con il percorso del file CSV.
        Salva il nome del file nell'attributo 'name'.
        """
        self.name = filepath

    def get_data(self):
        """
        Legge il file CSV e restituisce il contenuto sotto forma di lista di liste.
        """
        dati = []
        try:
            with open(self.name, mode='r', newline='', encoding='utf-8') as file:
                lettore_csv = csv.reader(file)
                for riga in lettore_csv:
                    dati.append(riga)
            return dati
        except FileNotFoundError:
            print(f"Errore: Il file '{self.name}' non esiste.")
            return []


# --- Esempio di utilizzo dell'Esercizio 2 ---
# (Assicurati di avere un file "dati.csv" nella stessa cartella per testarlo)
if __name__ == "__main__":
    # Creiamo un file di test al volo per l'esempio
    import os
    with open("dati.csv", "w", encoding="utf-8") as f:
        f.write("01-01-2012,266.0\n")
        f.write("01-02-2012,145.9\n")

    # Utilizzo della classe CSVFile
    mio_file_csv = CSVFile("dati.csv")
    print(f"\nNome del file memorizzato nell'attributo 'name': {mio_file_csv.name}")
    
    lista_dati = mio_file_csv.get_data()
    print("Dati estratti dal file (lista di liste):")
    print(lista_dati)

    # Pulizia del file di test creato
    if os.path.exists("dati.csv"):
        os.remove("dati.csv")