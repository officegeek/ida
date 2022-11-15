# Opret
def min_funktion_1():
    print('Hej')

# Kald/Brug
min_funktion_1()

# Med et Argument
def min_funktion_2(fnavn):
    print(f'Hej {fnavn}')    

# Kald/Brug
min_funktion_2('Tue')

# Med flere Arguments
def min_funktion_2(fnavn, lname):
    print(f'Hej {fnavn} {lname}')


# Kald/Brug
min_funktion_2('Tue', 'Hellstern')

# Med flere Arguments + Default
def min_funktion_3(fnavn, lname, ven = 'Ja'):
    print(f'Hej {fnavn} {lname}, Ven: {ven}')    

# Kald/Brug
min_funktion_3('Tue', 'Hellstern')
min_funktion_3('Ole', 'Olsen', 'Nej')

# Return values
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

# Global <> Local variables
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