def somma_vendite_shampoo(nome_file):
    totale = 0.0
    with open(nome_file, 'r') as file:
        for riga in file:
            try:
                # Supponendo che il valore sia l'unico dato o l'ultimo della riga
                valore = float(riga.strip().split(',')[-1])
                totale += valore
            except ValueError:
                continue # Salta intestazioni o righe vuote
    return totale