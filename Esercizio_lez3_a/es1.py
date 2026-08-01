def somma_elementi(lista) :
    totale = 0
    for numero in lista :

        totale += numero
    return totale

lista = [1,2,3]
print(somma_elementi(lista))
