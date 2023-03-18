import random as rnd

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        
    return array 


def main():
    N = int(input("Number of element in List: "))
    list_01 = [rnd.randint(1,20) for i in range(N)]
    print(list_01)
    print(merge_sort(list_01))


if __name__ == "__main__":
    main()