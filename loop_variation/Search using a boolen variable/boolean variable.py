#Um etwas zu suchen und wissen, das dieses Elemtn zu finden ist, können wir eine Variable zu Anfang als FALSE definieren, um den TRUE wert herauszugeben

fund = False
print("Bevor", fund)

for i in [9,41,12,3,74,15]:
    if i == 3:
        fund = True
    else:
        fund = False
    print(fund, i)

print("Nacher", fund)
