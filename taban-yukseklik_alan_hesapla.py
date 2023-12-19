tabanDegeri = float(input("Taban uzunluğu: "))
yukseklikDegeri = float(input("Yukseklik uzunluğu: "))

def hesapla(t,h):
    alan = (t*h)/2
    print("Üçhenin alanı: ", alan)

if __name__ == "__main__":
    hesapla(tabanDegeri,yukseklikDegeri)
    