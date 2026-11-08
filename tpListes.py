jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
ventes = [125000, 98000, 143500, 87000, 210000, 176500]

total = sum(ventes) 
moyenne = total/ len(ventes)

print("totale ventes :" ,total)
print("moyenne ventes:" ,moyenne)

max_vente = ventes.index(max(ventes) )
jour_max= jours[max_vente] 
print("le jour avec les ventes les fortes:" + jour_max)

for i in range (len(ventes)) :
    if ventes[i] > moyenne :
      print(jours[i])

paires = list(zip(ventes , jours))
classement = sorted(paires , reverse = True)

for i , j in classement :
  print(i, ":",j) 



    

