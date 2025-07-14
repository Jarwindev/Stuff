Text=input("Ange en text: ")
New_Text=Text.replace(" ", "")
if New_Text == New_Text[::-1]:
    print("Texten är ett palindrom.")
else:
    print("Texten är inte ett palindrom.")