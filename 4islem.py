def dortIslem(x,y):
    toplam = x+y
    fark = x-y
    carpim = x*y
    bolum = x/y
    print(f"Toplam: {toplam}")
    print(f"Fark: {fark}")
    print(f"Bolum: {bolum}")
    print(f"Carpim: {carpim}")

ilk_deger = int(input("ilk değeri gir: "))
ikinci_deger = int(input("İkinci değeri gir:"))

if __name__ == "__main__":
    dortIslem(ilk_deger, ikinci_deger)