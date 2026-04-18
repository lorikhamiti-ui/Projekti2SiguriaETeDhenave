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
        c = te_gjitha_numrat[i+1]
        teksti_enkriptuar += katrori[(r * 5) + c]
        
    return teksti_enkriptuar
