import csv

class CSVFile:
    def __init__(self, name):
        # Inizializziamo l'attributo col nome del file
        self.name = name

    def get_data(self):
        data = []
        
        # Tentiamo di aprire il file
        try:
            with open(self.name, mode='r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    data.append(row)
        except FileNotFoundError:
            # Se il file non esiste, stampiamo il messaggio di errore
            print(f"Errore: Il file '{self.name}' non esiste.")
            return [] # Ritorniamo una lista vuota per non bloccare il programma
            
        return data
    



    import csv

class CSVFile:
    def __init__(self, name):
        self.name = name
        
        # Verifichiamo subito se il file esiste provando ad aprirlo
        try:
            with open(self.name, mode='r', encoding='utf-8') as file:
                file.readline() # Leggiamo solo la prima riga per test
        except FileNotFoundError:
            print(f"Errore: Il file '{self.name}' non esiste.")

    def get_data(self):
        data = []
        # Avendo già fatto il controllo prima, ipotizziamo che qui il file esista 
        # (anche se per sicurezza il try-except è sempre consigliato)
        try:
            with open(self.name, mode='r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    data.append(row)
        except FileNotFoundError:
            return []
            
        return data