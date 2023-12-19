# Harmonik ortalama, seride bulunan sayıların tersine bölümü ile hesaplanmasıdır.

girdi = input("Hesaplamak için 0'dan farklı sayılar girin: ")
sayilar = girdi.split()

def hesapla():
    degerSayisi = 0
    tersineBolum = 0
    for i in sayilar:
        tersineBolum += 1/int(i)
        degerSayisi +=1
    sonuc = degerSayisi/tersineBolum
    print("Harmonik ortalama: ", sonuc)


if __name__ == "__main__":
    hesapla()