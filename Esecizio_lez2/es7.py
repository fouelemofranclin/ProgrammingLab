def fattoriale_iterativo(n):
    risultato = 1
    for i in range (1, n+1):
        risultato += i
        return risultato
    



    print(fattoriale_iterativo(5))