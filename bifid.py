def enkripto_bifid(teksti, celsi):
    alfabeti = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # normalizojme celesin
    celsi = celsi.upper().replace("J", "I").replace(" ", "")
    
    katrori = ""
    # ndertojme matricen 5x5
    for shkronja in celsi:
        if shkronja not in katrori:
            katrori += shkronja
            
    # plotesojme katrorin me shkronjat e mbetura te alfabetit
    for shkronja in alfabeti:
        if shkronja not in katrori:
            katrori += shkronja
            
    teksti_i_paster = ""
    # pastrojme tekstin dhe mbajme vetem shkronjat qe jane ne katror
    teksti = teksti.upper().replace("J", "I")
    for shkronja in teksti:
        if shkronja in katrori:
            teksti_i_paster += shkronja
            
    rreshtat = []
    kolonat = []
    
    # kthejme cdo shkronje ne koordinata
    for shkronja in teksti_i_paster:
        indeksi = katrori.index(shkronja)
        rreshtat.append(indeksi // 5)
        kolonat.append(indeksi % 5)
    
    # bashkojme fillimisht rreshtat pastaj kolonat sipas rregullit bifid
    te_gjitha_numrat = rreshtat + kolonat
    
    teksti_enkriptuar = ""
    # lexojme numrat nga dy dhe i kthejme serish ne shkronja
    for i in range(0, len(te_gjitha_numrat), 2):
        r = te_gjitha_numrat[i]

def dekripto_bifid(teksti_enkriptuar, celsi):
    alfabeti = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    celsi = celsi.upper().replace("J", "I").replace(" ", "")
    
    katrori = ""
    for shkronja in celsi:
        if shkronja not in katrori:
            katrori += shkronja
            
    for shkronja in alfabeti:
        if shkronja not in katrori:
            katrori += shkronja

    teksti_i_paster = ""
    teksti_enkriptuar = teksti_enkriptuar.upper().replace("J", "I")
    for shkronja in teksti_enkriptuar:
        if shkronja in katrori:
            teksti_i_paster += shkronja

    te_gjitha_numrat = []
    for shkronja in teksti_i_paster:
        indeksi = katrori.index(shkronja)
        te_gjitha_numrat.append(indeksi // 5)
        te_gjitha_numrat.append(indeksi % 5)

    gjysma = len(te_gjitha_numrat) // 2
    rreshtat = []
    kolonat = []

    for i in range(gjysma):
        rreshtat.append(te_gjitha_numrat[i])

    for i in range(gjysma, len(te_gjitha_numrat)):
        kolonat.append(te_gjitha_numrat[i])

    teksti_dekriptuar = ""
    for i in range(gjysma):
        r = rreshtat[i]
        c = kolonat[i]
        teksti_dekriptuar += katrori[(r * 5) + c]

    return teksti_dekriptuar
        c = te_gjitha_numrat[i+1]
        teksti_enkriptuar += katrori[(r * 5) + c]
        
    return teksti_enkriptuar
