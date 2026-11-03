# Lab 04 – Zadanie 5 (☆, dodatkowe): Mini-crawler
#
# Crawler (robot sieciowy) przegląda strony i zbiera z nich linki.
# Przeczytaj plik dane/strona.html i:
#   1. policz wszystkie linki – wystąpienia tekstu  href="
#   2. wypisz domeny linków bez powtórzeń, np. docs.python.org
#
# Wynik:
#     Liczba linków: 5
#     www.python.org
#     docs.python.org
#     ...
#
# Wskazówki:
#   - text.find('href="', start) zwraca pozycję albo -1 – szukaj w pętli while
#   - adres kończy się na kolejnym znaku "
#   - domena to fragment między "://" a pierwszym "/" po nim
#   - (dla chętnych) urllib.request.urlopen pobierze prawdziwą stronę

with open("dane/strona.html", encoding="utf-8") as f:
    html = f.read()

# TODO: Twój kod poniżej
liczba_linkow = 0
domeny = []
start = 0

while True:
    pozycja = html.find('href="', start)

    if pozycja == -1:
        break

    liczba_linkow += 1

    poczatek = pozycja + 6
    koniec = html.find('"', poczatek)

    adres = html[poczatek:koniec]

    poczatek_domeny = adres.find("://") + 3
    koniec_domeny = adres.find("/", poczatek_domeny)

    if koniec_domeny == -1:
        domena = adres[poczatek_domeny:]
    else:
        domena = adres[poczatek_domeny:koniec_domeny]

    if domena not in domeny:
        domeny.append(domena)

    start = koniec + 1

print(f"Liczba linków: {liczba_linkow}")

for domena in domeny:
    print(domena)