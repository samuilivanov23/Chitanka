import os
import re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import zipfile

i = 1

while i <= 75:
    url = "https://chitanka.info/authors/first-name/-.html/" + str(i)

    print("page: " + str(i))
    print(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find("ul", class_="superlist").find_all("a", itemprop="url"):
        #create separate folder for each author's books
        author_name = link['href'].split('/')[-1]
        folder_location = "../books/" + author_name

        url = "https://chitanka.info/person/" + author_name

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        print("\nauthor: " + author_name)

        #using regex to match the starting pattern and everything else after that
        if author_name == "rainer-maria-rilke":
            for link2 in soup.find_all("a", {'title': re.compile(r'^Сваляне във формат txt.zip')}):
                #Name the files using the last portion of the link

                if link2['href'].split('/')[-2] == "text":
                    book_name = link2['href'].split('/')[-1]
                    filename = os.path.join(folder_location, book_name)
                    print(filename)

                    if not os.path.exists(folder_location):os.mkdir(folder_location)

                    f = open(filename, 'wb')
                    f.write(requests.get(urljoin(url,link2['href'])).content)
                    f.close()
    print("\n")
    i += 1