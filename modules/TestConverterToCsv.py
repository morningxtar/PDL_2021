import unittest
import modules.ConverterToCsv as md
from os import listdir
from os.path import isfile, join, isdir


class TestConverterToCsv(unittest.TestCase):

    def test_transform_wikiurls_to_realurls(self):
        wikiurls_path = '../input/wikiurls.txt'
        with open(wikiurls_path, 'r') as f:
            urls = md.ConverterToCsv.transform_wikiurls_to_realurls(f.readlines())

        self.assertEquals(336, len(urls))

    # check if each url return 200 so it's successful and each contains wikitable
    def test_check_found_url(self):
        wikiurls_path = '../input/wikiurls.txt'
        with open(wikiurls_path, 'r') as f:
            urls = md.ConverterToCsv.transform_wikiurls_to_realurls(f.readlines())
            for url in urls:
                status_code, has_wikitable = md.ConverterToCsv.check_found_url(url)
                self.assertEqual(status_code, 200,
                                 '{} n\'est pas valide et renvoie une erreur {}'.format(url, status_code))
                self.assertTrue(has_wikitable, 'La page ne contient pas de wikitable')

    def test_get_tables_contents_from_url(self):
        self.fail()

    def test_write_csv_files(self):
        # path
        monRepertoire_output = '../output'
        #  Get the list of all files and directories
        #  in the root directory 'path'
        for folder in listdir(monRepertoire_output):
            # isdir Check whether
            # the specified path is
            # an existing directory or not
            self.assertTrue(isdir(folder))
            # used to check whether
            # the specified path is
            # an existing regular file or not
            self.assertTrue(isfile(join(monRepertoire_output, folder)))


if __name__ == '__main__':
    unittest.main()
