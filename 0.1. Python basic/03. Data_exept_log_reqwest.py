#Работа с датами
from datetime import datetime, timedelta  # импорт библиотек

startDate = '2017-05-01'  # формат string
endDate = '2017-05-10'  # формат string
datetime.strptime(startDate, '%Y-%m-%d')  # преобразуем формат даты

# форматы дат
# https://docs.python.org/3/library/datetime.html
datetime.strptime('May 9 2017  9:00AM', '%b %d %Y %I:%M%p')
startDateDT = datetime.strptime(startDate, '%Y-%m-%d')
endDateDT = datetime.strptime(endDate, '%Y-%m-%d')

currentDT = startDateDT

while currentDT <= endDateDT:  # создаем цикл в котором происходи увеличении дата на 1 день до достижения конечного дня
    print(currentDT.strftime('%Y-%m-%d'))
    currentDT += timedelta(days=1)

# File "<ipython-input-16-03f9feb12cc3>", line 7
print(currentDT.strftime('%Y-%m-%d'))


# Logging
# Что было бы круто:
# сообщения выводятся на экран в Jupyter notebook без задержек(как это иногда бывает у print)
# сообщения автоматом пишутся в файл в едином формате(например, когда скрипт выполняется по cron)
# https://docs.python.org/3.6/library/logging.html

import logging   # импорт библиотеки логирования

# что будем выводить / писать в файл
# https://docs.python.org/3.6/library/logging.html#logrecord-attributes

logger = logging.getLogger('Тест логгера')
hdlr = logging.FileHandler('error.log', mode='w')  # создаем файл error.log
formatter = logging.Formatter('%(asctime)s [LINE:%(lineno)d] %(levelname)s разделитель %(message)s')  # задаем формат логирования
# %(asctime)s - актуальное дата, время
# %(lineno)d - Номер исходной строки, в которой был выполнен вызов регистрации (если доступно).
# %(levelname)s - Название уровня: Текст уровень протоколирования для сообщения ( 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
# %(message)s - сообщение


hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
data = [1, 55, 'abc', 12]
for num in data:
    # проверяем входные данные на целое число
    if isinstance(num, int):
        logger.info('Ok %s', num)  # в этой строке происходи запись лога, что число целое значит ок

    else:
        logger.warning('Некорректное значение. Значение было %s', num)  # в этой строке происходи запись о ошибке


##Веб - запросы
print("веб запросы")
# для выполнения запросов к API систем используется библиотека requests
# есть еще urllib разных версий
import requests

# сделаем запрос к API Вконтакте
# используем метод users.get, который возвращает основную информацию о пользователе
# документация метода https://new.vk.com/dev/users.get
# как делать запросы к API ВКонтакте https://new.vk.com/dev/api_requests

r = requests.get('https://api.vk.com/method/users.get?user_id=1&fields=bdate&v=5.52')
# лучше писать так

url = 'https://api.vk.com/method/users.get'

params = {
    'user_id': 1,
    'fields': 'bdate',
    'v': '5.52'
}

r = requests.get(url, params=params)
# запрос сделали, посмотрим что пришло в ответ (дополнительное поле в запросе задали одно, информации минимум)

# r.{'response': [{'bdate': '10.10.1984',
#                'first_name': 'Павел',
#                'id': 1,
#                'last_name': 'Дуров'}]}
# это ответ в формате JSON
# сейчас это просто строка, с которой тяжело работать

type(r.text)
#str


# преобразуем строку в словарь, чтобы обращаться к нужным нам элементам
# используем библиотеку для работы с форматом JSON
import json

response = json.loads(r.text)
response
# {'response': [{'bdate': '10.10.1984',
#                'first_name': 'Павел',
#                'id': 1,
#                'last_name': 'Дуров'}]}


# обратите внимание, что response представляет собой словарь с единственным ключом 'response'
# значение словаря response - лист из одного элемента, который представляет собой словарь

# response['response'][0]
# для упрощения отображения заведем переменную
# data = response['response'][0]
# data['first_name']
# 'Павел'
# выведем полученную информацию
# иногда при отображении русских букв возникают ошибки
# чтобы избежать проблем в нашем случае добавляем преобразование в стандартную кодировку UTF-8

# print('ID пользователя - {:.00f}'.format(data['id']))
# print('Имя - {}'.format(data['first_name']))
# print('Фамилия - {}'.format(data['last_name']))
# print('Дата рождения - {}'.format(data['bdate']))



## Try-except
#Имеется файл data_bugs.txt с двумя столбцами чисел. Нужно посчитать сумму второго столбца.
# Проблема в том, что там файле есть две ошибки: пятый элемент не является числом, девятый - отсутствует

# итоговая сумма, которую надо посчитать
totalSum = 0

# счетчик номера строки
lineNumber = 1

with open('data_bugs.txt', 'r') as f:
    for line in f:

        # проверяем, что в текущую строку можно считать в два значения
        try:
            line = line.strip().split('\t')

            # можно использовать запись (тогда будет ошибка ValueError)
            # lineID, value = line.strip().split('\t')
            lineID = line[0]
            value = line[1]

            totalSum += int(value)

        except IndexError as iError:
            print('Похоже в строке {} один столбец'.format(lineNumber))
            print(iError)
            print('')

        except ValueError as vError:
            print('Значение строки {} не было целым числом'.format(lineNumber))
            print(vError)
            print('')

        except Exception as e:
            print('Внезапная ошибка на строке P{. Вот что известно:'.format(lineNumber))
            print(e)

        lineNumber += 1

print(totalSum)

