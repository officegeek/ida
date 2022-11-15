# tuescript.py

# Definition af min funktion
def my_function():
    print('Jeg kommer fra en funktion i "tuescript.py"')

# Afvikling af denne fil
if __name__ == "__main__":
    print('Hvis afviklet direkte fra tuespript.py - __name__ = ' + __name__ )
else:
    print('Hvis afviklet via import - __name__ = ' + __name__)