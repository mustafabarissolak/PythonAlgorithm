kisaKenar = float(input("Kısa kenarı gir: "))
uzunKenar = float(input("Uzun kenarı gir: "))

def dortgen(kisa, uzun):
    cevre = 2*(kisa+uzun)
    alan = kisa*uzun
    print(f"Alanı: {alan}\nÇevresi: {cevre}")

if __name__ == "__main__":
    dortgen(kisaKenar,uzunKenar)

