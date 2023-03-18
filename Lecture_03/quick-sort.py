import random as rnd

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = []
    more = []
    for i in array[1:]:
        if i <= pivot:
            less.append(i)
        elif i> pivot:
            more.append(i)
    return quick_sort(less) + [pivot] + quick_sort(more)



def main():
    N = int(input("Number of element in List: "))
    list_01 = [rnd.randint(1,20) for i in range(N)]
    print(list_01)
    print(quick_sort(list_01))


if __name__ == "__main__":
    main()