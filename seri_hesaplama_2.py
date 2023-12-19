# 1/2 + 2/5 + 3/10 + ... n / n^2 + 1 = ?

n = int(input("Seri açılımı için bir n değeri girin: "))

def hesapla():
    a = 1
    b = 2
    toplam = 0.0
    for i in range(1, (n+1)):
        toplam += a/b
        a += 1
        b = a**2 + 1
    print("Sonuc: ", toplam)

if __name__ == "__main__":
    hesapla()

