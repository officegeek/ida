---
    layout: default
    title: Kontrolstrukturer
    parent: Python Videregående
    has_children: false
    nav_order: 10
---

# Kontrolstrukturer
Pythons kontrolstrukturer fungerer som kontrolstrukturerne i andre sprog, du har adgang til:

- if .. else
- and
- or
- nested if
- while loops
- for loops

## Logiske betingelser
Python har disse logisk betingelser:

- *Lig med*: **a == b**
- *Ikke lig med*: **a != b**
- *Mindre end*: **a < b**
- *Mindre end eller lig med*: **a <= b**
- *Større end*: **a > b**
- *Større end eller lig med*: **a >= b**

Disse betingelser kan du bruge flere steder f.eks. i **IF** sætninger og **Loops**.

## if
En if sætning starter med et if keyword.

```python
a = 10
b = 100

if b > a:
    print('b er større end a')
```

## elif
**elif** er pythons måde at sige "*hvis de tidligere betingelser ikke var sande, så prøv denne betingelse*".

```python
a = 20
b = 20

if b > a:
    print('b er større end a')
elif a == b
    print('a og b er ens')
```

## else
**else** fanger alt, som ikke er fanget af de foregående betingelser.

```python
a = 200
b = 20

if b > a:
    print('b er større end a')
elif a == b
    print('a og b er ens')
else:
    print('a er større end b')
```

Du kan godt bruge **else** uden **elif**.

## and
**and** bruges til at kombinere betingede udsagn, **begge** udsagn skal være **sande**.

Det kunne f.eks. være:

```python
a = 100
b = 20
c = 500
if a > b and c > a:
  print("Begge betingelser er Sande")
```

## or
**or** bruges også til at kombinere betingede udsagn, **kun et** udsagn skal være **sandt**.

```python
a = 100
b = 20
c = 500
if a > b or c > a:
  print("En betingelser er Sand")
```

## nested if
Du kan have if-sætninger inde i if-sætninger, dette kaldes **nestede if-sætninger**.

```python
x = 35

if x > 10:
    print("Over 10,")
    if x > 20:
        print("også over 20.")
    else:
        print("men ikke over 20.")
```

## while loops
Med et **while** loop kan du afvikle kode, så **længe en betingelse er sand**.

```python
i = 1
while i < 5:
    print(i)
    i += 1
```

**Note**: Husk at øge **i** (*i += 1*), ellers vil løkken fortsætte for *evigt*.

### break
Du kan stoppe et loop med **break**, selvom while-betingelsen er sand.

```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

## for loops
Et **for loop** bruges til at gennemløbe en sekvens, det kan være, **list**, **tuple**, **dictionary**, **set** eller **string**.

```python
navne = ['Ole', 'Lis', 'Per']

for x in navne:
    print(x)
```

### else
Du kan også bruge **else** i for loop

```python
navne = ['Ole', 'Lis', 'Per']

for x in navne:
    print(x)
else:
    print('Slut')
```

**Note**: **else** vil ikke blive udført hvis du brugere **break**.