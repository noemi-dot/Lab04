class Cabina:
    def __init__(self, codice_cabina, letti, ponte, prezzo_base):
        self.codice_cabina = codice_cabina
        self.letti = letti
        self.ponte = ponte
        self.prezzo_base = prezzo_base
        self.disponibile = True


class Animale(Cabina):
