import re
import os
import shutil
import string
import random
import requests
from bs4 import BeautifulSoup
from alive_progress import alive_bar

def get_images(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    the_image_link = soup.find('a', class_='image', href=True)

    new_path = the_image_link['href']

    level_2_link = f'https://en.wikipedia.org{new_path}'

    level_2_page = requests.get(level_2_link)

    level_2_soup = BeautifulSoup(level_2_page.content, 'html.parser')

    the_image = level_2_soup.find('a', class_='internal', href=True)

    return the_image['href']

def useRegex(input_list):

    print('')
    print('Filtering paths, getting only relevant paths.')
    print('')

    paths = []

    paths_ = []

    with alive_bar(len(input_list), bar = 'blocks', spinner = 'waves') as bar:

        for input in input_list:

            pattern = re.compile(r"^//upload.wikimedia.org/wikipedia/commons/.*jpg$", re.IGNORECASE)

            paths.append(pattern.findall(input))

            bar()

    res = [ele for ele in paths if ele != []]

    for list in res:

        paths_.append(list[0])

    return paths_

def random_word(length):

   letters = string.ascii_lowercase

   return ''.join(random.choice(letters) for i in range(length))

def download_images(path_list):

    print('')
    print('Downloading images.')
    print('')

    with alive_bar(len(path_list), bar = 'blocks', spinner = 'waves') as bar:

        for image_url in path_list:

            image_name = random_word(15)

            image_file = requests.get(f'https:{image_url}', stream=True)

            if image_file.status_code == 200:

                image_file.raw.decode_content = True

                file_name = f'/home/loisa/Pictures/cat_species/cat_image_{image_name}.jpg'

                with open(file_name, 'wb') as file:

                    shutil.copyfileobj(image_file.raw, file)

            else:

                print('\nError: 404 \nImage not found.')

            bar()

def main():

    url = [
        'https://en.wikipedia.org/wiki/Abyssinian_cat',
        'https://en.wikipedia.org/wiki/Aegean_cat',
        'https://en.wikipedia.org/wiki/American_Bobtail',
        'https://en.wikipedia.org/wiki/American_Curl',
        'https://en.wikipedia.org/wiki/American_Shorthair',
        'https://en.wikipedia.org/wiki/American_Wirehair',
        'https://en.wikipedia.org/wiki/Cyprus_cat#Aphrodite_Giant',
        'https://en.wikipedia.org/wiki/Arabian_Mau',
        'https://en.wikipedia.org/wiki/Asian_cat',
        'https://en.wikipedia.org/wiki/Asian_Semi-longhair',
        'https://en.wikipedia.org/wiki/Australian_Mist',
        'https://en.wikipedia.org/wiki/Balinese_cat',
        'https://en.wikipedia.org/wiki/Bambino_cat',
        'https://en.wikipedia.org/wiki/Bengal_cat',
        'https://en.wikipedia.org/wiki/Birman',
        'https://en.wikipedia.org/wiki/Bombay_cat',
        'https://en.wikipedia.org/wiki/Brazilian_Shorthair',
        'https://en.wikipedia.org/wiki/British_Longhair',
        'https://en.wikipedia.org/wiki/Burmese_cat',
        'https://en.wikipedia.org/wiki/Burmilla',
        'https://en.wikipedia.org/wiki/California_Spangled',
        'https://en.wikipedia.org/wiki/Chantilly-Tiffany',
        'https://en.wikipedia.org/wiki/Chartreux',
        'https://en.wikipedia.org/wiki/Chausie',
        'https://en.wikipedia.org/wiki/Colorpoint_Shorthair',
        'https://en.wikipedia.org/wiki/Cornish_Rex',
        'https://en.wikipedia.org/wiki/Cymric_cat',
        'https://en.wikipedia.org/wiki/Cyprus_cat',
        'https://en.wikipedia.org/wiki/Devon_Rex',
        'https://en.wikipedia.org/wiki/Donskoy_cat',
        'https://en.wikipedia.org/wiki/Dragon_Li',
        'https://en.wikipedia.org/wiki/List_of_experimental_cat_breeds#Dwelf',
        'https://en.wikipedia.org/wiki/Egyptian_Mau',
        'https://en.wikipedia.org/wiki/European_Shorthair',
        'https://en.wikipedia.org/wiki/Exotic_Shorthair',
        'https://en.wikipedia.org/wiki/Foldex_cat',
        'https://en.wikipedia.org/wiki/German_Rex',
        'https://en.wikipedia.org/wiki/Havana_Brown',
        'https://en.wikipedia.org/wiki/Highlander_cat',
        'https://en.wikipedia.org/wiki/Himalayan_cat',
        'https://en.wikipedia.org/wiki/Japanese_Bobtail',
        'https://en.wikipedia.org/wiki/Javanese_cat',
        'https://en.wikipedia.org/wiki/Khao_Manee',
        'https://en.wikipedia.org/wiki/Korat',
        'https://en.wikipedia.org/wiki/Korean_Bobtail',
        'https://en.wikipedia.org/wiki/Kurilian_Bobtail',
        'https://en.wikipedia.org/wiki/Lambkin_(cat)',
        'https://en.wikipedia.org/wiki/LaPerm',
        'https://en.wikipedia.org/wiki/Lykoi',
        'https://en.wikipedia.org/wiki/Maine_Coon',
        'https://en.wikipedia.org/wiki/Manx_cat',
        'https://en.wikipedia.org/wiki/Mekong_Bobtail',
        'https://en.wikipedia.org/wiki/Minskin',
        'https://en.wikipedia.org/wiki/Minuet_cat',
        'https://en.wikipedia.org/wiki/Munchkin_cat',
        'https://en.wikipedia.org/wiki/Nebelung',
        'https://en.wikipedia.org/wiki/Norwegian_Forest_cat',
        'https://en.wikipedia.org/wiki/Ocicat',
        'https://en.wikipedia.org/wiki/Ojos_Azules',
        'https://en.wikipedia.org/wiki/Oriental_bicolour',
        'https://en.wikipedia.org/wiki/Oriental_Longhair',
        'https://en.wikipedia.org/wiki/Oriental_Shorthair',
        'https://en.wikipedia.org/wiki/Persian_cat',
        'https://en.wikipedia.org/wiki/Traditional_Persian',
        'https://en.wikipedia.org/wiki/Peterbald',
        'https://en.wikipedia.org/wiki/Pixie-bob',
        'https://en.wikipedia.org/wiki/Ragamuffin_cat',
        'https://en.wikipedia.org/wiki/Ragdoll',
        'https://en.wikipedia.org/wiki/Russian_Blue',
        'https://en.wikipedia.org/wiki/Savannah_cat',
        'https://en.wikipedia.org/wiki/Scottish_Fold',
        'https://en.wikipedia.org/wiki/Selkirk_Rex',
        'https://en.wikipedia.org/wiki/Serengeti_cat',
        'https://en.wikipedia.org/wiki/Siamese_cat',
        'https://en.wikipedia.org/wiki/Siberian_cat',
        'https://en.wikipedia.org/wiki/Singapura_cat',
        'https://en.wikipedia.org/wiki/Snowshoe_cat',
        'https://en.wikipedia.org/wiki/Sokoke',
        'https://en.wikipedia.org/wiki/Somali_cat',
        'https://en.wikipedia.org/wiki/Sphynx_cat',
        'https://en.wikipedia.org/wiki/Suphalak',
        'https://en.wikipedia.org/wiki/Korat#Thai_Lilac,_Thai_Blue_Point_and_Thai_Lilac_Point',
        'https://en.wikipedia.org/wiki/Tonkinese_cat',
        'https://en.wikipedia.org/wiki/Tonkinese_cat',
        'https://en.wikipedia.org/wiki/Toyger',
        'https://en.wikipedia.org/wiki/Turkish_Angora',
        'https://en.wikipedia.org/wiki/Turkish_Van',
        'https://en.wikipedia.org/wiki/Van_cat',
        'https://en.wikipedia.org/wiki/Ukrainian_Levkoy',
        'https://en.wikipedia.org/wiki/York_Chocolate'
    ]

    image_list = []

    os.system('cls' if os.name == 'nt' else 'clear')

    print('Scrapper is now running...')
    print('')
    print('Fetching image paths.')
    print('')

    with alive_bar(len(url), bar = 'blocks', spinner = 'waves') as bar:

        for i in url:

            image_list.append(get_images(i))

            bar()

    path_list = useRegex(image_list)

    download_images(path_list)

    print('')
    print('Scrapping process complete.')
    print('')

if __name__ == '__main__':

    main()

