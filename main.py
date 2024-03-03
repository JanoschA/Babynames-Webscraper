import requests
import csv
from bs4 import BeautifulSoup


def get_names_and_ranks(url, gender):
    form_data = {
        'tx_kkbabynames_ranklist[filter][gender]': gender,
        'tx_kkbabynames_ranklist[filter][dateInterval]': 'lastYear',  # last30Days, last60Days, lastYear are possible
    }

    with requests.Session() as session:
        first_response = session.post(url, data=form_data)

        names_and_ranks = []

        for i in range(20):
            soup = BeautifulSoup(first_response.text, 'html.parser')

            name_elements = soup.select('div.name')

            names_and_ranks += [
                (int(element.text.split('.')[0].replace('\n', '')), element.text.split('.')[1].replace('\n', '')) for
                element in name_elements]

            next_page_link = soup.select_one('a.page-link[aria-label*="Zur nächsten Seite"]')

            if next_page_link is None:
                break

            next_page_url = 'https://www.hipp.de' + next_page_link['href']

            first_response = session.get(next_page_url)

    return names_and_ranks


girls = get_names_and_ranks(
    'https://www.hipp.de/schwanger/ratgeber/babynamen/top-200-vornamen/', 'f')
boys = get_names_and_ranks(
    'https://www.hipp.de/schwanger/ratgeber/babynamen/top-200-vornamen/', 'm')

with open('names.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    writer.writerow(['Position', 'Girlname', 'Boyname'])

    for girl, boy in zip(girls, boys):
        girl_rank, girl_name = girl
        boy_rank, boy_name = boy
        writer.writerow([girl_rank, girl_name, boy_name])
