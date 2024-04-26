# list comprehansion

result = []

# lijst vullen van 0 tem 9, alleen even nummers
for i in range(10):
    if i % 2 == 0:
        result.append((i,i))

# kan ook op deze manier gechreven worden
result = [(i,i) for i in range(10) if i % 2 == 0]

# print(result)


# Dictionairy comprehansion

dictionary = {}

# for i in range(10):
#     if i % 2 == 0:
#         dictionary[i] = i*2
 
# kan ook op deze manier
dictionary = {i:[j for j in range(i)] for i in range(10) if i % 2 == 0}

# print(dictionary)



# higher order functions

class Persoon:
    def __init__(self, naam, leeftijd, land):
        self.naam = naam
        self.leeftijd = leeftijd
        self.land = land


def check_age_lower_than_18(persoon):
    if persoon.leeftijd >= 18:
        return True
    else:
        return False
    
def check_country(persoon):
    if persoon.land == "Belgie":
        return True
    else:
        return False

def is_allowed(functie, personen):
    return [p for p in personen if functie(p)]


p1 = Persoon("Adriaan", 20, "Belgie")
p2 = Persoon("Elin", 19, "Roemenie")
p3 = Persoon("Jorrit", 1000, "Slowakije")

personen = [p1,p2,p3]
filtered_personen = is_allowed(check_age_lower_than_18, personen)


# nested functies 
# functie in functie
# gebruiken om structuur te houden

