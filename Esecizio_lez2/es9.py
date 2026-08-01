def conta_vocali(stringa):
    vocali = "aeiouAEIOU"
    conteggio = 0
    
    for carattere in stringa:
        if carattere in vocali:
            conteggio += 1
            
    return conteggio

# Esempio di utilizzo:
testo = "Ciao a tutti!"
risultato = conta_vocali(testo)
print(f"Numero di vocali: {risultato}")  # Output: 5