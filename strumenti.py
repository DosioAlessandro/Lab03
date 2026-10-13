class Strumenti:
    def __init__(self, codice, tipo, marca, anno, valore):
        self.__codice = codice
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = anno
        self.__valore = valore

    @property
    def codice(self):
        return self.__codice

    @property
    def marca(self):
        return self.__marca

    def __str__(self):
        return f"{self.__codice}, {self.__tipo}, {self.__marca}, {self.__anno_acquisto}, {self.__valore}"

lista_strumenti = []