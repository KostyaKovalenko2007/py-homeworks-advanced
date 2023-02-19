import unittest
#from lection4 import task1
def multyp(a,b):
    return a*b

class TestCollection(unittest.TestCase):
    # def test_task1_check_countries(self):
    #     task = task1()
    #     self.assertEqual(task.get_russia_visits(),
    #                      [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']},
    #                       {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']},
    #                       {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}])
    def test_numbers(self):
        self.assertEqual(multyp(3,4),12)


