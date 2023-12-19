print("P = n! / (n-r)! ")

def hesapla():
    n = int(input("n değerini gir: "))
    r = int(input("r değerini gir: "))
    pay = 1
    payda = 1

    for i in range(1,n+1):
        pay *= i

    for j in range(1,(n-r)+1):
        payda *= j

    p = pay / payda

    print(f"Permutasyon: ", p)

if __name__ == "__main__":
    hesapla()