import unittest
import modules.modules as md


class Testconverter(unittest.TestCase):

    def test_transform_wikiurls_to_realurls(self):
        md.transform_wikiurls_to_realurls("Comparison_between_Esperanto_and_Ido")
        self.assertTrue()

    def test_check_found_url(self):
        self.fail()

    def test_get_tables_contents_from_url(self):
        self.fail()

    def test_write_csv_files(self):
        self.fail()
