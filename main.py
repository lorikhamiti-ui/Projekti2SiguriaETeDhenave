from bifid import enkripto_bifid, dekripto_bifid
from permutation import enkripto_permutation, dekripto_permutation

def main():
    vazhdo = True

    while vazhdo:
        print("\n--- MENUJA ---")
        print("1. Bifid Cipher")
        print("2. Permutation Cipher")
        print("3. Dil")

        zgjedhja = input("Zgjidhni (1, 2 ose 3):")

        if zgjedhja == '1' or zgjedhja == '2':
            veprimi = input("Deshironi te Enkriptoni apo Dekriptoni? Shkruaj E ose D:")

            teksti = input("Shkruaj tekstin:")
            çelsi = input("Shkruaj çelsin:")

            if zgjedhja == '1':
                if veprimi.upper() == 'E':
                    rezultati = enkripto_bifid(teksti,çelsi)
                elif veprimi.upper() == 'D':
                    rezultati = dekripto_bifid(teksti,çelsi)
                else:
                    print("Keni dhene veprim te gabuar.")
                    continue 
            elif zgjedhja == '2':
                if veprimi.upper() == 'E':
                    rezultati = enkripto_permutation(teksti, celsi)
                elif veprimi.upper() == 'D':
                    rezultati = dekripto_permutation(teksti, celsi)
                else:
                    print("Keni dhene veprim te gabuar.")
                    continue

            print("Rezultati: " + rezultati)
            
            pergjigja = input("\nDeshironi te provoni perseri? (po/jo): ")
            if pergjigja.lower() == 'jo':
                print("Mirupafshim!")
                vazhdo = False
                
        elif zgjedhja == '3':
            print("Mirupafshim!")
            vazhdo = False
            
        else:
            print("Zgjedhje e gabuar. Provoni prap.")

main()