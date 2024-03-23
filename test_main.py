
import unittest
from main import Model


class TestModel(unittest.TestCase):

    def test_mi_to_km(self):
        # проверка ожидаемого значения
        model = Model(10)
        mi_to_km = model.mi_to_km()
        self.assertEqual(mi_to_km, 16.09344)

    def test_value_with_wrong_type(self):
        # Тестирование ожидаемого исключения
        # при изменении состояния value
        model = Model(10)
        with self.assertRaises(TypeError):
            model.value = 'abc'
            model.value = False
