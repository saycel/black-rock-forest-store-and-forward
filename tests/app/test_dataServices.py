from unittest import TestCase

from backend import dataServices


class LoadFromCsv(TestCase):
    def test_load_and_save_data(self):
        dataServices.CsvDataService().insert_many_from_http([["c","f"],[12,14]])