# f-string

# Interpolation
navn = 'Tue'
alder = 24

print(f'Hej, {navn}, din alder er {alder}')

# Variabel Navn
print(f'Hej, {navn=}, din alder er {alder=}')

# Beregninger
tal = 10

print(f'{tal * 2}')
print(f'{tal * 2 = }')

# Formatering
pris = 1366.1265
rabat = 0.22

# .2f
print(f'{pris:.2f}')

# ,.2f
print(f'{pris:,.2f}')

# .2n
print(f'{pris:.1n}')

# .0%
print(f'{rabat:.0%}')

# Format på pi - stigende til 6 decimaler
from math import pi

for i in range(1, 7):
    print(f'{pi:.{i}f}')

# Nedtælling fra 10
for i in range(10, -1, -1):
    print(f'{i:02}')

# Find det længste nummer og indsæt nuller så alle har sammen længde
produkt_ider = [67, 123456789, 6337493, 82941, 45259835]

laengste_produkt_id = len(max(map(str, produkt_ider), key=len))

for produkt_id in produkt_ider:
    print(f'{produkt_id:0{laengste_produkt_id}}')

# Dato og Tid
from datetime import datetime;

date_val = datetime.now()
print(date_val)

print(f'{date_val:%d-%m-%Y}')
print(f'{date_val:%Y}')
print(f'{date_val:%H}')

# Align
align = ['left', 'center', 'right']

print(f'{align[0]:<25}')
print(f'{align[1]:^25}')
print(f'{align[2]:>25}')

# Tabel format
print(f'Number\t\tSquare\t\tCube')
for x in range(1, 11):
    x = float(x)
    print(f'{x:5.2f}\t\t{x*x:6.2f}\t\t{x*x*x:8.2f}')