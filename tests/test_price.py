import unittest
import os
from app import create_app, db
from app.models import Price, Material


class PriceTasteCase(unittest.TestCase):

    def setUp(self):
        # Price
        self.PRICE_TEST = 45.2

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

    def test_price(self):
        price = self.__get_price()

        self.assertEqual(price.price, self.PRICE_TEST)
        self.assertIsNotNone(price.material)
        self.assertEqual(price.material.name, self.NAME_TEST)
        self.assertEqual(price.material.description, self.DESCRIPTION_TEST)
        self.assertEqual(price.material.measuring_unit, self.MEASURING_UNIT_TEST)

    def __get_price(self):
        price = Price()
        price.price = self.PRICE_TEST

        material = Material()
        material.name = self.NAME_TEST
        material.description = self.DESCRIPTION_TEST
        material.measuring_unit = self.MEASURING_UNIT_TEST

        price.material = material

        return price

if __name__ == '__main__':
    unittest.main()