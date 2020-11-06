# importing the libraries
import pandas as pd
import lxml
import html5lib
import time
import os
import modules.ConverterToCsv as md

wikiurls_path = '../input/wikiurls.txt'
output_path = '../output'
statistics_path = '../statistics'

if __name__ == '__main__':
    start_time = time.time()
    os.mkdir('../statistics') if not os.path.isdir('../statistics') else ''
    os.mkdir(output_path) if not os.path.isdir('../output') else ''

    with open(wikiurls_path, 'r') as f:
        files_no_extracted = []
        urls_invalid = []
        status_code_list = []
        number_of_files_no_extracted = 0
        urls = md.ConverterToCsv.transform_wikiurls_to_realurls(f.readlines())
        for url in urls:
            print(url)
            namefolder = url.split('/')[len(url.split('/')) - 1]
            status_code, wikitable_bool = md.ConverterToCsv.check_found_url(url)
            if status_code == 200 and wikitable_bool:
                try:
                    dataframes = pd.read_html(url, attrs={"class": "wikitable"})
                    #  print(len(dataframes))
                    for index, dataframe in enumerate(dataframes):
                        filename = namefolder + '_{}'.format(index)
                        md.ConverterToCsv.write_csv_files(dataframe, '../output/{}'.format(filename))
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

        nombre_tableaux_extraits = md.ConverterToCsv.count_csv_files(output_path)
        print()
        print('--- stats ---')
        print()
        print('tableaux non extraits {}'.format(files_no_extracted))
        print('{} tableaux non extraits'.format(number_of_files_no_extracted))
        print('{} tableaux extraits'.format(md.ConverterToCsv.count_csv_files(output_path)))

        execution_time = (time.time() - start_time)
        df = pd.DataFrame({
            'nombre tableaux extraits': [nombre_tableaux_extraits],
            'nombre tableaux non extraits': [number_of_files_no_extracted],
            'temps execution en seconde': [execution_time],
        })
        df.to_csv(r'{}'.format(statistics_path + '/general_statistic.csv'), index=False)
