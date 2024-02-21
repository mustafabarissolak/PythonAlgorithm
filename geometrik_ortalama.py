girdi = input("Hesaplamak için sayılar girin: ")
sayilar = girdi.split()

def hesapla():
    islem = 1
    for i in sayilar:
        islem *= int(i)
    sonuc = islem**(1/len(sayilar))
    return sonuc

if __name__ == "__main__":
    hesapla()
    G_mean = hesapla()
    print("Geometrik ortalama: ", G_mean)
