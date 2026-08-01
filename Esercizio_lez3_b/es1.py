def conteggio_parole(lista_parole):
    dizionario = {}
    for parola in lista_parole:
        dizionario[parola] = dizionario.get(parola, 0) + 1
    return dizionario


lista_parole = [1,2,3]

print(conteggio_parole(lista_parole))
