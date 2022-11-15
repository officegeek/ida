def min_funktion():
  print('Hej, jeg kommer fra en funktion')

min_funktion()


# Paramenter
def velkomst(f_navn, e_navn):
  print(f'Hej {f_navn} {e_navn}, godt at se dig')

velkomst('Tue', 'Hellstern')

# Ukendt antal
def deltagernavn(*navn):
      print('Deltager 2 hedder ' + navn[1])

deltagernavn('Ole', 'Lis', 'Ulla')

# Default
def lande(country = 'Danmark'):
      print(f'Jeg er fra {country}')

lande('Sverige')
lande('USA')
lande()
lande('UK')

# Return
def gange_func(x):
      return 5 * x

print(gange_func(10))
print(gange_func(5))

# List
def hent_deltager_navne(deltagernavn):
      for x in deltagernavn:
            print(x)

deltagere = ['Tue', 'Ole', 'Lis']

hent_deltager_navne(deltagere)