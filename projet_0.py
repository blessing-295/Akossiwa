import random

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_QUESTION = 10

def poser_question():
    a =  random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b =  random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    #0 -> +
    #1 -> *
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    reponse_str = input(f"calculez: {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if o == 1:
        calcul = a*b
    if reponse_int == calcul:
        #print("reponse correcte")
        return True
    
        #print("reponse incorrecte")
    return False
    
   
  #◘cettfe partie pour afficher le nombre de quetion  
nb_points = 0   
for i in range(0, NB_QUESTION):
    print(f"question N°{i+1} / {NB_QUESTION} ")
    if poser_question():
        print("reponse correcte")
        nb_points += 1
    
    else: 
         print("reponse incorrecte")
    print()
    
moyenne = int(NB_QUESTION/2)
print(f"votre note est : {nb_points} sur {NB_QUESTION}" ) 

if nb_points == NB_QUESTION :
   print("excéllent")
elif nb_points == 0:
    print("réviser vos maths")
elif nb_points > moyenne :
    print("pas mal")
else:
    print("peut mieux faire")






