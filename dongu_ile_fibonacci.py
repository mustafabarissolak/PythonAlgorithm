n_eleman = int(input("Fibonacci dizisinde ilk n eleman çıktısı için n değeri girin: "))
fibonacci = []

def hesapla(eleman):
    a = 0
    b = 1

    for i in range(eleman):
        a,b = b, a+b
        fibonacci.append(a)

    print(fibonacci)

if __name__ == "__main__":
    hesapla(n_eleman)
