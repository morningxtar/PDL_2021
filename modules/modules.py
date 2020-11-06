# importing the libraries
from bs4 import BeautifulSoup
import requests
import os


def transform_wikiurls_to_realurls(wikiurls):
    base_url = 'https://en.wikipedia.org/wiki/'
    real_wikiurls = []
    for wikiurl in wikiurls:
        wikiurl = base_url + wikiurl
        real_wikiurls.append(wikiurl.strip())
    return real_wikiurls


def check_found_url(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, features='html.parser')
    _tables = soup.find_all("table", attrs={"class": "wikitable"})
    # print(soup.prettify())
    return req.status_code, len(_tables) != 0


def get_tables_contents_from_url(url):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, features='html.parser')
    _tables = soup.find_all("table", attrs={"class": "wikitable"})
    return _tables


def write_csv_files(dataframe, filename):
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
