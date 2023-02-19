import pytest
from lection4 import task1,task2, task4


class TestLecture4_task1():
    def test_task1_country_default(self):
        assert task1().get_russia_visits() == [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']},
                                               {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']},
                                               {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]

    def test_task1_if_list_empty(self, ):
        task = task1()
        task.geo_logs = []
        assert task.get_russia_visits() == []

    @pytest.mark.parametrize("visits, country, expected", [
        ([
             {'visit1': ['Москва', 'Россия']},
             {'visit2': ['Дели', 'Индия']},
             {'visit3': ['Владимир', 'Россия']},
             {'visit4': ['Лиссабон', 'Португалия']},
             {'visit5': ['Париж', 'Франция']},
             {'visit6': ['Лиссабон', 'Португалия']},
             {'visit7': ['Тула', 'Россия']},
             {'visit8': ['Тула', 'Россия']},
             {'visit9': ['Курск', 'Россия']},
             {'visit10': ['Архангельск', 'Россия']}],
         'Индия', [{'visit2': ['Дели', 'Индия']}]),
        ([
             {'visit1': ['Москва', 'Россия']},
             {'visit2': ['Дели', 'Индия']},
             {'visit3': ['Владимир', 'Россия']},
             {'visit4': ['Лиссабон', 'Португалия']},
             {'visit5': ['Париж', 'Франция']},
             {'visit6': ['Лиссабон', 'Португалия']},
             {'visit7': ['Тула', 'Россия']},
             {'visit8': ['Тула', 'Россия']},
             {'visit9': ['Курск', 'Россия']},
             {'visit10': ['Архангельск', 'Россия']}],
         'Португалия', [{'visit4': ['Лиссабон', 'Португалия']}, {'visit6': ['Лиссабон', 'Португалия']}, ]),
        ([
             {'visit1': ['Москва', 'Россия']},
             {'visit2': ['Дели', 'Индия']},
             {'visit3': ['Владимир', 'Россия']},
             {'visit4': ['Лиссабон', 'Португалия']},
             {'visit5': ['Париж', 'Франция']},
             {'visit6': ['Лиссабон', 'Португалия']},
             {'visit7': ['Тула', 'Россия']},
             {'visit8': ['Тула', 'Россия']},
             {'visit9': ['Курск', 'Россия']},
             {'visit10': ['Архангельск', 'Россия']}],
         '', [])])
    def test_task1_parametrized(self, visits, country, expected):
        task = task1()
        task.geo_logs = visits
        assert task.get_russia_visits(country = country) == expected

class TestLecture4_task2():
    @pytest.mark.parametrize("dict, expected",[
        ({'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}, [98, 35, 15, 213, 54, 119] ),
        ({},[]),])
    def test_tast2_testcases(self, dict, expected):
        test = task2()
        test.ids=dict
        assert test.get_unique() == expected
class TestLecture4_task4():
    @pytest.mark.parametrize("dct, expected", [
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
        ({'facebook': 155, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'facebook'), #Max Facebook
        ({'facebook': 155, 'yandex': 120, 'vk': 115, 'google': 155, 'email': 42, 'ok': 98}, ['facebook','google']), #doubling
        ({},'')
    ])
    def test_task4_testcases(self,dct, expected):
        test = task4()
        test.stats = dct
        assert test.get_max() in expected