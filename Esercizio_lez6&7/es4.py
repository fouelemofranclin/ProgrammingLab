class NumericalCSVFile(CSVFile):
    
    # Sostituiamo i parametri espliciti con *args e **kwargs
    def get_data(self, *args, **kwargs):
        
        # Inoltriamo tutto al metodo get_data() di CSVFile
        original_data = super().get_data(*args, **kwargs)
        
        numerical_data = []
        
        for row in original_data:
            if not row:
                continue
                
            new_row = []
            new_row.append(row[0])  # Mantiene la data come stringa
            
            error_encountered = False
            
            for value in row[1:]:
                try:
                    new_row.append(float(value.strip()))
                except (ValueError, TypeError) as e:
                    print(f"Errore di conversione nella riga {row}: {e}")
                    error_encountered = True
                    break
            
            if not error_encountered:
                numerical_data.append(new_row)
                
        return numerical_data
    


    # Creiamo l'oggetto numerico
num_file = NumericalCSVFile("shampoo_sales.csv")

# Chiediamo solo le righe da 1 a 2. 
# La richiesta passa da NumericalCSVFile, viene inoltrata a CSVFile (che taglia le righe),
# ritorna a NumericalCSVFile (che converte in float) e infine viene restituita.
dati_filtrati_e_numerici = num_file.get_data(start=1, end=2)

print("\nRisultato filtrato e convertito:", dati_filtrati_e_numerici)