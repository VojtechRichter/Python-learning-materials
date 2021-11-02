age = int(input("Zadejte vek: "))

if age <= 18:
    if age >= 15:
        print("dospivajici")
    else:
        print("dite")
else:
    print("dospely")