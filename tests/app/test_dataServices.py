from unittest import TestCase

from backend import dataServices
from backend.database import db_session
from backend.models import User


class LoadFromCsv(TestCase):
    def test_load_and_save_data(self):
        dataServices.CsvDataService().insert_many_from_http([["c", "f"], [12, 14]])

    pass


class test_ing(TestCase):
    def test_encrypt(self):
        user = User()
        user.password = b"myp4ss"
        user.email = "german@german.com"

        db_session.add(user)
        db_session.commit()

    def test_decrypt(self):
        user = User.query.filter().first()
        db_session.delete(user)
        db_session.commit()
