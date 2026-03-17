import re

class AnalizatorLeksykalny:
    def __init__(self, tekst):
        self.tekst = tekst
        self.pozycja = 0
        self.reguly = [
            ('NUMBER', r'\d+'),
            ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MUL', r'\*'),
            ('DIV', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('SPACE', r'[ \t\n\r]+')
        ]

    def skaner(self):
        while self.pozycja < len(self.tekst):
            for nazwa, wzorzec in self.reguly:
                regex = re.compile(wzorzec)
                dopasowanie = regex.match(self.tekst, self.pozycja)
                if dopasowanie:
                    wartosc = dopasowanie.group(0)
                    kolumna = self.pozycja + 1
                    self.pozycja = dopasowanie.end()
                    if nazwa == 'SPACE':
                        break
                    return (nazwa, wartosc, kolumna)
            else:
                raise RuntimeError(f"Błąd w kolumnie {self.pozycja + 1}")
        return None


if __name__ == '__main__':
    wyrazenie = "2+3*(76+8/3)+ 3*(9-3) + zmienna"
    skaner = AnalizatorLeksykalny(wyrazenie)

    while True:
        token = skaner.skaner()
        if token is None:
            break
        print(token)
