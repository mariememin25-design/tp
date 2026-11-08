
catalogue = {
"P01": {"nom": "Ordinateur portable", "categorie": "Informatique",
"prix": 45000},
"P02": {"nom": "Imprimante", "categorie": "Informatique",
"prix": 12000},
"P03": {"nom": "Chaise de bureau", "categorie": "Mobilier",
"prix": 6500},
"P04": {"nom": "Ramette papier", "categorie": "Fournitures",
"prix": 350},}
 
catalogue["PO5"] = {"nom" : "Bureau"  ,"categorie" : "Mobilier" , "prix": 18000}
print(catalogue)
for i in catalogue.values() :
    if i["categorie"]== "Informatique" :
        nouveau_prix = i["prix"]*1.05
        i["prix"] = nouveau_prix
        print(nouveau_prix)

del catalogue["P04"]
print(catalogue)

for code , produit in catalogue.items() :
    print(f"{code:<5} | {produit["nom"]:<20} | {produit["categorie"]:<15} | {produit["prix"]:>12}")


for categorie in ["Informatique" ,"Mobilier" ,"Fournitures"] :
    somme = 0
    n = 0
    for p in catalogue.values() : 
        if p["categorie"] == categorie:
            somme+= p["prix"]
            n+= 1
    if n>0 :
        print(f"{categorie}: {somme/n} MRU")        
    else :
        print(f"{categorie}: aucun produit disponible ")

