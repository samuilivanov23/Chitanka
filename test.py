from bs4 import BeautifulSoup
import requests, re

url = "https://chitanka.info/person/aleksandyr-pushkin"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


a_tags = soup.find_all("a", {'title': re.compile(r'^Сваляне във формат txt.zip')})

books_names = []
for a_tag in a_tags:
    if "/text/" in str(a_tag):
        latin_book_name = a_tag['href'].split('/')[-1]
        book_chitanka_id = re.findall('([0-9])', latin_book_name)
        book_chitanka_id = ''.join(book_chitanka_id)
        
        parent_tag = a_tag.parent.parent.parent.parent
        cyrillic_book_name = parent_tag.find("a", itemprop="name").find("i").get_text()
        cyrillic_book_name = book_chitanka_id + "-" + re.sub('\s+', '-', cyrillic_book_name)
        
        books_names.append(cyrillic_book_name)

# parent_tag = my_a_tags[0].parent.parent.parent.parent
# print(parent_tag.find("a", itemprop="name").find("i").get_text())
print(books_names)
print(len(books_names))