import re

class Token:
    def __init__(self, kod, wartosc, kolumna):
        self.kod = kod
        self.wartosc = wartosc
        self.kolumna = kolumna

    def __str__(self):
        return f"({self.kod:8}, '{self.wartosc}')"


class AnalizatorLeksykalny:
    def __init__(self, tekst):
        self.tekst = tekst
        self.pozycja = 0  
        
        self.reguly = [
            ('NUMBER', r'\d+'),                           # Liczba całkowita
            ('ID',     r'[a-zA-Z_][a-zA-Z0-9_]*'),        # Identyfikator
            ('PLUS',   r'\+'),                            # Działanie: dodawanie
            ('MINUS',  r'-'),                             # Działanie: odejmowanie
            ('MUL',    r'\*'),                            # Działanie: mnożenie
            ('DIV',    r'/'),                             # Działanie: dzielenie
            ('LPAREN', r'\('),                            # Nawias okrągły lewy
            ('RPAREN', r'\)'),                            # Nawias okrągły prawy
            ('SPACE',  r'[ \t\n\r]+')                     # Białe znaki
        ]
        
        czesci_regex = [f'(?P<{nazwa}>{wzorzec})' for nazwa, wzorzec in self.reguly]
        self.master_regex = re.compile('|'.join(czesci_regex))

    def skaner(self):
        """Główna funkcja skanująca, zwracająca następny poprawny token."""
        while self.pozycja < len(self.tekst):
            dopasowanie = self.master_regex.match(self.tekst, self.pozycja)
            
            if dopasowanie:
                typ_tokena = dopasowanie.lastgroup
                wartosc = dopasowanie.group(typ_tokena)
                kolumna = self.pozycja + 1 
                
                self.pozycja = dopasowanie.end()
                
                if typ_tokena == 'SPACE':
                    continue
                    
                return Token(typ_tokena, wartosc, kolumna)
            else:
                bledny_znak = self.tekst[self.pozycja]
                kolumna_bledu = self.pozycja + 1
                raise RuntimeError(
                    f"BŁĄD SKANERA: Nierozpoznany symbol '{bledny_znak}' "
                    f"w kolumnie {kolumna_bledu}."
                )
        
        return None


# TEST SKANERA
if __name__ == '__main__':
    wyrazenie = "2+3*(76+8/3)+ 3*(9-3) + zmienna ^ 2"
    
    print(f"Skanowane wyrażenie: {wyrazenie}")
    print("-" * 50)
    
    skaner_obj = AnalizatorLeksykalny(wyrazenie)
    
    try:
        while True:
            token = skaner_obj.skaner()
            if token is None:
                break
            
            print(f"{token}  [Znaleziono w kol. {token.kolumna}]")
            
    except RuntimeError as e:
        print("-" * 50)
        print(e)
