import unittest
import os
from app import create_app, db
from app.models import Price, Material
from app.services import PriceService

price_service = PriceService()

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
    
    def test_price_save(self):
        price = self.__get_price()
        price_service.save(price)
        self.assertGreaterEqual(price.id,1)
        self.assertEqual(price.price, self.PRICE_TEST)
        self.assertEqual(price.material.name, self.NAME_TEST)
        self.assertEqual(price.material.description, self.DESCRIPTION_TEST)
        self.assertEqual(price.material.measuring_unit, self.MEASURING_UNIT_TEST)
    
    def test_price_update(self):
        price = self.__get_price()
        price_service.save(price)

        price.price = 123
        price.material.name = "Pipe test"

        price_service.update(price, price.id)
        self.assertEqual(price.price, 123)
        self.assertEqual(price.material.name, "Pipe test")
    
    def test_price_delete(self):
        price = self.__get_price()
        price_service.save(price)
        price_service.delete(price.id)
        self.assertIsNone(price_service.find(price.id))
    
    def test_price_all(self):
        price = self.__get_price()
        price_service.save(price)
        self.assertGreaterEqual(len(price_service.all()),1)
    
    def test_price_find(self):
        price = self.__get_price()
        price_service.save(price)

        self.assertEqual(price_service.find(price.id), price)
    
    def test_price_find_by_id_material(self):
        price = self.__get_price()
        price_service.save(price)

        self.assertEqual(price_service.find_by_material_id(price.material_id), price)

    def __get_price(self) -> Price:
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


