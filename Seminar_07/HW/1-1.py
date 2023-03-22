'''
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его
кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе
стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух
вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
и “Пам парам”, если с ритмом все не в порядке
'''

vowels = ['у','е','а','ы','о','э','я','и','ю','ё']

def ritm(ritm_line):
    vowels_num = list()
    phrases = ritm_line.lower().split()
    for phrase in phrases:
        letters = {}.fromkeys(vowels,0)
        for i in phrase:
            if letters.get(i) != None:
                letters[i] += 1
        vowels_num.append(sum(letters.values()))
    print(vowels_num)        
    if len(set(vowels_num)) == 1:
        if (tuple(set(vowels_num)))[0] == 0:
            return False 
        else:
            return True
    else:
        return False 

def main():
    poem = input("Enter Phrase: ")
    if ritm(poem):
        print("Парам пам-пам")
    else:
        print("Пам парам")




if __name__ == "__main__":
    main()