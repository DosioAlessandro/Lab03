import csv
from operator import attrgetter
import strumenti
import prestiti

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile

    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self.__responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, "r", newline = "") as file:
            f_letto = csv.reader(file)
            for riga in f_letto:
                s = strumenti.Strumenti(riga[0], riga[1], riga[2], riga[3], riga[4])
                strumenti.lista_strumenti.append(s)

    def aggiungi_strumento(self, codice, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        s = strumenti.Strumenti(codice, tipo, marca, anno_acquisto, valore)
        return s

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        l = sorted(strumenti.lista_strumenti, key=attrgetter("marca"))
        return l

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if len(prestiti.lista_prestiti) == 0:
            codice = ("P1")
        else:
            codice = "P" + str(int(prestiti.lista_prestiti[-1].codice_prestito[1:]) + 1)
        p = prestiti.Prestiti(codice, data, id_strumento, cognome_allievo)
        return p

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        try:
            prestito_trovato = False
            for i in prestiti.lista_prestiti:
                if i.codice_prestito == id_prestito:
                    prestito_trovato = True
                    prestiti.lista_prestiti.remove(i)
            if prestito_trovato:
                print(f"Prestito {id_prestito} terminato con successo.")
            else:
                raise Exception
        except Exception:
            print("Non è stato trovato alcun prestito con questo codice")





