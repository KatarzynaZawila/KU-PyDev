# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej
bok1 = float(input())
bok2 = float(input())
bok3 = float(input())


if bok1 <= 0 or bok2 <= 0 or bok3 <=0 or bok1+bok2<=bok3 or bok1+bok3<=bok2 or bok3+bok2<=bok1:
    print("Nie da się zbudować trójkąta") 
else:
    if bok1 == bok2 ==bok3:
        print("równoboczny")
    elif bok1==bok2 or bok1==bok3 or bok2==bok3:
        print("równoramienny")
    else:
        print("różnoboczny")

    najdluzszy_bok = max(bok1, bok2, bok3)
    twierdzenie_Pitagorasa = bok1**2 + bok2**2 + bok3**2 - najdluzszy_bok**2

    if abs(twierdzenie_Pitagorasa - najdluzszy_bok**2) < 1e-9:
        print("prostokątny")

