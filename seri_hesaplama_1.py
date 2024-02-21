# 1/2 + 2/3 + 3/4 + ... n/n+1 = ?

n = int(input("Seri açılımı için bir n değeri girin: "))

def hesapla():
    a = 1
    b = 2
    toplam = 0
    for i in range(1, n+1):
        toplam += a/b
        a += 1
        b += 1
    return toplam

if __name__ == "__main__":
    seri = hesapla()
    print(f"Sonuc: {seri}")
