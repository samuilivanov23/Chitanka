import re, os

my_dirnames = os.listdir("../books")[:300]
files_locations = []
unique_words = []

#read all books and extract the unique words
for my_dir in my_dirnames:
    for my_file in os.listdir("../books/"+my_dir):
       if my_file.endswith(".txt"):
            file_location = "../books/"+my_dir+"/"+my_file
            dir_location = "../books/"+my_dir+"/"
            my_author_name = my_dir
            files_locations.append(file_location)

            f = open(file_location, encoding='utf-8', mode='r')
            file_content = f.read()
            f.close()

            current_file_words = set()
            current_file_words = " ".join(re.findall('[а-яА-Я]+', file_content)).split()
            current_file_words = list(current_file_words)

            final_words = set()
            for word in current_file_words:
                word = word.lower()
                if len(word) > 2:
                    final_words.add(word)

            final_words = list(final_words)
            unique_words += final_words

unique_words = set(unique_words)
count = 0
print(unique_words)

for word in unique_words:
    if word == "ходил":
        print("match")
        count+=1

print(len(unique_words))
print("\n\n")

print("matches: " + str(count))