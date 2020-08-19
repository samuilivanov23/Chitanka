f = open("../unique_words_9.txt", encoding='utf-8', mode='r')
file_content = f.read()
f.close()
word_list = file_content.split("\n")

final_words = []
count = 0

for word in word_list:
    if word[:(len(word) - 1)] in word_list:
        final_words.append(word[:(len(word) - 1)])
    elif word[:(len(word) - 2)] in word_list:
        final_words.append(word[:(len(word) - 2)])
    elif word[:(len(word) - 3)] in word_list:
        final_words.append(word[:(len(word) - 3)])
    else:
        final_words.append(word)

    print(count)
    count+=1

final_words = list(set(final_words))

f = open("../filtered_words_2.txt", encoding="utf-8", mode="a")

print("\n")
for word in final_words:
    f.write(word + "\n")