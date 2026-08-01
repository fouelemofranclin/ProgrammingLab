def dizionario_file(nome_file):
    conteggio = {}
    with open(nome_file, 'r') as file:
        for riga in file:
            parole = riga.split()
            for p in parole:
                p_pulita = p.strip(",.!?").lower()
                conteggio[p_pulita] = conteggio.get(p_pulita, 0) + 1
    return conteggio