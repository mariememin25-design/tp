ventes = [("Aicha", 12000), ("Sidi", 8000), ("Aicha", 15500),("Mohamed", 4000), ("Sidi", 22000), ("Aicha", 3000),
("Fatimetou", 18000)]

vendeurs_distincts = set()
for nom , momtant in ventes :
    vendeurs_distincts.add(nom)
n = len(vendeurs_distincts)
print(f"le nombre de vendeurs distincts: {n} ")

nb_ventes ={}
chiffres_affaires = {}
for nom , montant in ventes :
    if nom in nb_ventes :
        nb_ventes[nom] += 1
    else :
        nb_ventes[nom] = 1
    if nom in chiffres_affaires :
        chiffres_affaires[nom] +=montant
    else :
        chiffres_affaires[nom] = montant 
print(f"nombre de ventes:{nb_ventes} ") 
print(f"chiffre des affaires: {chiffres_affaires}") 

l = sorted(chiffres_affaires , reverse= True) 
print(l)
