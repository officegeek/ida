---
    layout: default
    title: Kontrolstrukturer
    parent: Python Videregående
    has_children: false
    nav_order: 20
---

# Funktioner
En funktion er en code, der bruges til at udføre en enkelt, relateret handling. 

Funktioner giver bedre modularity i din code og en høj grad af kode genbrug.

Python har mange indbyggede funktioner som f.eks. **print()** osv. men du kan også lave dine egne funktioner. Disse funktioner kaldes **user-defined functions.**

## Opret en funktion
Du skal bruge **def** keyword når du vil opretter en funktion.

**Eksempel**
```python
def min_funktion():
    print('Hej')
```

## Brug af en funktion
Når du vil bruge en funktion skal du bare skrive navnet efterfulgt af ()

**Eksempel**
```python
# Opret
def min_funktion():
    print('Hej')

# Kald/Brug
min_funktion()
```

## Arguments
Du kan overføre argumenter til funktioner. Du kan tilføje flere argumenter til en funktion, de skal bare adskilles af et **,**

**Et argument**
```python
def min_funktion(fnavn):
    print(f'Hej {fnavn}')
```
**Flere argumenter**
```python
def min_funktion(fnavn, lname):
    print(f'Hej {fnavn} {lname}') 
```

## Default Argument
Det er også muligt at angive en Default værdi, på den måde behøver du ikke at angive en værdi.

**Med flere Arguments + Default**
```python
def min_funktion_3(fnavn, lname, ven = 'Ja'):
    print(f'Hej {fnavn} {lname}, Ven: {ven}')

# Kald/Brug
min_funktion_3('Tue', 'Hellstern')
min_funktion_3('Ole', 'Olsen', 'Nej')
```

## Return Values
En funktion kan også returnere en *værdi* ved at bruge et **return** statement. Det kan f.eks være en beregning du gerne vil have resultatet af.

```python
def min_beregning(tal1, tal2):
    total = tal1 + tal2
    return total

min_total = min_beregning(10, 20)
print(min_total) 

def min_funktion_navn(fnavn, lname):
    print(f'Hej {fnavn} {lname}')
    return fnavn + ' ' + lname

navn = min_funktion_navn('Per', 'Hansen')
print(navn)
```

## Global <> Local variables
Variabler, der er defineret inde i en funktion, er kun tilgængelige lokalt, og dem, der er defineret udenfor, har et globalt omfang.

Dette betyder, at lokale variabler kun kan tilgås inden for den funktion, hvori de er erklæret, mens globale variabler kan tilgås i hele programmet og af alle funktioner.

Når du kalder en funktion, bringes de variable, der er erklæret inde i den, ind i omfanget.

```python
# Dette er en global variable.
salgspris = 0; 

# Function
def rabat(salg_uden_rabat, rabat = 10):
    salgspris = salg_uden_rabat - (salg_uden_rabat*rabat/100)
    print(f'Print af salgspris inde fra funktionen: {salgspris}')
    return salgspris

print(f'Print uden for funktionen, global variabel: {salgspris}')

ny_pris = rabat(100,20)
print(ny_pris)
```

