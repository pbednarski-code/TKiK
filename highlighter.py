import html
from lexer import AnalizatorLeksykalny
from tokens import COLORS

class SyntaxHighlighter:
    def __init__(self, tekst):
        self.skaner = AnalizatorLeksykalny(tekst)

    def generuj_html(self):
        wynik = [
            "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n"
            "<style>\n"
            "body { background-color: #1E1E1E; color: #D4D4D4; font-family: 'Courier New', Courier, monospace; padding: 20px; }\n"
            "pre { margin: 0; }\n"
            "</style>\n"
            "</head>\n<body>\n<pre>"
        ]
        
        while True:
            token = self.skaner.skaner()
            if token is None:
                break
            
            nazwa, wartosc, _ = token
            wartosc_html = html.escape(wartosc)
            kolor = COLORS.get(nazwa)
            
            if kolor:
                wynik.append(f'<span style="color: {kolor};">{wartosc_html}</span>')
            else:
                wynik.append(wartosc_html)
                
        wynik.append("</pre>\n</body>\n</html>")
        return "".join(wynik)
