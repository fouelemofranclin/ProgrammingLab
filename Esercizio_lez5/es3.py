class Corso:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Corso({self.nome})"


class Docente:
    def __init__(self, nome):
        self.nome = nome
        self.corsi_insegnati = set()  # Usiamo i set per una ricerca più efficiente

    def aggiungi_corso(self, corso):
        self.corsi_insegnati.add(corso)

    # --- PUNTO 1 ---
    def insegna_tutto_a(self, studente):
        """
        Verifica se questo docente insegna TUTTI i corsi frequentati dallo studente.
        Restituisce True se i corsi dello studente sono un sottoinsieme dei corsi insegnati.
        """
        if not studente.corsi_frequentati:
            return False # Se lo studente non frequenta corsi, il confronto non ha senso
            
        return studente.corsi_frequentati.issubset(self.corsi_insegnati)


class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.corsi_frequentati = set()

    def iscrivi_a_corso(self, corso):
        self.corsi_frequentati.add(corso)


# --- PUNTO 2 ---
def verifica_copertura_studenti(lista_studenti, lista_docenti):
    """
    Verifica che, per OGNI studente, esista almeno un docente 
    che insegni tutti i corsi frequentati da quello studente.
    Utilizza la funzione del Punto 1.
    """
    for studente in lista_studenti:
        # Verifichiamo se esiste ALMENO un docente che copre tutti i suoi corsi
        coperto = any(docente.insegna_tutto_a(studente) for docente in lista_docenti)
        
        # Se anche solo uno studente non ha un docente che copre tutti i suoi corsi, restituisce False
        if not coperto:
            print(f"Attenzione: Lo studente {studente.nome} frequenta corsi non coperti interamente da un singolo docente.")
            return False
            
    return True




Esempio di Test

Ecco come puoi testare il codice per verificarne il corretto funzionamento:

# Creazione dei corsi
matematica = Corso("Matematica")
fisica = Corso("Fisica")
programmazione = Corso("Programmazione")

# Creazione dei docenti e assegnazione corsi
prof_rossi = Docente("Prof. Rossi")
prof_rossi.aggiungi_corso(matematica)
prof_rossi.aggiungi_corso(fisica)

prof_bianchi = Docente("Prof. Bianchi")
prof_bianchi.aggiungi_corso(programmazione)

# Creazione degli studenti e iscrizione ai corsi
studente_a = Studente("Alice")
studente_a.iscrivi_a_corso(matematica)
studente_a.iscrivi_a_corso(fisica) # Rossi insegna entrambi

studente_b = Studente("Bob")
studente_b.iscrivi_a_corso(programmazione) # Bianchi lo insegna

# --- Test Punto 1 ---
print("--- Test Punto 1 ---")
print(f"Il Prof. Rossi insegna tutti i corsi di Alice? {prof_rossi.insegna_tutto_a(studente_a)}") # True
print(f"Il Prof. Bianchi insegna tutti i corsi di Alice? {prof_bianchi.insegna_tutto_a(studente_a)}") # False

# --- Test Punto 2 ---
print("\n--- Test Punto 2 ---")
studenti = [studente_a, studente_b]
docenti = [prof_rossi, prof_bianchi]

tutti_coperti = verifica_copertura_studenti(studenti, docenti)
print(f"Tutti gli studenti hanno i corsi coperti da almeno un docente? {tutti_coperti}") # True