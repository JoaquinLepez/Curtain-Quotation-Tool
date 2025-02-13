import unittest
import os
from app import create_app, db
from app.models import Stock, Material, Chain, Mechanism, Pipe, Fabric


class StockTasteCase(unittest.TestCase):

    def setUp(self):
        # Stock 
        self.AMOUNT_TEST = 3
        
        # Material 
        self.NAME_TEST = "Tela"
        self.DESCRIPTION_TEST = "Tela color gris de blackout"
        self.MEASURING_UNIT_TEST = "Metros cuadrados"

        # Chain - Pipe
        self.METERS_TEST = 5.3

        # Mechanism
        self.UNITS_TEST = 3

        # Fabric
        self.WIDTH_TEST = 5
        self.HEIGHT_TEST = 4

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

        self.assertIsNotNone(stock.chains)
        self.assertEqual(stock.chains.meters, self.METERS_TEST)
        
        self.assertIsNotNone(stock.mechanisms)
        self.assertEqual(stock.mechanisms.units, self.UNITS_TEST)

        self.assertIsNotNone(stock.pipes)
        self.assertEqual(stock.pipes.meters, self.METERS_TEST)

        self.assertIsNotNone(stock.fabrics)
        self.assertEqual(stock.fabrics.height, self.HEIGHT_TEST)
        self.assertEqual(stock.fabrics.width, self.WIDTH_TEST)

    def __get_stock(self):
        material = Material()
        material.name = self.NAME_TEST
        material.description = self.DESCRIPTION_TEST
        material.measuring_unit = self.MEASURING_UNIT_TEST

        chain = Chain()
        chain.meters = self.METERS_TEST

        mechanism = Mechanism()
        mechanism.units = self.UNITS_TEST

        pipe = Pipe()
        pipe.meters = self.METERS_TEST

        fabric = Fabric()
        fabric.height = self.HEIGHT_TEST
        fabric.width = self.WIDTH_TEST

        stock = Stock()
        stock.amount = self.AMOUNT_TEST
        stock.material = material
        stock.chains = chain
        stock.mechanisms = mechanism
        stock.pipes = pipe
        stock.fabrics = fabric

        return stock

if __name__ == '__main__':
    unittest.main()