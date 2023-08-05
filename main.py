import requests
import os

URL = "https://the-one-api.dev/v2"
KEY = os.environ.get('api_key')


def all_books(url):
    link = url + '/book'
    response = requests.get(link)
    response.raise_for_status()
    book_dic = response.json()['docs']
    return book_dic


def one_book(url, id):
    link = f"{url}/book/{id}"
    response = requests.get(link)
    return response.json()['docs']


def chapters(url, id):
    link = f"{url}/book/{id}/chapter"
    response = requests.get(link).json()['docs']
    chapter_name = [r['chapterName'] for r in response]
    return chapter_name


def movies(url, api):
    url = url + '/movie'
    headers = {'Authorization': f'Bearer {api}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['docs']


def character(url, api):
    url = url + '/character'
    headers = {'Authorization': f'Bearer {api}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['docs']


books = all_books(URL)
book1_id = books[0]['_id']
book2_id = books[1]['_id']
book3_id = books[2]['_id']
book_title = [book['name'] for book in books]
print(book_title)
book2 =one_book(URL, book2_id)
print(book2)
book3_chapters = chapters(URL, book3_id)
print(book3_chapters)
movies_all = movies(URL, KEY)
print(movies_all)
characters_all = character(URL, KEY)
print(characters_all)

