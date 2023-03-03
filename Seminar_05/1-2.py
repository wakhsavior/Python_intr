import random


def main():
    N = int(input("Enter size of ratings: "))
    ratings = [random.randint(1,5) for i in range(N) ]
    print(ratings)
    minRating =  min(ratings)
    maxRating = max(ratings)
    ratings = [minRating if i == maxRating else i for i in ratings]
    # for i in range(N):
    #     if ratings[i] == maxRating:
    #         ratings[i] = minRating
    print(ratings)
if __name__ == "__main__":
    main()