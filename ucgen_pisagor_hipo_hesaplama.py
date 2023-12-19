ilkDik = float(input("Ilk dik kenar uzunluğunu girin: "))
ikinciDik = float(input("Ikınci dik kenar uzunluğunu girin: "))

def hesapla(a,b):
    c = ((a**2) + (b**2))
    hipo = c**(1/2)
    print("Hipotenüs değeri: ", hipo) 
    

if __name__ == "__main__":
    hesapla(ilkDik,ikinciDik)
