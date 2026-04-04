def tipo_triangolo(a,b,c) :
    if (a+b > c) and (a+c > b) and (b+c>a):
        if a == b == c : 
            return "triangolo equilatero"
        elif a == b or b == c or a == c :
            return "triangolo isoscele"
        else:
            return "triangolo scaleno"
    else:
        return "questi valori non possono formare un triangolo"
    


    print(tipo_triangolo(3,4,5))