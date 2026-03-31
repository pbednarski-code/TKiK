import sys
from highlighter import SyntaxHighlighter

def glowna(plik_we, plik_wy):
    try:
        with open(plik_we, 'r', encoding='utf-8') as f:
            tekst = f.read()
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {plik_we}")
        return

    highlighter = SyntaxHighlighter(tekst)
    
    try:
        html_output = highlighter.generuj_html()
    except RuntimeError as e:
        print(e)
        return

    with open(plik_wy, 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"Pomyślnie wygenerowano plik: {plik_wy}")

if __name__ == '__main__':
    plik_wejsciowy = "input.txt"
    plik_wyjsciowy = "output.html"
    
    if len(sys.argv) == 3:
        plik_wejsciowy = sys.argv[1]
        plik_wyjsciowy = sys.argv[2]
        
    glowna(plik_wejsciowy, plik_wyjsciowy)
