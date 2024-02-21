girdi = input("Hesaplamak için sayılar girin: ")
sayilar = girdi.split()

def hesapla():
    toplam = 0
    for i in sayilar:
        toplam += int(i)
    sonuc = toplam/len(sayilar)
    return sonuc

if __name__ == "__main__":
    hesapla()
