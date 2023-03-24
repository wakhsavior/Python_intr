
alp = 'ёуеаоэяиюы'

def main():
    phrase = input().lower().split()
    # vowels_phrase = [char for word in phrase for char in word if char in alp]  # Не работает как надо. На каждую итерацию будет один элемент списка
    vowels_phrase = [len([char for char in word if char in alp]) for word in phrase] # Лист в листе, рабочий вариант
    # vowels_phrase = []
    # for word in phrase:
    #     vowels = []
    #     for char in word:
    #         if char in alp:
    #             vowels.append(char)
    #     vowels_phrase.append(len(vowels))
    print(vowels_phrase)
    if all(vowels_phrase) and len(set(vowels_phrase))==1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

if __name__ == "__main__":
    main()