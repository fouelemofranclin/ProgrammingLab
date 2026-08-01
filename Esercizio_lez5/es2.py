class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def __str__(self):
        return f"Veicolo: {self.marca} {self.modello}"


# Sottoclasse Auto
class Auto(Veicolo):
    def __init__(self, marca, modello, numero_porte):
        # Richiamo il costruttore della classe base (Veicolo)
        super().__init__(marca, modello)
        self.numero_porte = numero_porte

    def __str__(self):
        # Estendo il metodo __str__ sfruttando super()
        return f"{super().__str__()} | Porte: {self.numero_porte}"


# Sottoclasse Moto
class Moto(Veicolo):
    def __init__(self, marca, modello, tipo):
        super().__init__(marca, modello)
        self.tipo = tipo  # Es. "Sportiva", "Touring", ecc.

    def __str__(self):
        return f"{super().__str__()} | Tipo: {self.tipo}"


# --- TEST EX 2 ---
print("\n--- Test Esercizio 2 ---")
mia_auto = Auto("Fiat", "500", 3)
mia_moto = Moto("Ducati", "Monster", "Sportiva")

print(mia_auto)
print(mia_moto)