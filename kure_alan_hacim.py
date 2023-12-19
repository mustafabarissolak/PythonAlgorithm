pi = 3.14
yariCap = float(input("Kürenin yarıçapını gir: "))

def alanHesapla(r):
    alan = 4*pi*r**2
    print("Alanı: ", alan)

def hacimHesapla(r):
    hacim = (4*pi*r**3)/3
    print("Hacmi: ",hacim)


if __name__ == "__main__":
    alanHesapla(yariCap)
    hacimHesapla(yariCap)
