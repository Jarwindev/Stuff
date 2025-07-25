#program som tar bort mellanslag från en text.

# Användaren anger en text och programmet skriver ut texten utan mellanslag.

Text=input("Ange en text: ")
print("Texten utan mellanslag:", Text.replace(" ", ""))