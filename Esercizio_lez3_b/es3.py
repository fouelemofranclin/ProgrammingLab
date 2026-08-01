def conta_parola_file(nome_file, parola_cercata):
    conteggio = 0
    with open(nome_file, 'r') as file:
        for riga in file:
            parole = riga.split()
            for p in parole:
                if p.strip(",.!?").lower() == parola_cercata.lower():
                    conteggio += 1
    return conteggio