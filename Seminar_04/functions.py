print(__name__)
def main():
    n = int(input())
    max_number = 0
    while n != 0:
        n = int(input())
        if max_number < n:
            max_number = n
    print(max_number)

if __name__ == "__main__":
    main()