import unittest
import os
from app import create_app, db
from app.models import Material


class MaterialTasteCase(unittest.TestCase):

    def setUp(self):
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

    def test_material(self):
        material = self.__get_material()

        self.assertEqual(material.name, self.NAME_TEST)
        self.assertEqual(material.description, self.DESCRIPTION_TEST)
        self.assertEqual(material.measuring_unit, self.MEASURING_UNIT_TEST)
        

    def __get_material(self):
        material = Material()
        material.name = self.NAME_TEST
        material.description = self.DESCRIPTION_TEST
        material.measuring_unit = self.MEASURING_UNIT_TEST

        return material

if __name__ == '__main__':
    unittest.main()