"""Необходимо парсить страницу со свежими вакансиями с поиском по "Python" и городами "Москва" и "Санкт-Петербург". Эти параметры задаются по ссылке"""
import requests
from bs4 import BeautifulSoup as bs

class hh():
    vacancies = []
    session = None
    def __init__(self):
        self.session = requests.session()
        self.session.headers.update({'User-agent': 'Mozilla/5.0',})
        pass
    def get_list_of_vacancies(self,url="https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"):
        resp = self.session.get(url=url)
        if resp.status_code == 200:
            #print(resp.text)
            soap = bs(resp.text,'html.parser')
            for link in soap.findAll('a',href=True,attrs={'class':"serp-item__title"}):
                self.vacancies.append({'vacancy_name':link.text,'url':link['href'],'vacancy_description':self.get_vacancy_description(url=link['href'])})
    def get_vacancy_description(self,url):
        resp = self.session.get(url=url)
        if resp.status_code == 200:
            #print(resp.text)
            soap = bs(resp.text,'html.parser')
            return soap.find('div', attrs={'class': "vacancy-description"}).text

        pass

    def filter_by(self,text=["Django", "Flask"]):
        result=[]
        for vacancy in self.vacancies:
            if str(vacancy['vacancy_description']).find()






if __name__ == "__main__":
    hh = hh()
    hh.get_list_of_vacancies()
    print(hh.vacancies)
