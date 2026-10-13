import deposito_strumenti
from datetime import datetime

def menu():
    print("\n--- MENU DEPOSITO STRUMENTI ---")
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento (da tastiera)")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Esci")
    return input("Scegli un'opzione >> ").strip()

def main():
    deposito = deposito_strumenti.DepositoStrumenti("Deposito Strumenti Civico", "Alessandro Visconti")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ")
            deposito.responsabile = nuovo_responsabile

        elif scelta == "2":
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    deposito.carica_file_strumenti(file_path)
                    break
                except FileNotFoundError:
                    print("Non è stato trovato nessun file con questo nome")

        elif scelta == "3":
            if len(deposito_strumenti.strumenti.lista_strumenti) >= 1:
                codice = "S" + str(int(deposito_strumenti.strumenti.lista_strumenti[-1].codice[1:]) + 1)
            else:
                codice = "S1"
            tipo = input("Tipo di strumento: ")
            marca = input("Marca: ")
            try:
                anno_acquisto = int(input("Anno di acquisto: ").strip())
                valore = float(input("Valore (euro): ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno e valore.")
                continue
            strumento = deposito.aggiungi_strumento(codice, tipo, marca, anno_acquisto, valore)
            print(f"Strumento aggiunto: {strumento}")
            deposito_strumenti.strumenti.lista_strumenti.append(strumento)

        elif scelta == "4":
            if len(deposito_strumenti.strumenti.lista_strumenti) == 0:
                print("Inserire prima degli strumenti")
            else:
                strumenti_ordinati = deposito.strumenti_ordinati_per_marca()
                for s in strumenti_ordinati:
                    print(s)

        elif scelta == "5":
            if len(deposito_strumenti.strumenti.lista_strumenti) == 0:
                print("Inserire prima degli strumenti")
            else:
                try:
                    strumento_trovato = False
                    id_strumento = input("ID strumento: ")
                    for i in deposito_strumenti.strumenti.lista_strumenti:
                        if i.codice == id_strumento:
                            strumento_trovato = True
                    strumento_già_prestato = False
                    for i in deposito_strumenti.prestiti.lista_prestiti:
                        if i.codice_strumento == id_strumento:
                            strumento_già_prestato = True
                    if strumento_già_prestato:
                        print("Lo strumenot è già in prestito")
                        raise Exception
                    elif not strumento_trovato:
                        print("Non è stato trovato alcuno strumeno con questo codice")
                        raise Exception
                    else:
                        cognome_allievo = input("Cognome allievo: ")
                        data = datetime.now().date()
                        prestito = deposito.nuovo_prestito(data, id_strumento, cognome_allievo)
                        print(f"Prestito andato a buon fine: {prestito}")
                        deposito_strumenti.prestiti.lista_prestiti.append(prestito)
                except Exception:
                    print("Non è stato possibile eseguire il prestito")

        elif scelta == "6":
            id_prestito = input("ID prestito da terminare: ").strip()
            deposito.termina_prestito(id_prestito)

        elif scelta == "7":
            print("Uscita dal programma...")
            break

        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()
