girdi = input("Hesaplamak için 0'dan farklı sayılar girin: ")
sayilar = girdi.split()

def hesapla():
    degerSayisi = 0
    tersineBolum = 0
    for i in sayilar:
        tersineBolum += 1/int(i)
        degerSayisi +=1
    sonuc = degerSayisi/tersineBolum
    return sonuc

if __name__ == "__main__":
    H_mean = hesapla()
    print("Harmonik ortalama: ", H_mean)
