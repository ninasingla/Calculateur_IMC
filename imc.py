# CALCULATEUR D'IMC 
# IMC = Poids / Taille²

print("# --- Calculateur d'IMC --- #")

# Définition des inputs 
prenom = input("Votre prénom : ")
taille = int(input("Votre taille (en cm) : "))
poids = float(input("Votre poids (en kg) : "))

# Calculer l'IMC avec les données entrées en input 
calcul_imc = poids / (taille*taille) * 10000
calcul_imc = round(calcul_imc, 2)

# Afficher l'IMC à l'utilisateur
print(f"Bonjour, {prenom} ! Votre IMC est de {calcul_imc}")

# Catégoriser le resultat obtenu
if calcul_imc <= 18.5:
    print("--> Vous êtes en insuffisance pondérale.")
elif 18.5 < calcul_imc <= 25 :
    print("--> Vous êtes de corpulence normale.")
elif 25 < calcul_imc <= 30 :
    print("--> Vous êtes en surpoids.")
elif 30 < calcul_imc <= 35 :
    print("--> Vous êtes en obésité modérée.")
elif 35 < calcul_imc <= 40 :
    print("--> Vous êtes en obésité sévère.")
else :
    print("--> Vous êtes en obésité morbide / massive.")
