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

    def handleSpellCheck(self, txtIn, language, modality):

        if txtIn == "":
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, il campo sentence non può essere vuoto.", color="red"))
            self._view.update()         # ho cambiato da update_page() ad update() perchè in view c'è update()
            return

        if language is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, devi scegliere una lingua.", color="red"))
            self._view.update()
            return

        if modality is None:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, devi scegliere una modalità di ricerca.", color="red"))
            self._view.update()
            return

        paroleErrate, tempo = self.handleSentence(txtIn, language, modality)
        self._view._lvOut.controls.append(ft.Text(f"Frase inserita: {txtIn}"))
        self._view._lvOut.controls.append(
            ft.Text(f"Parole errate:{paroleErrate} \nTempo impiegato: {tempo} secondi"))
        self._view._txtSentence.value = ""
        self._view.update()

    def handleLanguageSelection(self, language):
        if language is not None:
            self._view._lvOut.controls.append(
                ft.Text(f"Lingua selezionata: {language}", color="green"))
        else:
            self._view._lvOut.controls.append(
                ft.Text("Errore nella selezione della lingua.", color="red"))
        self._view.update()


    def handleModalitySelection(self, modality):
        if modality is not None:
            self._view._lvOut.controls.append(
                ft.Text(f"Modalità selezionata: {modality}", color="green"))
        else:
            self._view._lvOut.controls.append(
                ft.Text("Errore nella selezione della modalità.", color="red"))
        self._view.update()

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


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

