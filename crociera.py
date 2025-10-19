import csv
from cabina import Cabina,CabinaAnimali,CabinaDeluxe
from passeggeri import Passeggeri

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome=nome
        self.cabine=[]
        self.passeggeri=[]

    """Aggiungere setter e getter se necessari"""

    def get_nome(self):
        return self._nome

    def set_nome(self, nuovo_nome):
        if nuovo_nome.strip():
            self._nome = nuovo_nome.strip()
        else:                                #se contiene una stringa vuota o fatta solo da spazi
            print("Nome non valido")

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader=csv.reader(file)
                righe = [riga for riga in reader]
                for line in righe:
                    codice=line[0].upper()
                    if codice.startswith("CAB"):
                        letti=int(line[1])
                        ponte=int(line[2])
                        prezzo_base=float(line[3])
                        cabina=Cabina(codice,letti,ponte,prezzo_base)
                        if len(line)==5:
                            extra=line[4]
                            if extra.isdigit():   #se è un numero, l'extra si riferisce agli animali
                                cabina=CabinaAnimali(codice,letti,ponte,prezzo_base,extra)
                            else:
                                cabina=CabinaDeluxe(codice,letti,ponte,prezzo_base,extra)
                        self.cabine.append(cabina)
                    elif codice.startswith("P"):
                        nome=line[1]
                        cognome=line[2]
                        passeggero=Passeggeri(codice,nome,cognome)
                        self.passeggeri.append(passeggero)

        except FileNotFoundError:
            print("File non trovato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        cabina=None
        for c in self.cabine:
            if c.codice_cabina==codice_cabina:
                cabina=c
                break
        if cabina is None:
            print(f"cabina {codice_cabina} non trovata")

        passeggero=None
        for p in self.passeggeri:
            if p.codice_passeggero==codice_passeggero:
                passeggero=p
                break
        if passeggero is None:
            print(f"passeggero {codice_passeggero} non trovato")

        if cabina.disponibile is not True:
            print(f" cabina {codice_cabina} non disponibile")

        if passeggero.cabina is not None:
            print(f"il passeggero {codice_passeggero} ha già una cabina assegnata")

        passeggero.cabina = cabina         #assegno la cabina al passeggero
        cabina.disponibile = False         #rendo non più disponibile la cabina
        print(f"Passeggero {codice_passeggero} assegnato alla cabina {codice_cabina}")

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        cabine_ordinate=sorted(self.cabine, key=lambda c:c.calcola_prezzo())

        print(cabine_ordinate)
        return cabine_ordinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for p in self.passeggeri:
            if p.cabina is not None:
                print(f"{p.codice_passeggero}: {p.nome}, {p.cognome}. Cabina {p.cabina.codice_cabina}")
            else:
                print(f"{p.codice_passeggero}: {p.nome}, {p.cognome}-----nessuna cabina è stata ancora assegnata")



