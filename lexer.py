import re
from tokens import RULES

class AnalizatorLeksykalny:
    def __init__(self, tekst):
        self.tekst = tekst
        self.pozycja = 0
        self.reguly = [(nazwa, re.compile(wzorzec)) for nazwa, wzorzec in RULES]

    def skaner(self):
        if self.pozycja >= len(self.tekst):
            return None

        for nazwa, regex in self.reguly:
            dopasowanie = regex.match(self.tekst, self.pozycja)
            if dopasowanie:
                wartosc = dopasowanie.group(0)
                kolumna = self.pozycja + 1
                self.pozycja = dopasowanie.end()
                return (nazwa, wartosc, kolumna)

        raise RuntimeError(f"Błąd leksykalny w kolumnie {self.pozycja + 1}: nierozpoznany znak '{self.tekst[self.pozycja]}'")
