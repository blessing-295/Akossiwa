#random = aléatoire
import random


def demander_nombre_magique(nb_min, nb_max):
   # quel est le nombre magique(entre & et 10)
   nombre_int = 0
   while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("vous devez rentrer un chiffre entre : Réessayer")
        else: 
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Lenombre doit être entre {nb_min} et {nb_max}. Réessayer")
                nombre_int = 0
   return nombre_int
    

    


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_VIES  = 4
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
vies = NB_VIES 

"""nombre = 0
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"il vous reste {vies} vies")
    nombre = demander_nombre_magique(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("bravo, vous avez gagné")
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre magique est plus petit")
        vies -= 1
    else:
        print("le nombre magique est plus grand")
        vies -= 1
        
        

if vies == 0:
    print(f"vous avez perdu : le  nombre magique était {NOMBRE_MAGIQUE}")"""
    
    
gagne = False
for i in range(0, NB_VIES):
    vies = NB_VIES-i
    print(f"il vous reste {vies} vies")
    nombre = demander_nombre_magique(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("bravo, vous avez gagné")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre magique est plus petit")
    else:
        print("le nombre magique est plus grand")
    # if vies == 0:

if not gagne:       
     print(f"vous avez perdu : le  nombre magique était {NOMBRE_MAGIQUE}")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    