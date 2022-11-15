# myApp
from time import sleep

print("Dette er en fil der viser brugen af main")

def process_data(data):
    print("Begynd data processering.......")
    modified_data = data + " modificeret data"
    sleep(3)
    print("Data processering afsluttet.")
    return modified_data

def read_data_from_web():
    print("Læs data fra f.eks. Internettet")
    data = "Data fra internettet"
    return data

def write_data_to_database(data):
    print("Skriv data til en database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()