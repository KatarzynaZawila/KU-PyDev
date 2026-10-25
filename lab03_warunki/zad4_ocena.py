# Lab 03 – Zadanie 4 (★): Ocena z przedmiotu
#
# Program wczytuje liczbę punktów (0–100) i wypisuje ocenę według progów
# z sylabusa naszego przedmiotu:
#     > 91        -> 5
#     > 83 – 91   -> 4.5
#     > 75 – 83   -> 4
#     > 67 – 75   -> 3.5
#     > 60 – 67   -> 3
#     <= 60       -> 2
#
# Przykład:  Ocena: 4.5
# Uwaga: w zachęcie input() nie wypisuj liczb (np. „0-100”) – testy szukają liczb w wyjściu.

# TODO: Twój kod poniżej
punkty = int(input())
if punkty<0 or punkty>100:
    print("Nieprawidłowa liczba punktów.")
elif punkty>91:
    print("5")
elif punkty > 83:
    print("4.5")  
elif punkty > 75:
    print ("4")
elif punkty > 67:
    print("3.5")
elif punkty > 60 :
    print("3")
else:
    print("2")