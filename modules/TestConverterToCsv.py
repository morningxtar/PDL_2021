import unittest
import modules.ConverterToCsv as md
from os import listdir
from os.path import isfile, join, isdir


class TestConverterToCsv(unittest.TestCase):

    def test_transform_wikiurls_to_realurls(self):
        wikiurls_path = '../input/wikiurls.txt'
        with open(wikiurls_path, 'r') as f:
            urls = md.ConverterToCsv.transform_wikiurls_to_realurls(f.readlines())
        '''for url in urls:
            self.assertIsNone(url)
            '''
        self.assertEqual(336, len(urls))

    def test_check_found_url1(self):
        url_sans_tab = "https://en.wikipedia.org/wiki/Comparison_of_Axis_&_Allies_games"
        url_avec_tab = "https://en.wikipedia.org/wiki/Comparison_of_Asian_national_space_programs"
        code, result_bool = md.ConverterToCsv.check_found_url(url_sans_tab)
        self.assertFalse(result_bool)
        self.assertEqual(404, code)
        code, result_bool = md.ConverterToCsv.check_found_url(url_avec_tab)
        self.assertTrue(result_bool)
        self.assertEqual(200, code)
            # self.assertNotEqual(md.ConverterToCsv.check_found_url(url)[1], 0)

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
            # isdir Check whether
            # the specified path is
            # an existing directory or not
            # self.assertTrue(isfile(folder))
            # used to check whether
            # the specified path is
            # an existing regular file or not
            self.assertTrue(isfile(join(monRepertoire_output, folder)))


if __name__ == '__main__':
    unittest.main()
