print("P = n! / (n-r)! ")
num1 = int(input("n değerini gir: "))
num2 = int(input("r değerini gir: "))

def hesapla(n, r):
    pay = 1
    payda = 1

    for i in range(1,n+1):
        pay *= i

    for j in range(1,(n-r)+1):
        payda *= j

    p = pay / payda
    return p

if __name__ == "__main__":
    per = hesapla(num1, num2)
    print(per)
