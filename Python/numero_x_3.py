# Kysytään käyttäjältä numeroita ja käsitellään virheet
while True:
    try:
        numero = int(input("Anna numero: "))
        
        # Kerrotaan numero kolmella
        tulos = numero * 3
        
        # Tulostetaan tulos
        print(f"Numero {numero} kerrottuna kolmella on {tulos}")
        
    except ValueError:
        print("Virhe: Syötä kelvollinen kokonaisluku!")