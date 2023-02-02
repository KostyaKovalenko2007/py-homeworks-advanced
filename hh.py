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
                desc = self.get_vacancy_description(url=link['href'])
                # :( Почемуто не работает вариант
                #self.vacancies.append({'vacancy_name': link.text,'url':link['href'],}.update(desc)) возвращает None
                #пришлось заморачиваться
                self.vacancies.append({'vacancy_name': link.text,
                                       'url':link['href'],
                                       'salary':desc['salary'],
                                       'city':desc['city'],
                                       'company':desc['company'],
                                       'vacancy_description':desc['vacancy_description']})



    def get_vacancy_description(self,url):
        resp = self.session.get(url=url)
        if resp.status_code == 200:
            soap = bs(resp.text,'html.parser')
            description = soap.find('div', attrs={'class': "vacancy-description"}).text
            salary = soap.find('div', attrs={'data-qa':'vacancy-salary'})
            company = soap.find('a', attrs={'data-qa':"vacancy-company-name"})
            city = soap.find('p', attrs={'data-qa':"vacancy-view-location"})
            if city == None:
                city = soap.find('span', attrs={'data-qa': "vacancy-view-raw-address"}).text.split(",")[0]
            else:
                city=city.text
            return {'salary':salary.span.get_text(),'company':company.span.text,'city':city,'vacancy_description':description,}
        return None
        pass

    def filter_by(self,text=["Django", "Flask"]):
        result=[]
        for vacancy in self.vacancies:
            check = True
            for search in text:
                if str(vacancy['vacancy_description']).count(search) <= 0:
                    check = False
            if check:
                result.append(vacancy)
        return result






if __name__ == "__main__":
    hh = hh()
    hh.get_list_of_vacancies()
    print('Number of provided vacancies by HH:', len(hh.vacancies))
    print(hh.vacancies)
    print('After filtration:',len(hh.filter_by()))
    print(hh.filter_by())
