vstup = int(input("Zadejte index mesta: "))

muj_list = [
    "Ostrava",
    "Kladno",
    "Praha",
    "Liberec",
    "Opava",
    "Ceske Budejovice",
    "Litomerice"
]

if vstup > len(muj_list) - 1:
    print("Chýbný vstup")

for index, _ in enumerate(muj_list):
    if index == vstup:
        print(index)
        print(muj_list[index])