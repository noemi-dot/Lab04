import csv
from cabina import Cabina
from passeggeri import Passeggeri

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.cabina=[]
        self.passeggero=[]

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader=csv.reader(file)

                righe = [riga for riga in reader]
                for line in righe:
                    if line[0][0].upper()== "C":
                        self.cabina.append(line[0])

                    elif line[0][0].upper()== "P":
                        self.passeggeri.append(line[0])


        except FileNotFoundError:
            print("File non trovato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

