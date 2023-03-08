# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def main():
    first_elem = int(input("Enter First Element of sequence: ")) 
    diff = int(input("Enter difference between elements: "))
    number = int(input("Enter number of Elements of sequence: "))

    for i in range(1,number + 1):
        print(f"{first_elem + i*diff}")


if __name__ == "__main__":
    main()