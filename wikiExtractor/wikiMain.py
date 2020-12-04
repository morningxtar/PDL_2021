# importing the libraries
import pandas as pd
import lxml
import html5lib
import time
import os

# importing the libraries
from bs4 import BeautifulSoup
import requests
import os


class ConverterToCsv:
    # Ajouter a base_url le nom de la page wikipedia pour obtenir l'adresse exacte.
    def transform_wikiurls_to_realurls(wikiurls):
        base_url = 'https://en.wikipedia.org/wiki/'
        real_wikiurls = []
        for wikiurl in wikiurls:
            wikiurl = base_url + wikiurl
            real_wikiurls.append(wikiurl.strip())
        return real_wikiurls

    # Retourne deux valeurs : le code d'erreur et True si l'url contient des tables avec un attribut wikitable
    def check_found_url(url):
        req = requests.get(url)
        soup = BeautifulSoup(req.text, features='html.parser')
        _tables = soup.find_all("table", attrs={"class": "wikitable"})
        # print(soup.prettify())
        return req.status_code, len(_tables) != 0

    # Retourne le contenu des tables à partir de l'url
    def get_tables_contents_from_url(url):
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, features='html.parser')
        _tables = soup.find_all("table", attrs={"class": "wikitable"})
        return _tables

    # Ecrire dans un fichier csv les données extraites
    def write_csv_files(dataframe, filename):
        # print((dataframe))
        dataframe.to_csv(r'{}'.format(filename + '.csv'), index=False)

        # print(list(filter(None, lines_contents[0].text.split('\n\n'))))
        # print(lines_contents[2])

    def count_csv_files(output):
        number_of_files = sum([len(files) for r, d, files in os.walk(output)])
        return number_of_files

    def test(_tables):
        lines_contents = _tables[5].tbody.find_all('tr')
        # print(lines_contents[0].find_all('th'))
        # print(lines_contents[0].find_all('td'))
        line_content = lines_contents[0].find_all('th') + lines_contents[0].find_all('td')
        # print(heading)
        # heading = list(filter(None, lines_contents[5].text.split('\n\n')))
        for index, head in enumerate(line_content):
            line_content[index] = ''
            if head.has_attr('colspan') and not head.has_attr('rowspan'):
                line_content[index] = line_content[index] + 'c' + head['colspan'] + '/'
            elif head.has_attr('rowspan') and not head.has_attr('colspan'):
                line_content[index] = line_content[index] + 'r' + head['rowspan'] + '/'
            elif head.has_attr('rowspan') and head.has_attr('colspan'):
                line_content[index] = line_content[index] + 'c' + head['colspan'] + ',r' + head['rowspan'] + '/'
            else:
                line_content[index] = line_content[index] + 'c1,r1/'
            if head.text[0] == '\n' or head.text[len(head.text) - 1] == '\n':
                line_content[index] = line_content[index] + head.text.replace('\n', ' ').strip()
            else:
                line_content[index] = line_content[index] + head.text.replace('\n', ' ')



def extractor_python():
    wikiurls_path = '../input/wikiurls.txt'
    output_path = '../output'
    statistics_path = '../statistics'
    start_time = time.time()
    os.mkdir('../statistics') if not os.path.isdir('../statistics') else ''
    os.mkdir(output_path) if not os.path.isdir('../output') else ''

    with open(wikiurls_path, 'r') as f:
        files_no_extracted = []
        urls_invalid = []
        status_code_list = []
        number_of_files_no_extracted = 0
        urls = ConverterToCsv.transform_wikiurls_to_realurls(f.readlines())
        for url in urls:
            print(url)
            namefolder = url.split('/')[len(url.split('/')) - 1]
            status_code, wikitable_bool = ConverterToCsv.check_found_url(url)
            if status_code == 200 and wikitable_bool:
                try:
                    dataframes = pd.read_html(url, attrs={"class": "wikitable"})
                    #  print(len(dataframes))
                    for index, dataframe in enumerate(dataframes):
                        filename = namefolder + '_{}'.format(index)
                        ConverterToCsv.write_csv_files(dataframe, '../output/{}'.format(filename))
                except Exception as e:
                    number_of_files_no_extracted = + number_of_files_no_extracted
                    files_no_extracted.append(
                        '{}, tableau {} non extrait'.format(url, filename) + ',erreur {}'.format(e))
            else:
                urls_invalid.append(url)
                status_code_list.append(status_code)

        with open("../statistics/invalid_urls.txt", "w") as text_file:
            for url_invalid in urls_invalid:
                print(f"{url_invalid}", file=text_file)

        nombre_tableaux_extraits = ConverterToCsv.count_csv_files(output_path)
        print()
        print('--- stats ---')
        print()
        print('tableaux non extraits {}'.format(files_no_extracted))
        print('{} tableaux non extraits'.format(number_of_files_no_extracted))
        print('{} tableaux extraits'.format(ConverterToCsv.count_csv_files(output_path)))

        execution_time = (time.time() - start_time)
        df = pd.DataFrame({
            'nombre tableaux extraits': [nombre_tableaux_extraits],
            'nombre tableaux non extraits': [number_of_files_no_extracted],
            'temps execution en seconde': [execution_time],
        })
        df.to_csv(r'{}'.format(statistics_path + '/general_statistic.csv'), index=False)
    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    duration = extractor_python()
    print("Duration of the extractors in python: {} s".format(duration))
