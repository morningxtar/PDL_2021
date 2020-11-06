# importing the libraries
import pandas as pd
import lxml
import html5lib
import os
import modules.ConverterToCsv as md
import time


def extractor_python():
    wikiurls_path = '../input/wikiurls.txt'
    output_path = '../output'

    start_time = time.time()
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(wikiurls_path, 'r') as f:
        urls = md.ConverterToCsv.transform_wikiurls_to_realurls(f.readlines())
        for url in urls:
            print(url)
            namefolder = url.split('/')[len(url.split('/')) - 1]
            status_code, wikitable_bool = md.ConverterToCsv.check_found_url(url)

            if status_code == 200 and wikitable_bool:
                try:
                    dataframes = pd.read_html(url, attrs={"class": "wikitable"})
                    number_of_files_no_extracted = 0
                    files_no_extracted = []
                    #  print(len(dataframes))
                    for index, dataframe in enumerate(dataframes):
                        filename = namefolder + '_{}'.format(index)
                        md.ConverterToCsv.write_csv_files(dataframe, '{}/{}'.format(output_path, filename))
                except Exception as e:
                    number_of_files_no_extracted = + number_of_files_no_extracted
                    files_no_extracted.append(filename + ',{}'.format(e))
        print()
        print('--- stats ---')
        print()
        print('tableaux non extraits {}'.format(files_no_extracted))
        print('{} tableaux non extraits'.format(number_of_files_no_extracted))
        print('Extractor Pyhton created {} files '.format(md.ConverterToCsv.count_csv_files(output_path)))
    end_time = time.time()

    return end_time - start_time


if __name__ == '__main__':
    duration = extractor_python()
    print("Duration of the extractors in python: {} s".format(duration))
