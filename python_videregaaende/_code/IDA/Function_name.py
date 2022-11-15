# Import af tuescript.py
import tuescript

# Afvikling af funktionen my_function i tuescript
tuescript.my_function()


# Afvikling af denne fil
if __name__ == "__main__":
    print ('Hvis afviklet direkte fra Function_name.py - __name__ = ' + __name__ )
else:
    print ('Hvis afviklet via import - __name__ = ' + __name__)