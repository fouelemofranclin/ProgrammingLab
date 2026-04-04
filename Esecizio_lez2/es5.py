n = int(input("inserisci un numero per verificare se è primo"))
contatore_divisore = 0

for i in range (1, n+1):
    if n % i == 0 :
        contatore_divisori += 1

if contatore_divisore == 2 :
    print(f"{n} è un numero primo")
else:
    print(f"{n} non è un numero primo")            