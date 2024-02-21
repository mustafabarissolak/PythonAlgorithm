print("ax^2 + bx + c = 0 için;")
degerA = float(input("A degeri: "))
degerB = float(input("B degeri: "))
degerC = float(input("C degeri: "))

def hesapla(a,b,c):
    delta = (b**2) - (4*a*c)
    b_yeni = (-1)*b

    if delta < 0:
        # print("Reel kök yok")
        return None

    elif delta == 0:
        sonuc = (b_yeni + (delta**(1/2))) / 2*a
        # print("Sonuç çift kat kök: ", sonuc)
        return sonuc

    else:
        kok1 = (b_yeni + (delta**(1/2))) / 2*a
        kok2 = (b_yeni - (delta**(1/2))) / 2*a
        # print("1. kök: ", kok1)
        # print("2. kök: ", kok2)
        return kok1, kok2

if __name__ == "__main__":
    hesapla_ = hesapla(degerA,degerB,degerC)
    print(hesapla_)
