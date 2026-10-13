class Prestiti:
    def __init__(self, codice_prestito, data,  codice_strumento, cognome):
        self.__codice_prestito = codice_prestito
        self.__data = data
        self.__codice_strumento = codice_strumento
        self.__cognome = cognome

    @property
    def codice_prestito(self):
        return self.__codice_prestito

    @property
    def codice_strumento(self):
        return self.__codice_strumento

    def __str__(self):
        return f"{self.__codice_prestito}, {self.__data}, {self.__codice_strumento}, {self.__cognome} "

lista_prestiti = []