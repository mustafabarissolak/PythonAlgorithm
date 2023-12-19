karsi = float(input("karsi kenar: "))
komsu = float(input("komsu kenar: "))
alfa = float(input("Sinüs alfa açısı: "))
PI = 3.14
hipo = (karsi**2 + komsu**2)**(1/2)

def hesapla(a,b,c):
    sinA = alfa*PI/180
    alan = (a*b*sinA)/2
    print("Alan: ", alan)

if __name__ == "__main__":
    hesapla(karsi,komsu,hipo)
