def calcola_quadrato():
    while True:
        # 1. Chiediamo l'input all'utente
        valore_input = input("Inserisci un numero intero: ")
        
        try:
            # 2. Tentiamo di convertire l'input in un numero intero
            numero = int(valore_input)
            
            # 3. Se la conversione riesce, calcoliamo il quadrato ed usciamo dal ciclo
            quadrato = numero ** 2
            print(f"Il quadrato di {numero} è {quadrato}.")
            break 
            
        except ValueError:
            # 4. Se la conversione fallisce, stampiamo l'errore e il ciclo ricomincia
            print("Errore: Il valore inserito non è un numero intero valido. Riprova.\n")

# Avvio del programma
if __name__ == "__main__":
    calcola_quadrato()