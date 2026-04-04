somma = 0
while True :
    n = int(input("inserisci un numero (0 fermarti):"))
    if n == 0 :
        break
    somma += n

    print(f"La somma totale è:{somma}")