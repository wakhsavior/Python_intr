
def recursion(num):
    if num == 0:
        return ''
    char = input("Enter Symbol: ")
    return recursion(num-1) + char        



def main():
     N = int(input("Enter Number: "))
     print(recursion(N))

if __name__ == "__main__":
    main()