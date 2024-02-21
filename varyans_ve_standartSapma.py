# # Senaryo: öğrenci sayısı ve notları.

ogrenciSayisi = int(input("Kaç öğrenci var? "))
notlar = []

for i in range(1, ogrenciSayisi + 1):
    notGirdi = float(input(f"{i}. öğrenci notunu giriniz: "))
    notlar.append(notGirdi)

n = len(notlar)

def aritmetik_ortalama():
    toplam = sum(notlar)
    ortalamaSonuc = toplam / n
    return ortalamaSonuc

def varyans():
    ortalama = aritmetik_ortalama()
    toplam = sum((x - ortalama) ** 2 for x in notlar)
    varyansSonuc = toplam / n
    return varyansSonuc

def standartSapma():
    standartSapmaSonuc = varyans() ** 0.5
    return standartSapmaSonuc

if __name__ == "__main__":
    Aort = aritmetik_ortalama()
    Var = varyans()
    Std = standartSapma()

    print("Ortalama:", Aort)
    print("Varyans:", Var)
    print("Standart Sapma:", Std)
