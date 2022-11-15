# Import pi fra math
from math import pi

# Imput fra brugeren
r = float(input ('Skriv radius af cirkel: '))

# Brug f string til print
print(f'Arealet af cirklen med radius {r:.2f} er: {float(pi * r**2):.2f}')