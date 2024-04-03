import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def iniziaRicerca(self, e):
        '''In questo punto aggiungiamo:
        1) I controlli: l'utente ha selezionato la lingua e la modalita? se no faglielo fare
        2) Visto che siamo nel controllore richiamiamola funzione del modello per fare effettivamente
           lo spellchecking
        3) In entrambi i casi stampiamo a video i risultati'''
        #Punto 1)
        if self._view._dd.value==None:
            self._view.lvOut.controls.append(ft.Text(f"Devi scegliere una lingua", color="red"))
            self._view.update()
            return
        if self._view._dd1.value==None:
            self._view.lvOut.controls.append(ft.Text(f"Devi scegliere la modalità di ricerca", color="red"))
            self._view.update()
            return
        if self._view._txtIn.value=="":
            self._view.lvOut.controls.append(ft.Text(f"Devi inserire una frase", color="red"))
            self._view.update()
            return
        '''Commento punto 1: ricordati che se non ci sono valori all'interno di un dropdown il valore 
           "nullo" del dropdown è None e non "" '''

        #Punto 2)
        self._view.lvOut.clean()
        testo = self._view._txtIn.value
        # per come fuzionano le ricerche vuole in ingresso la lista delle parole presenti nella
        # frase di input e non la stringa e basta
        parole = testo.split(" ")
        if self._view._dd1.value=="Default":
            risultato=self._multiDic.searchWord(parole,self._view._dd.value)
        elif self._view._dd1.value=="Lineare":
            risultato=self._multiDic.searchWordLinear(parole,self._view._dd.value)
        else:
            risultato = self._multiDic.searchWordDichotomic(parole, self._view._dd.value)
        self._view.lvOut.controls.append(ft.Text(f"La frase inserita è: {testo}", color="blue"))
        self._view.lvOut.controls.append(ft.Text(f"Gli errori sono:", color="blue"))
        for parola in risultato:
            if not(parola.corretta):
                self._view.lvOut.controls.append(ft.Text(f"{parola}", color="orange"))

        self._view.update()
        '''Ricordati che il controllore deve poter accedere sia al modello sia alla view.
           Per quanto riguarda la view il gioco è semplice: viene definito un costruttore che abbia come
           parametri in ingresso la view, quando faccio partire il main la view viene inizializzata e la posso usare
           nel controllore.
           Al contrario per poter dire al controllore quale è il modello da cui deve prendere le informazioni devo
           creare, sempre nel costruttore, un oggetto del tipo della classe modello.
           In questo caso il modello deve essere un oggetto della classe multidictionary, quindi creo, nel costruttore
           del controllore un oggetto che faccia riferimento a tale classe.
           ESSENZIALMENTE:
           1) View: deve sapere chi è il controllore e chi è la pagina per poter scambiare informazioni con questi
              due elementi e funzionare correttamente. Nel main passo alla view la pagina, attraverso il costruttore,
              e il controllore, per poter passare alla view il suo controllore devo generare un metodo nel view 
              stesso che chiamo setController
           2) Controllore: deve sapere chi è la view e chi è il modello per poter scambiare informazioni con questi
              due elementi e funzionare correttamente. Per fare questo genero due oggetti nel costruttore del
              controllore uno view e l'altro modello. Nel main passo direttamente al costruttore il valore della sua
              view, mentre l'oggetto del modello posso passarlo direttamente importando la classe desiderata come
              modello nel costruttore stesso
           IN GENERALE:
           Nella view scrivo tutti gli elementi grafici, nel modello mantengo tutta la logica del programma e nel 
           controller collego la parte logica dell'applicazione con gli  input dell'utente provenienti dall'interazione 
           con la parte grafica .
           Quella che prima era la console del programma dove stampavo e chiedevo in input i dati adesso è diventata
           la combinazione di view e page, aumentando la complessità non mi basta più avere la logica direttamente 
           collegata agli input ma è meglio avere un intermediario che aiuti, ovvero il controller'''



def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text



