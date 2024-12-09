# Functies voor de bewerkingen
def optellen(x, y):
    return x + y

def aftrekken(x, y):
    return x - y

def vermenigvuldigen(x, y):
    return x * y

def delen(x, y):
    if y == 0:
        return "Fout: Delen door nul is niet toegestaan"
    return x / y

# Gebruikerstinput
print("Selecteer een bewerking:")
print("1. Optellen")
print("2. Aftrekken")
print("3. Vermenigvuldigen")
print("4. Delen")

keuze = input("Voer je keuze in (1/2/3/4): ")

getal1 = float(input("Voer het eerste getal in: "))
getal2 = float(input("Voer het tweede getal in: "))

if keuze == '1':
    print(f"{getal1} + {getal2} = {optellen(getal1, getal2)}")
elif keuze == '2':
    print(f"{getal1} - {getal2} = {aftrekken(getal1, getal2)}")
elif keuze == '3':
    print(f"{getal1} * {getal2} = {vermenigvuldigen(getal1, getal2)}")
elif keuze == '4':
    print(f"{getal1} / {getal2} = {delen(getal1, getal2)}")
else:
    print("Ongeldige keuze")
