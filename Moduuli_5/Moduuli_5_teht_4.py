"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa
järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
ja for/in toistorakennetta niiden läpikäymiseen.
"""


lista = []

for i in range(0, 5):
    kaupunki = input("Anna kaupungin nimi: \n")
    lista.append(kaupunki)


for i in lista:
    print(i)



