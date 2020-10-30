# importing the libraries
import pandas as pd
import lxml
import html5lib

import modules.modules as md

wikiurls_path = '../input/wikiurls.txt'

if '__main__' == '__main__':
    with open(wikiurls_path, 'r') as f:
        urls = md.transform_wikiurls_to_realurls(f.readlines())
        for url in urls:
            print(url)
            namefolder = url.split('/')[len(url.split('/')) - 1]
            status_code, wikitable_bool = md.check_found_url(url)

            if status_code == 200 and wikitable_bool:
                dataframes = pd.read_html(url, attrs={"class": "wikitable"})
                for index, dataframe in enumerate(dataframes):
                    filename = namefolder + '_{}'.format(index)
                    md.write_csv_files(dataframe, '../output/{}'.format(filename))
