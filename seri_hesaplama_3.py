# 0/3 + 3/10 + 8/29 + ... n^2 - 1 / n^3 + 2 = ?

n = int(input("Seri açılımı için bir n değeri girin: "))

def hesapla():
    a = 0
    b = 3
    toplam = 0
    sayac = 1
    
    while sayac <= n:
        toplam += a/b
        sayac += 1
        a = sayac**2 - 1
        b = sayac**3 + 2
        
    return toplam

if __name__ == "__main__":
    seri = hesapla()
    print(f"Sonuc: {seri}")
