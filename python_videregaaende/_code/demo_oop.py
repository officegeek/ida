# Kommentar
# CTRL+K+C fjern CTRL+K+U

# Opret klassen - Medarbejder
#class Medarbejder:
#    pass

# Brug klassen - Medarbejder
#Kim = Medarbejder()

# Check om Ulla/Kim er en Medarbejder
#print(Ulla.__class__.__name__)
#print(Kim.__class__.__name__)

# Attributes
# class Medarbejder:
    
#     def __init__(self, lon, email, mobil):
#         self.lon = lon
#         self.email = email
#         self.mobil = mobil
        
# Opret Kim        
# Kim = Medarbejder(30000, 'kim@mitfirma.dk', 23435363)

# Opret med error
# Kim = Medarbejder(30000, 'kim@mitfirma.dk')

# class Medarbejder:
    
#     def __init__(self, lon = 0, email = '', mobil = ''):
#         self.lon = lon
#         self.email = email
#         self.mobil = mobil

# Kim = Medarbejder(30000, 'kim@mitfirma.dk')

# class Medarbejder:
        
#     # class attribute
#     firmanavn = "Mit firma"
    
#     def __init__(self, lon = 0, email = '', mobil = ''):
#         self.lon = lon
#         self.email = email
#         self.mobil = mobil

# Kim = Medarbejder(30000, 'kim@mitfirma.dk', 12345678)

# # Print Kim
# print(f'Kims løn er: {Kim.lon}')
# print(f'Kims e-mail er: {Kim.email}')
# print(f'Kims mobil er: {Kim.mobil}')
# print(f'Firmaet hedder: {Kim.firmanavn}')

# # Opdatering af oplysninger
# Kim.lon = 40000
# Kim.mobil = 87654321

# class Medarbejder:
        
#     # class - attribute
#     firmanavn = "Mit firma"
    
#     # instance - attributter
#     def __init__(self, lon = 0, email = '', mobil = ''):
#         self.lon = lon
#         self.email = email
#         self.mobil = mobil
    
#     # Løn stigning metode
#     def lonstigning(self):
#         self.lon += 0.1 * self.lon

# Kim = Medarbejder(30000, 'kim@mitfirma.dk', 12345678)

# # Print Kim
# print(f'Kims løn er: {Kim.lon}')
# print(f'Kims e-mail er: {Kim.email}')
# print(f'Kims mobil er: {Kim.mobil}')
# print(f'Firmaet hedder: {Kim.firmanavn}')

# # Løn stigning
# Kim.lonstigning()

# print(f'Kims nye løn er: {Kim.lon}')


class Medarbejder:
        
    # class - attribute
    firmanavn = "Mit firma"
    
    # instance - attributter
    def __init__(self, lon = 0, email = '', mobil = ''):
        self.lon = lon
        self.email = email
        self.mobil = mobil
    
    # Løn stigning metode
    def lonstigning(self, stigninglon = 10):
        self.lon +=  (stigninglon/100) * self.lon

Kim = Medarbejder(30000, 'kim@mitfirma.dk', 12345678)

# Print Kim
print(f'Kims løn er: {Kim.lon}')

# Løn stigning
Kim.lonstigning(20)

print(f'Kims nye løn er: {Kim.lon}')

