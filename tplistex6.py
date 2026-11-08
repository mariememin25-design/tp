
liste_montants = [1200, -350, 4800, 0, 15000, -90, 700]

list_positif = []
for m in liste_montants :
    if m> 0 :
        list_positif.append(m)
print(f"les montant positifs : {list_positif}")

value_abs = []
for m in  liste_montants :
    value_abs.append(abs(m))
print(f"les valeures absolues : {value_abs}")

value_tva = []
for m in liste_montants :
    if m>0 :
        m += round(m*1.16) 
        value_tva.append(m)
print(f"les montant positifs augmente de tva : {value_tva}")
















