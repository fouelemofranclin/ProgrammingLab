def rimuovi_duplicati_file(file_input):
    righe_uniche = []
    seen = set()
    
    with open(file_input, 'r') as f:
        for riga in f:
            if riga not in seen:
                righe_uniche.append(riga)
                seen.add(riga)
                
    with open('unique.txt', 'w') as f_out:
        f_out.writelines(righe_uniche)