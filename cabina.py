class Cabina:
    def __init__(self, codice_cabina, letti, ponte, prezzo_base):
        self.codice_cabina = codice_cabina
        self.letti = letti
        self.ponte = ponte
        self.prezzo_base = prezzo_base
        self.disponibile = True


    def calcola_prezzo(self):
        #Prezzo standard
        return self.prezzo_base

    def __str__(self):
        if self.disponibile==True:
            stato="Disponibile"
        else:
            stato="Occupata"

        return f"{self.codice_cabina}: {self.letti} letti - Ponte {self.ponte} - Prezzo {self.calcola_prezzo()}€ - {stato}"

class CabinaAnimali(Cabina):
    def __init__(self, codice_cabina, letti, ponte, prezzo_base, max_animali):
        super().__init__(codice_cabina, letti, ponte, prezzo_base)
        self.max_animali = max_animali

    def calcola_prezzo(self):
        return self.prezzo_base * (1 + 0.10 * float(self.max_animali))

class CabinaDeluxe(Cabina):
    def __init__(self, codice_cabina, letti, ponte, prezzo_base, stile):
        super().__init__(codice_cabina, letti, ponte, prezzo_base)
        self.stile = stile

    def calcola_prezzo(self):
        return self.prezzo_base * 1.20