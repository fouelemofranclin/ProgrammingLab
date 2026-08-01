def mostra_menu():
    while True:
        # 1. Stampa del Menù principale
        print("--- MENÙ OPERAZIONI ---")
        print("1. Calcolare la somma di due numeri")
        print("2. Calcolare la differenza tra due numeri")
        print("3. Uscire")
        
        scelta = input("Scegli un'opzione (1, 2 o 3): ").strip()
        print() # Riga vuota per formattazione

        # 2. Gestione dell'opzione 1: Somma
        if scelta == "1":
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
                print(f"-> Risultato della somma: {num1} + {num2} = {num1 + num2}\n")
            except ValueError:
                print("Errore: Devi inserire dei numeri validi!\n")

        # 3. Gestione dell'opzione 2: Differenza
        elif scelta == "2":
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
                print(f"-> Risultato della differenza: {num1} - {num2} = {num1 - num2}\n")
            except ValueError:
                print("Errore: Devi inserire dei numeri validi!\n")

        # 4. Gestione dell'opzione 3: Uscita dal programma
        elif scelta == "3":
            print("Grazie per aver usato il programma. Arrivederci!")
            break # Interrompe il ciclo while ed esce

        # 5. Gestione input non valido per il menù
        else:
            print("Errore: Opzione non valida. Inserisci solo 1, 2 o 3.\n")

# Avvio del programma
if __name__ == "__main__":
    mostra_menu()