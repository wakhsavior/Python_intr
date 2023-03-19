vowels = ['у','е','а','ы','о','э','я','и','ю','ё']

def count_letters(func, phrase):
    words = list()
    for word in phrase.split():
        words.append(tuple(x for x in word if func(x)!=None))
    return words

def main():
    poem = input("Enter Phrase: ")
    letters = {}.fromkeys(vowels,0)

    if (len(set(len(x) for x in count_letters(lambda x: letters.get(x),poem))) == 1):   
        print("Парам пам-пам")
    else:
        print("Пам парам")
    


if __name__ == "__main__":
    main()