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

def dekripto_permutation(teksti_enkriptuar, celsi):
    teksti_enkriptuar = teksti_enkriptuar.upper().replace(" ", "")
    celsi = celsi.upper()
    
    alfabeti = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    renditja = []

    for shkronja_alfabeti in alfabeti:
        for i in range(len(celsi)):
            if celsi[i] == shkronja_alfabeti:
                renditja.append(i)

    numri_kolonave = len(celsi)
    shkronja_per_kolone =len(teksti_enkriptuar) // numri_kolonave
    mbetja = len(teksti_enkriptuar) % numri_kolonave

    gjatesia_e_kolonave = []
    for i in range(numri_kolonave):
        gjatesia_e_kolonave.append(shkronja_per_kolone)

    for i in range(mbetja):
        gjatesia_e_kolonave[i] += 1

    kolonat_e_renditura = []
    for i in range(numri_kolonave):
        kolonat_e_renditura.append("")

    indeksi_tekstit = 0
    for indeksi_kolones in renditja:
        gjatesia = gjatesia_e_kolonave[indeksi_kolones]
        kolona_aktuale = ""
        for i in range(gjatesia):
            kolona_aktuale += teksti_enkriptuar[indeksi_tekstit]
            indeksi_tekstit += 1
        kolonat_e_renditura[indeksi_kolones] = kolona_aktuale

    teksti_dekriptuar = ""
    numri_rreshtave = shkronja_per_kolone
    if mbetja > 0:
        numri_rreshtave += 1

    for rreshti in range(numri_rreshtave):
        for kolona in range(numri_kolonave):
            if rreshti < len(kolonat_e_renditura[kolona]):
                teksti_dekriptuar += kolonat_e_renditura[kolona][rreshti]

    return teksti_dekriptuar