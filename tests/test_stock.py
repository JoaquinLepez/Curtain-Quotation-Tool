import unittest
import os
from app import create_app, db
from app.models import Stock


class StockTasteCase(unittest.TestCase):

    def setUp(self):
        # Stock
        self.AMOUNT_TEST = 3

        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_stockl(self):
        stock = self.__get_stock()

        self.assertEqual(stock.amount, self.AMOUNT_TEST)
        

    def __get_stock(self):
        stock = Stock()
        stock.amount = self.AMOUNT_TEST

        return stock

if __name__ == '__main__':
    unittest.main()