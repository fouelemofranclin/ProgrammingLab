class Poligono:
    def __init__(self, numero_lati):
        self.numero_lati = numero_lati

    def descrizione(self):
        return f"Sono un poligono con {self.numero_lati} lati"


# Quadrilatero eredita da Poligono
class Quadrilatero(Poligono):
    def __init__(self):
        # Un quadrilatero ha sempre 4 lati, lo passiamo direttamente a super()
        super().__init__(4)

    def descrizione(self):
        return "Sono un quadrilatero"


# Rettangolo eredita da Quadrilatero
class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init__() # Inizializza come Quadrilatero (4 lati)
        self.base = base
        self.altezza = altezza

    def descrizione(self):
        # Sovrascriviamo includendo base e altezza
        return f"{super().descrizione()} (Rettangolo) con base {self.base} e altezza {self.altezza}"

    def perimetro(self):
        return (self.base + self.altezza) * 2

    def area(self):
        return self.base * self.altezza


# Triangolo eredita da Poligono
class Triangolo(Poligono):
    def __init__(self, lato1, lato2, lato3):
        super().__init__(3) # Un triangolo ha sempre 3 lati
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

    def descrizione(self):
        return f"Sono un triangolo con lati di lunghezza: {self.lato1}, {self.lato2}, {self.lato3}"

    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3

    def is_equilatero(self):
        # Restituisce True se tutti e tre i lati sono uguali
        return self.lato1 == self.lato2 == self.lato3


# --- TEST EX 4 ---
print("\n--- Test Esercizio 4 ---")

p = Poligono(5)
print(p.descrizione())

q = Quadrilatero()
print(q.descrizione())

r = Rettangolo(10, 5)
print(r.descrizione())
print(f"Perimetro Rettangolo: {r.perimetro()} | Area Rettangolo: {r.area()}")

t1 = Triangolo(3, 4, 5)
print(t1.descrizione())
print(f"Perimetro Triangolo 1: {t1.perimetro()} | È equilatero? {t1.is_equilatero()}")

t2 = Triangolo(6, 6, 6)
print(f"Triangolo 2 è equilatero? {t2.is_equilatero()}")