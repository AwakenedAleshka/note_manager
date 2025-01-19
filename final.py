username = (input("Введите Ваше имя: "))
username_safe = username
title = ["Основные темы",
        "Персонажи",
        "Рекомендации для чтения"
        ]
title.append(input("Введите 1 название заметки: "))
title.append(input("Введите 2 название заметки: "))
title.append(input("Введите 3 название заметки: "))
title_safe = title


content = (input("Введите текст Вашей заметки: "))
content_safe = content
# выбор статуса на русском и английском (параметр от 0 до 7)
status = int(input("Введите статус Вашей заметки от 0 до 7, где \
                \n 0 - \033[31mЧерновик\033[0m\
                \n 1 - \033[31mDraft\033[0m\
                \n 2 - \033[31mАктивна\033[0m\
                \n 3 - \033[31mActive\033[0m\
                \n 4 - \033[31mУдаленна\033[0m\
                \n 5 - \033[31mDeleted\033[0m\
                \n 6 - \033[31mПросроченна\033[0m\
                \n 7 - \033[31mOutdated\033[0m\
                \nВнимание!!! Только одна цифра - Ваш ввод: "))
status_info = ("Черновик", "Draft", "Активна", "Active", \
        "Удаленна", "Deleted", "Просроченна", "Outdated")
status_safe =  status
created_date = (input("Введите дату создания в формате \"ДД-ММ-ГГГГ\": "))
created_date_safe = created_date
issue_date = (input("Введите дату окончания в формате \"ДД-ММ-ГГГГ\": "))
issue_date_safe = issue_date

note = []
note.append(username_safe)
note.append(title_safe)
note.append(content_safe)
note.append(status_safe)
note.append(created_date_safe)
note.append(issue_date_safe)

note_default = [
    "Имя пользователя",
    ["Заголовок1", "Заголовок2", "Заголовок3",\
     "Заголовок4", "Заголовок5", "Заголовок6"],
    "Содержание заметки",
    "Статус",
    "Дата создания",
    "Дата изменения"
]



# Приколюшка с замедленным выводом текста
import time
print()
congratulations = "Спасибо за предоставнные данные:)" \
                  "\n\033[31mВаша заметка успешно создана!\033[0m"

for char in congratulations:
    print(char, end='', flush=True)
    time.sleep(0.08)

print('\nВариант 1')

print(note_default[0],"\033[31m%s\033[0m" % note[0])
print(note_default[1],"\n" "\033[31m%s\033[0m" % note[1])
print(note_default[2],"\033[31m%s\033[0m" % note[2])
print(note_default[3],"\033[31m%s\033[0m" % status_info[note[3]])
print(note_default[4],"\033[31m%s\033[0m" % note[4])
print(note_default[5],"\033[31m%s\033[0m" % note[5])

print('\nВариант 2')

# вывод вариант2
print("\n")
print("Пользователь: \033[31m%s\033[0m" %username_safe)
print("\nЗаголовки заметки из готового списка:\n")
print("1. \033[31m%s\033[0m" %title_safe[0])
print("2. \033[31m%s\033[0m" %title_safe[1])
print("3. \033[31m%s\033[0m" %title_safe[2])
print("\nДобавленные Вами заголовоки заметки:\n")
print("4. \033[31m%s\033[0m" %title_safe[3])
print("5. \033[31m%s\033[0m" %title_safe[4])
print("6. \033[31m%s\033[0m" %title_safe[5])
# вывод заголовков вариант2
print('\nЗаголоки еще вариант с выбором из списка')
print(note_default[1][0]," - \033[31m%s\033[0m" %note[1][0])
print(note_default[1][1]," - \033[31m%s\033[0m" %note[1][1])
print(note_default[1][2]," - \033[31m%s\033[0m" %note[1][2])
print(note_default[1][3]," - \033[31m%s\033[0m" %note[1][3])
print(note_default[1][4]," - \033[31m%s\033[0m" %note[1][4])
print(note_default[1][5]," - \033[31m%s\033[0m" %note[1][5])
print ("Текст земетки: \033[31m%s\033[0m" %content_safe)
print("Статус заметки: \033[31m%s\033[0m" %status_info[status_safe])
print("Дата создания: \033[31m%s\033[0m" %created_date_safe)
print("Дата окончания: \033[31m%s\033[0m" %issue_date_safe)


