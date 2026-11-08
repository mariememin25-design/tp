
janvier = ["C01", "C02", "C03", "C05", "C08"]
fevrier = ["C02", "C03", "C04", "C08", "C09"]
mars = ["C01", "C03", "C08", "C09", "C10"]

trois_mois = []
for c in janvier  :
    if c in fevrier and c in mars :
    
       trois_mois.append(c)
print(f"les clients venus le trois mois: {trois_mois}")

au_moins_une_fois = []
for c in mars + janvier + fevrier :
    if c not in au_moins_une_fois:
        au_moins_une_fois.append(c)        
print(f"les clients venus au moins une fois : {au_moins_une_fois}")

nouveaux_client = []
for c in mars :
    if c not in janvier and c not in fevrier :
      nouveaux_client.append(c) 
 


print(f" les nouveaux clients en mars: {nouveaux_client}") 
