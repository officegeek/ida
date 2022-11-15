# Lister
liste1=[22, -5, 16, -45, -17, 19, 87, -10]
liste2=[]

# Overfør kun positive tal til liste2
for i in liste1:
    if i > 0:
        liste2.append(i)

print(f'Indholdet af liste2: {liste2}')