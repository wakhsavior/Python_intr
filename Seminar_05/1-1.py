# Числа Фибоначчи через рекурсию

def Fibonachi (n):
    if n in [0,1]:
        return 1
    return Fibonachi(n-1) + Fibonachi(n-2)
    


def main():
    N = int(input("Enter Number: "))
    fibonachi = Fibonachi(N)
    print(fibonachi)


if __name__ == "__main__":
    main()