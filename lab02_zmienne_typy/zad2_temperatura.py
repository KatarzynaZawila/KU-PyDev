# Lab 02 – Zadanie 2 (★): Konwerter temperatury
#
# 1. Wczytaj temperaturę w stopniach Celsjusza i wypisz ją w Fahrenheitach:
#        F = C * 9 / 5 + 32
# 2. Wczytaj temperaturę w stopniach Fahrenheita i wypisz ją w Celsjuszach:
#        C = (F - 32) * 5 / 9
#
# Przykład: 37 °C = 98.6 °F,  212 °F = 100.0 °C
# Wyniki zaokrąglij do 1 miejsca po przecinku: f"{x:.1f}"

# TODO: Twój kod poniżej
C = float(input())
F = float(input())
zmiana_C_na_F = C * 9 / 5 + 32
zmiana_F_na_C = (F - 32) * 5 / 9
print(f"{C} °C = {zmiana_C_na_F:.1f}°F")
print(f"{F} °F = {zmiana_F_na_C:.1f} °C")
