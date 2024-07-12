import unittest
import os
from app import create_app, db
from app.models import Stock, Material


class StockTasteCase(unittest.TestCase):

    def setUp(self):
        # Stock 
        self.AMOUNT_TEST = 3
        
        # Material 
        self.NAME_TEST = "Tela"
        self.DESCRIPTION_TEST = "Tela color gris de blackout"
        self.MEASURING_UNIT_TEST = "Metros cuadrados"

        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_stock(self):
        stock = self.__get_stock()

        self.assertEqual(stock.amount, self.AMOUNT_TEST)
        self.assertIsNotNone(stock.material)
        self.assertEqual(stock.material.name, self.NAME_TEST)
        self.assertEqual(stock.material.description, self.DESCRIPTION_TEST)
        self.assertEqual(stock.material.measuring_unit, self.MEASURING_UNIT_TEST)

    def __get_stock(self):
        material = Material()
        material.name = self.NAME_TEST
        material.description = self.DESCRIPTION_TEST
        material.measuring_unit = self.MEASURING_UNIT_TEST

        stock = Stock()
        stock.amount = self.AMOUNT_TEST
        stock.material = material

        return stock

if __name__ == '__main__':
    unittest.main()