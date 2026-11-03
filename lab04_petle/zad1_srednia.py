# Lab 04 – Zadanie 1 (★): Średnia ocen
#
# Program wczytuje oceny (float), każdą w osobnej linii, aż użytkownik
# wciśnie Enter w pustej linii. Potem wypisuje średnią z 2 miejscami, np.:
#     Średnia ocen: 4.00
# Jeśli nie podano żadnej oceny, wypisz: Brak ocen
#
# Wskazówki:
#   - pętla while True + break, gdy linia jest pusta
#   - licz sumę i liczbę ocen w dwóch zmiennych

# TODO: Twój kod poniżej
liczba_ocen = 0.0
suma_ocen = 0.0

while True:
    wpis = input()
    if wpis == "":
        break
    ocena = float(wpis)
    suma_ocen += ocena
    liczba_ocen +=1

if liczba_ocen == 0:
    print("Brak ocen")
else:
    srednia = suma_ocen / liczba_ocen
    print(f"Średnia ocen: {srednia:.2f}")
