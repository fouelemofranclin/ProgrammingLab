import csv

class CSVFile:
    def __init__(self, name):
        """
        Inizializza l'oggetto con il nome del file.
        """
        self.name = name

    def get_data(self):
        """
        Legge il file CSV e restituisce i dati sotto forma di lista di liste.
        """
        data = []
        try:
            with open(self.name, mode='r', encoding='utf-8') as file:
                # csv.reader legge ogni riga come una lista di stringhe
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Errore: Il file '{self.name}' non è stato trovato.")
            return []
        
        return data
    



    Come testare la classe

Se vuoi verificare che funzioni, puoi creare al volo un file di prova (ad esempio dati.csv) e poi usare la classe in questo modo:
Python

# Supponiamo di avere un file "shampoo_sales.csv" nella stessa cartella

# 1. Creiamo l'istanza della classe passando il nome del file
mio_file = CSVFile("shampoo_sales.csv")

# 2. Verifichiamo l'attributo "name"
print("Nome del file:", mio_file.name)

# 3. Estraiamo i dati con get_data()
dati_estratti = mio_file.get_data()
print("Contenuto del file:", dati_estratti)