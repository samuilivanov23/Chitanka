import re, os

my_dirnames = os.listdir("../books")
unique_words = []
words_count = dict()
count = 0

#read all books and extract the unique words
for my_dir in my_dirnames:
    print("my dir: " + my_dir)
    for my_file in os.listdir("../books/"+my_dir):
        if my_file.endswith(".txt"):
            file_location = "../books/"+my_dir+"/"+my_file
            f = open(file_location, encoding='utf-8', mode='r')
            file_content = f.read()
            f.close()

            current_file_words = list(set(re.findall("[а-яА-Я]{3,}", file_content)))

            f = open("../unique_words.txt", encoding="utf-8", mode="w+")
            for word in current_file_words:
                word = word.lower()
                f.write(word+"\n")
                if word in words_count:
                    words_count[word] += 1
                else:
                    words_count[word] = 1
            f.close()

f = open("../unique_words.txt", encoding='utf-8', mode='r')
file_content = f.read()
f.close()

for key in words_count:
    if words_count[key] == 1:
        count+=1

print("count: " + str(count))