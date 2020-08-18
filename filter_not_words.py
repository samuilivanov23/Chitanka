import re

words_count = dict()

f = open("../unique_words.txt", encoding='utf-8', mode='r')
file_content = f.read()
f.close()

current_file_words_not_include = list(set(re.findall("\w+[аоу]{3,}", file_content)))
current_file_words_include = list(set(re.findall("\w+", file_content)))

for word in current_file_words_not_include:
    print(word)

for word in current_file_words_not_include:
    if word in current_file_words_include:
        current_file_words_include.remove(word)
        print("here")

f = open("../unique_words_4.txt", encoding='utf-8', mode='w+')

for word in current_file_words_include:
    f.write(word + "\n")

f.close()