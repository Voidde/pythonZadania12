import datetime

miesiace_koszty = {
    "Styczen": 2000,
    "Luty": 1230,
    "Marzec":2300,
    "Kwieceien": 1600,
    "Maj": 1800,
    "Czerwiec":1900,
    "Lipiec":2100,
    "Sierpien":3000,
    "Wrzesien":2500,
}

minimum = min(miesiace_koszty.values())
maximum = max(miesiace_koszty.values())
srednia = sum(miesiace_koszty.values()) / len(miesiace_koszty)

obecna_data = datetime.datetime.now()

obecny_miesiac = obecna_data.month

x = obecny_miesiac - 2

ostatni_miesiac = list(miesiace_koszty.keys())[x]

ostatni_miesiac_kwota = miesiace_koszty[ostatni_miesiac]

if(ostatni_miesiac_kwota > srednia):
    print("Zacznij oszczedzac")
else:
    print("Jestes bezpieczny")

#print(f"Wartośc srednia wynosi: {srednia:}")

for msc,koszt in miesiace_koszty.items():
    if(koszt > srednia):
        print(f"{msc}: {koszt}")

