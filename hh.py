"""Необходимо парсить страницу со свежими вакансиями с поиском по "Python" и городами "Москва" и "Санкт-Петербург". Эти параметры задаются по ссылке"""
import requests

class hh():
    vacancies = []
    session = None
    def __init__(self):
        self.session = requests.session()
        pass
    def get_list_of_vacancies(self,url="https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"):
        print(url)
        resp = self.session.get(url=url)
        # if resp.status_code == 200:
        print(resp.text)



if __name__ == "__main__":
    hh = hh()
    hh.get_list_of_vacancies()
