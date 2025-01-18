# импортируем дату
from datetime import date

#  создаем 6 переменных:
username = (input("Введите Ваше имя: "))
title = (input("Введите название заметки: "))
content = "Текст, я тут заполнил за Вас, \n\
                потому что Вы так или иначе \n\
                набирёте что то вроде \"фывапролджэ\" "
# выбор статуса на русском и английском (параметр от 0 до 7)
status = ("Черновик", "Draft", "Активна", "Active", \
        "Удаленна", "Deleted", "Просроченна", "Outdated")
# переменная для получения текущей даты
created_date = date.today()
created_date_format = (created_date.strftime("%d-%m-%Y"))
# переменная даты истечения срока
issue_date = date(2025,1,31)
issue_date_format = issue_date.strftime("%d-%m-%Y")

# вывод
print("Пользователь: \033[31m%s\033[0m" %username)
print("Заголовок заметки: \033[31m%s\033[0m" %title)
print ("Текст земетки: \033[31m%s\033[0m" %content)
print("Статус заметки: \033[31m%s\033[0m" %status[0])
print("Дата создания: \033[31m%s\033[0m" %created_date_format)
print("Дата истечения: \033[31m%s\033[0m" %issue_date_format)