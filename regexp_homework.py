'''
Иногда при знакомстве мы записываем контакты в адресную книгу кое-как с мыслью, что "когда-нибудь потом все обязательно поправим". Копируем данные из интернета или из смски. Добавляем людей в разных мессенджерах. В результате получается адресная книга, в которой совершенно невозможно кого-то нормально найти: мешает множество дублей и разная запись одних и тех же имен.

Кейс основан на реальных данных из https://www.nalog.ru/opendata/, https://www.minfin.ru/ru/opendata/

Ваша задача: починить адресную книгу, используя регулярные выражения.
Структура данных будет всегда:
lastname,firstname,surname,organization,position,phone,email
Предполагается, что телефон и e-mail у человека может быть только один.
Необходимо:

поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
объединить все дублирующиеся записи о человеке в одну.

'''

from pprint import pprint
import re
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
export = []
for row in contacts_list:
  #Добавляем шапку
  if row[0] == 'lastname':
    export.append(row)
  else:
    #parce FIO
    for c  in range(3):
      fio = re.split('\s', row[c])
      if fio !=None or len(fio) >1 :
        for i in range(len(fio)):
          row[i+c] = fio[i]
    #parce Phone
    if row[5] != '':
      tel_split = re.split('доб.',row[5])
      phone = re.findall("\d",tel_split[0])
      row[5] = f'+7({"".join(phone[1:4])}){"".join(phone[4:7])}-{"".join(phone[7:9])}-{"".join(phone[9:11])}'
      if len(tel_split) > 1:
        phone = re.findall("\d", tel_split[1])
        row[5]+= f" доб.{''.join(phone)};"
    #find duplicates
    counter = 0
    if len(export) != 0:
      # Если выходной список не пуст, бежим по всем записям
      for c in range(len(export)):
        #Сравниваем ФИО и счетаем совпадения полей
        for i in range(3):
          if export[c][i] == row[i]:
            counter +=1
      #Если их больше 1 то считаем что дубликат
      if counter > 1:
        for i in range(7):
          # пробегаемся по всем полям и если в выходном списке поле пустое а обработанном поле заполненно, обновляем.
          export[c][i]  = row[i] if export[c][i] == '' and row[i] != '' else export[c][i]
      else:
        #Если совпадений не найдено, добавляем новую запись
        export.append(row)
contacts_list = export
pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
