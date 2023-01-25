# Manchmal hat man eine Liste in eine Datei, welche man in eine Schleife packen möchte
#Man kann eine Schleife machen, welches nur einmal pro Datei in einer Liste läuft: Dafür benutzt man den  Befehl [ for (irgend eine Variable) in (Name der Liste): )

#Ein einfaches definite loop:

Zahlen_liste = [5,4,3,2,1]

for x in Zahlen_liste:
    print(x)
print("Ende!")


#Ein definite loop mit strings:

Namen_liste = ["Joseph","Hans","Fritz"]

for i in Namen_liste:
    print("Hallo", i)
print("Ende !")
