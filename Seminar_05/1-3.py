
def is_simple(num):
    if num in [2,3]:
        return True
    elif num%2 == 0 or num < 2:
        return True
    for i in range(3,int(num**0.5) + 1,2):
        if num%i == 0:
            return False
    return True 

def main():
     N = int(input("Enter Number: "))
     print(is_simple(N))

if __name__ == "__main__":
    main()