import unittest
import os
from app import create_app, db
from app.models import Price


class PriceTasteCase(unittest.TestCase):

    def setUp(self):
        # Stock
        self.PRICE_TEST = 45.2

        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_price(self):
        price = self.__get_price()

        self.assertEqual(price.price, self.PRICE_TEST)
        

    def __get_price(self):
        price = Price()
        price.price = self.PRICE_TEST

        return price

if __name__ == '__main__':
    unittest.main()