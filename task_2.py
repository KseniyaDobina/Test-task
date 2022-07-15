import requests
from bs4 import BeautifulSoup


def find_letters(url):
    """
    Функция для подсчета количества животных
    :param url: исходная ссылка на википедию
    :return: словарь
    """
    page = requests.get(url).text

    letters_dict = {}

    while True:
        soup = BeautifulSoup(page, 'lxml')
        animals = soup.find('div', class_='mw-category-columns').findAll('a')
        for animal in animals:
            if animal.text[0] in letters_dict.keys():
                letters_dict[animal.text[0]] += 1
            else:
                letters_dict[animal.text[0]] = 1
        links = soup.find('div', id='mw-pages').findAll('a')
        for a in links:
            if a.text == 'Следующая страница':
                new_url = 'https://ru.wikipedia.org/' + a.get('href')
                page = requests.get(new_url).text
                break
        else:
            return letters_dict


if __name__ == '__main__':
    my_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    dictionary_of_letters = find_letters(my_url)
    for id_c in dictionary_of_letters.keys():
        print(id_c + ':', dictionary_of_letters[id_c])
