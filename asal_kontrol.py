sayi = int(input("Pozitif bir tamsayı girin: "))

def hesapla(a):
    if a < 0:
        print("Lütfen pozitif tam sayı girin")

    elif a > 0 and a <= 2:
        print(f"{a} Sayısı asal. :(")

    else:
        asalmı = True
        
        for i in range(2,a):
            if a%i == 0:
                asalmı = False
        if asalmı:
            print(f"{a} Sayısı asal.")
        else:
            print(f"{a} Sayısı asal değil.")

if __name__ == "__main__":
    hesapla(sayi)
