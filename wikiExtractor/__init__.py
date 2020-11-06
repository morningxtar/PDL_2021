# importing the libraries
import pandas as pd
import lxml
import html5lib

import modules.modules as md

wikiurls_path = '../input/wikiurls.txt'
output_path = '../output'

if __name__ == '__main__':
    with open(wikiurls_path, 'r') as f:
        urls = md.transform_wikiurls_to_realurls(f.readlines())
        for url in urls:
            print(url)
            namefolder = url.split('/')[len(url.split('/')) - 1]
            status_code, wikitable_bool = md.check_found_url(url)

            if status_code == 200 and wikitable_bool:
                try:
                    dataframes = pd.read_html(url, attrs={"class": "wikitable"})
                    number_of_files_no_extracted = 0
                    files_no_extracted = []
                    for index, dataframe in enumerate(dataframes):
                        filename = namefolder + '_{}'.format(index)
                        md.write_csv_files(dataframe, '../output/{}'.format(filename))
                except Exception as e:
                    number_of_files_no_extracted = + number_of_files_no_extracted
                    files_no_extracted.append(filename + ',{}'.format(e))
        print()
        print('--- stats ---')
        print()
        print('tableaux non extraits {}'.format(files_no_extracted))
        print('{} tableaux non extraits'.format(number_of_files_no_extracted))
        print('{} tableaux extraits'.format(md.count_csv_files(output_path)))
