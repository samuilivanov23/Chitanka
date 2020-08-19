import re

words_count = dict()

f = open("../unique_words_8.txt", encoding='utf-8', mode='r')
file_content = f.read()
f.close()

current_file_words_include = list(set(re.findall("\w+", file_content)))

letters_list = ["г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ю", "я"]

for letter in letters_list:
    regex_string_1 = "\w+[" + letter + "]{2,}\w+"
    regex_string_2 = "\w+[" + letter + "]{2,}"
    regex_string_3 = "[" + letter + "]{2,}\w+"
    regex_string_list = [regex_string_1, regex_string_2, regex_string_3]

    for regex_string in regex_string_list:
        current_file_words_not_include = list(set(re.findall(regex_string, file_content)))


        for word in current_file_words_not_include:
            if word in current_file_words_include:
                current_file_words_include.remove(word)
                print("here")
                print(word)

f = open("../unique_words_9.txt", encoding='utf-8', mode='w+')

for word in current_file_words_include:
    f.write(word + "\n")

f.close()