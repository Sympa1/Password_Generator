import random

# Symbolliste
password_elements = ["a", "b", "c", "ä", "ö", "ü", "!", "@", "#", "$", "%", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z", "Ä", "Ö", "Ü", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{",
                     "}", ";", ":", "<", ">", ",", ".", "?", "/", "|", "\\", "'", '"', "`", "~"]

# Deklaration (ohne Wertzuweisung) der Liste für das zu generierendes Passwort
final_password = []

# Begrüßung
print("\nHallo ich bin \"PG\" Ihr freundlicher Passwortgenerator :)\n")

# Deklaration der Variable zur bestimmung der maximalen Passwortlänge
max_length = 255

while True:
    try:
        # Erfassung der Nutzeingaben als "Integer" für die Passwortspezifikationen
        password_length = int(input("Geben Sie die Passwortlänge an (max. 255 Zeichen): "))
        # Kontrolle, ob die maximalen Zeichen eingehalten wurden
        if password_length > max_length:
            print("\n Ihre gewünschte Passwortlänge entspricht nicht der Maximal zulässigen Passwortlänge!\n")
        else:
            # Generieren des Passwortes
            for i in range(password_length):
                element = random.choice(password_elements)
                final_password.append(element)

            break
    except ValueError:
        print("Bitte geben Sie nur Ganzzahlen an!")

# Ausgabe des passwortes
print("Das ist Ihr neues Passwort: ", "".join(final_password))
