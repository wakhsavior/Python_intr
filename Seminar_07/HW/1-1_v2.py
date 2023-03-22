vowels = ['у','е','а','ы','о','э','я','и','ю','ё']

def count_letters(func, phrase):
    words = list()
    for word in phrase.split():
        words.append(tuple(x for x in word if func(x)!=None))
    return words

def main():
    poem = input("Enter Phrase: ")
    letters = {}.fromkeys(vowels,0)

    vowels_num = set(len(x) for x in count_letters(lambda x: letters.get(x),poem))

    if (len(vowels_num) == 1 and (tuple(vowels_num))[0] != 0):   
        print("Парам пам-пам")
    else:
        print("Пам парам")
    


if __name__ == "__main__":
    main()