import unittest
import modules.ConverterToCsv as md
import requests
from os import listdir
from os.path import isfile, join, isdir


class TestConverterToCsv(unittest.TestCase):

    def test_transform_wikiurls_to_realurls(self):
        wikiurls_path = '../input/wikiurls.txt'
        with open(wikiurls_path, 'r') as f:
            urls = md.ConverterToCsv.transform_wikiurls_to_realurls(f.readlines())
        dataset = ["https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido",
                   "https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Interlingua",
                   "https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Novial"]
        self.assertEqual(336, len(urls))
        self.assertTrue(all(item in urls for item in dataset))

    def test_check_found_url(self):
        url_sans_tab = "https://en.wikipedia.org/wiki/Comparison_of_Axis_&_Allies_games"
        url_avec_tab = "https://en.wikipedia.org/wiki/Comparison_of_Asian_national_space_programs"
        code, result_bool = md.ConverterToCsv.check_found_url(url_sans_tab)
        self.assertFalse(result_bool)
        self.assertEqual(404, code)
        code, result_bool = md.ConverterToCsv.check_found_url(url_avec_tab)
        self.assertTrue(result_bool)
        self.assertEqual(200, code)

    def test_get_tables_contents_from_url(self):
        urlsTab = "https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido"
        tabs = md.ConverterToCsv.get_tables_contents_from_url(urlsTab)
        self.assertEqual(8, len(tabs))

    def test_write_csv_files(self):
        # path
        monRepertoire_output = '../output'
        #  Get the list of all files and directories
        #  in the root directory 'path'
        for folder in listdir(monRepertoire_output):
            self.assertTrue(isfile(join(monRepertoire_output, folder)))

    def test_count_csv_files(self):
        path_output = '../output'
        nbFiles = 0
        for folder in listdir(path_output):
            if isfile(join(path_output, folder)):
                nbFiles = nbFiles + 1
        self.assertEqual(nbFiles, md.ConverterToCsv.count_csv_files(path_output))


if __name__ == '__main__':
    unittest.main()
