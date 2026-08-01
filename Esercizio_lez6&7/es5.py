from datetime import datetime

def calcola_eta_e_prossimo_compleanno():
    # 1. Input della data di nascita
    data_input = input("Inserisci la tua data di nascita (formato GG-MM-AAAA): ")
    
    try:
        # Convertiamo la stringa in un oggetto datetime
        data_nascita = datetime.strptime(data_input, "%d-%m-%m").date() if "%d-%m-%Y" else datetime.strptime(data_input, "%d-%m-%Y")
        # Correggiamo il parsing per prendere la data corretta
        data_nascita = datetime.strptime(data_input, "%d-%m-%Y")
    except ValueError:
        print("Formato data non valido! Usa il formato GG-MM-AAAA (es. 15-08-2000).")
        return

    # 2. Otteniamo il momento attuale (data e ora corrente)
    adesso = datetime.now()
    oggi = adesso.date()

    # 3. Calcolo dell'età attuale
    eta = oggi.year - data_nascita.year
    # Se il compleanno non è ancora avvenuto quest'anno, sottraiamo 1 anno
    if (oggi.month, oggi.day) < (data_nascita.month, data_nascita.day):
        eta -= 1

    print(f"\nHai {eta} anni.")

    # 4. Calcolo del prossimo compleanno (data e ora esatta: la mezzanotte di quel giorno)
    anno_prossimo_compleanno = oggi.year
    # Se il compleanno per quest'anno è già passato, il prossimo sarà l'anno prossimo
    if (oggi.month, oggi.day) >= (data_nascita.month, data_nascita.day):
        anno_prossimo_compleanno += 1

    prossimo_compleanno = datetime(
        year=anno_prossimo_compleanno, 
        month=data_nascita.month, 
        day=data_nascita.day,
        hour=0, minute=0, second=0
    )

    # 5. Calcolo del tempo mancante (sottrazione tra oggetti datetime restituisce un timedelta)
    tempo_mancante = prossimo_compleanno - adesso

    # Estraiamo i giorni
    giorni = tempo_mancante.days
    
    # I secondi rimanenti (esclusi i giorni interi) si ottengono con il resto del timedelta
    secondi_rimanenti = tempo_mancante.seconds
    
    # Calcoliamo ore, minuti e secondi dai secondi rimanenti
    ore = secondi_rimanents // 3600
    secondi_rimanenti %= 3600
    minuti = secondi_rimanenti // 60
    secondi = secondi_rimanenti % 60

    # 6. Mostriamo il countdown a schermo
    print("Al tuo prossimo compleanno mancano:")
    print(f"{giorni} giorni, {ore} ore, {minuti} minuti e {secondi} secondi.")

# Avvio del programma
if __name__ == "__main__":
    calcola_eta_e_prossimo_compleanno()