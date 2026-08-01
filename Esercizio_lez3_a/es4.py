def hanno_elementi_comuni(lista1,lista2):
    for elemento in lista1 :
        if elemento in lista2 :
            return True
    return False

print(hanno_elementi_comuni([1,2],[2,3]))