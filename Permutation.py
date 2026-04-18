def enkripto_permutation(teksti, çelsi) :
    teksti = teksti.upper() .replace(" ","")
    çelsi = çelsi.upper()

    alfabeti = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    renditja = []

    for shkronja_alfabeti in alfabeti:
        for i in range(len(çelsi)):
            if çelsi[i] == shkronja_alfabeti:
                renditjja.append(i)

    kolonat = []
    for i in range(len(çelsi)):
        kolonat.append("")

    for i in range(len(teksti)):
        numri_kolones = i % len(çelsi)
        kolonat[numri_kolones] += teksti[i]

    teksti_enkriptuar = ""
    for indeksi in renditja:
        teksti_enkriptuar += kolonat[indeksi]

    return teksti_enkriptuar