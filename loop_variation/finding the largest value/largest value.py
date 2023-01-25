#Wir definieren eine Variable mit einer Nummer, welches zu dem Zeitpunkt die größte Nummer ist
#Wenn die Nummer in der Liste größer als die Nummer in der Variable ist, ist diese dann die größte Nummer

größte_nummer = -1
print("Bevor", größte_nummer)

for x in [9,41,12,3,74,15]:
    if x > größte_nummer:
        größte_nummer = x
    print(größte_nummer, x)

print("Nacher", größte_nummer)

