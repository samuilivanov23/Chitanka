char_set_1 = ["ите"]
char_set_2 = ["ия", "ът", "ят", "та", "то"]

f = open("../unique_words_4.txt", encoding='utf-8', mode='r')
file_content = f.read()
f.close()

current_file_words = file_content.split("\n")

count = 0
for word in current_file_words:
    print(count)

    filtered_words_file = open("../filtered_words.txt", encoding='utf-8', mode='r')
    filtered_words_content = filtered_words_file.read().split("\n")
    filtered_words_file.close()

    f = open("../filtered_words.txt", encoding="utf-8", mode="a")

    if word[(len(word) - 3):] in char_set_1:
        if not word[:(len(word) - 3)] in filtered_words_content:
            f.write(word[:(len(word) - 3)] + "\n")
            print(word[:(len(word) - 3)])

    elif word[(len(word) - 2):] in char_set_2:
        if not word[:(len(word) - 2)] in filtered_words_content:
            f.write(word[:(len(word) - 2)] + "\n")
            print(word[:(len(word) - 2)])
            
    else:
        if not word in filtered_words_content:
            f.write(word + "\n")
            print(word)

    count+=1
    f.close()