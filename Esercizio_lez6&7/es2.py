class NumericalCSVFile(CSVFile):
    
    def get_data(self, start=None, end=None):
        # 1. Chiamiamo la get_data originale della classe madre
        original_data = super().get_data(start, end)
        
        numerical_data = []
        
        # 2. Iteriamo su ogni riga del file appena letto
        for row in original_data:
            # Saltiamo eventuali righe completamente vuote
            if not row:
                continue
                
            new_row = []
            # La prima colonna (la data) deve rimanere una stringa
            new_row.append(row[0])
            
            # Flag per tracciare se si verifica un errore in questa riga
            error_encountered = False
            
            # 3. Proviamo a convertire tutte le altre colonne in float
            for value in row[1:]:
                try:
                    # Rimuoviamo eventuali spazi bianchi prima della conversione
                    new_row.append(float(value.strip()))
                except (ValueError, TypeError) as e:
                    # Stampiamo l'errore a schermo come richiesto
                    print(f"Errore di conversione nella riga {row}: {e}")
                    error_encountered = True
                    break  # Interrompiamo il ciclo su questa riga ed usciamo
            
            # 4. Se la riga non ha generato errori, la aggiungiamo ai dati finali
            if not error_encountered:
                numerical_data.append(new_row)
                
        return numerical_data
    




    # Script di test
if __name__ == "__main__":
    # Creiamo un file di test per simulare lo scenario
    with open("shampoo_sales.csv", "w", encoding="utf-8") as f:
        f.write("01-01-2012,266.0\n")
        f.write("01-02-2012,145.9\n")
        f.write("01-01-2015,\n")       # Errore: manca il valore dopo la virgola
        f.write("01-02-2015,ciao\n")   # Errore: "ciao" non è convertibile in float
        f.write("01-03-2012,183.1\n")

    print("--- Avvio lettura con NumericalCSVFile ---")
    num_file = NumericalCSVFile("shampoo_sales.csv")
    dati_finali = num_file.get_data()
    
    print("\n--- Elaborazione completata ---")
    print("Dati finali salvati nella lista:")
    print(dati_finali)