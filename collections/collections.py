class task1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    def __init__(self):
        pass
    def get_russia_visits(self, country='Россия'):
        out= []
        for trip in self.geo_logs:

            if trip.get(list(trip.keys())[0])[1] == country:
                out.append(trip)
        return out

class task2():
    def __init__(self):
        pass

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    def get_unique(self):
        out = []
        for item in self.ids:
            out.extend(list(self.ids[item]))
        return list(set(out))
class task4():
    def __init__(self):
        pass

    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    def get_max(self):
        return sorted(self.stats.items(), key=lambda item: item[1], reverse = True)[0][0]



if __name__ == '__main__':
    task1 = task1()
    print(task1.get_russia_visits())
    task2 = task2()
    print(task2.get_unique())
    task4 = task4()
    print(task4.get_max())