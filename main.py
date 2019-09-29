# pip install requests for installation

import requests
from urllib.parse import urljoin

url = input('Insira a URL aqui: ')
res = requests.get(url)

html = res.text

open_tag = False


def find_between(value, first, last):
    try:
        start = value.index(first) + len(first)
        end = value.index(last, start)
        return value[start:end]
    except ValueError:
        return ''


img_list = set()

for word in html.split():
    # print(word)
    if word.find('<img') > -1:
        # print('open tag', word)
        open_tag = True

    if open_tag == True and word.find('src') > -1:
        open_tag = False
        img_url = find_between(word, 'src="', '"')

        if img_url.find('http') == -1:
            img_url = urljoin(url, img_url)

        img_list.add(img_url)

print(*img_list, sep="\n")
# print(res.text)