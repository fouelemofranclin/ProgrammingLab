class Veicolo:
    def __init__(self, anno, modello, marca):
        """
        Inizializza il veicolo con anno, modello e marca.
        La velocità iniziale viene impostata a 0.
        """
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0

    def __str__(self):
        """
        Restituisce una rappresentazione testuale dei dettagli del veicolo.
        """
        return f"Veicolo: {self.marca} {self.modello} ({self.anno}) - Velocità: {self.speed} km/h"

    def accellerare(self):
        """
        Incrementa la velocità di 5 unità.
        """
        self.speed += 5

    def frenare(self):
        """
        Decrementa la velocità di 5 unità, evitando che diventi negativa.
        """
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        """
        Restituisce la velocità corrente.
        """
        return self.speed


# --- Esempio di utilizzo dell'Esercizio 1 ---
if __name__ == "__main__":
    # Creazione di un'istanza di Veicolo
    auto = Veicolo(2020, "500", "Fiat")
    print(auto)  # Richiama automaticamente il metodo __str__

    # Accelerazione
    print("\nAccelerazione in corso...")
    auto.accellerare()
    auto.accellerare()
    print(f"Velocità corrente (get_speed): {auto.get_speed()} km/h")
    print(auto)

    # Frenata
    print("\nFrenata in corso...")
    auto.frenare()
    print(auto)