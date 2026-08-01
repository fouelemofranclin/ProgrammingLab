class Studente:
    def __init__(self, nome, cognome, corsi):
        self.nome = nome
        self.cognome = cognome
        self.corsi = corsi  # Memorizza la lista dei corsi passata come argomento

    def saluta(self):
        # Uniamo i corsi in una stringa separata da virgole per una stampa pulita
        lista_corsi = ", ".join(self.corsi)
        print(f"Ciao! Sono lo studente {self.nome} {self.cognome} e frequento i seguenti corsi: {lista_corsi}.")


class Docente:
    def __init__(self, nome, cognome, corsi):
        self.nome = nome
        self.cognome = cognome
        self.corsi = corsi  # Memorizza la lista dei corsi insegnati

    def saluta(self):
        lista_corsi = ", ".join(self.corsi)
        print(f"Buongiorno, sono il docente {self.nome} {self.cognome} e insegno i seguenti corsi: {lista_corsi}.")









        Verifica del funzionamento

Utilizzando il codice dell'esempio che hai fornito, ecco cosa succede quando lo eseguiamo:
Python

# Creazione della lista di corsi
corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]

# Istanza della classe Studente
obj_Irene = Studente("Irene", "Rossi", corsi)

# Chiamata al metodo saluta
obj_Irene.saluta()

Output a schermo:

    Ciao! Sono lo studente Irene Rossi e frequento i seguenti corsi: Programmazione, Laboratorio, Analisi, Geometria.