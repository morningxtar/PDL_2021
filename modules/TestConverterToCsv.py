import unittest
import modules.ConverterToCsv as md
from os import listdir
from os.path import isfile, join, isdir


class TestConverterToCsv(unittest.TestCase):

    def test_transform_wikiurls_to_realurls(self):
        urls = md.transform_wikiurls_to_realurls()
        for url in urls:
            self.assertIsNot(url)
        self.assertEquals(335, len(urls))

    def test_check_found_url(self):
        self.assertTrue(md.check_found_url())

    def test_get_tables_contents_from_url(self):
        self.fail()

    def test_write_csv_files(self):
        md.write_csv_files()
        # path
        monRepertoire_output = '../output/{}'
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

    def test_write_csv_files(self):
        self.fail()
