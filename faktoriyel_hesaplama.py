sayi = int(input("Faktöriyeli hesaplanacak pozitif tamsayı değerini gir: "))

def hesapla(num):
    sonuc = 1
    sayac = 1
    while sayac != num:
        sonuc *= num
        num -= 1
    print(sonuc)

if __name__ == "__main__":
    hesapla(sayi)

