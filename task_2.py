import sys
import random


day_month_dict = {
    1: 'январь 31',
    2: 'февраль 28',
    3: 'март 31',
    4: 'апрель 30',
    5: 'май 31',
    6: 'июнь 30',
    7: 'июль 31',
    8: 'август 31',
    9: 'сентябрь 30',
    10: 'октябрь 31',
    11: 'ноябрь 30',
    12: 'декабрь 31'
}


# Список животных по китайскому календарю с 1970 по 1981 (12 лет - 1 цикл)
china_calendar_dict = {
    1970: 'Год Собаки',
    1971: 'Год Свиньи',
    1972: 'Год Крысы',
    1973: 'Год Быка',
    1974: 'Год Тигра',
    1975: 'Год Кролика',
    1976: 'Год Дракона',
    1977: 'Год Змеи',
    1978: 'Год Лошади',
    1979: 'Год Овцы',
    1980: 'Год Обезьяны',
    1981: 'Год Петуха'
}


# Дни недели начиная с января 1970 года (ключи словаря - числа месяца)
day_of_week_dict = {
    1: 'Четверг',
    2: 'Пятница',
    3: 'Суббота',
    4: 'Воскресенье',
    5: 'Понедельник',
    6: 'Вторник',
    7: 'Среда'
}


# True - високосный год; False - оьычный год
def leap_year_check(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


# Если год високосный перезаписываем словарь с месяцами и днями в месяцах
def leap_year_fixing(year):
    if leap_year_check(year):
        day_month_dict[2] = 'февраль 29'


# Возвращает номер квартала в году
def quarter_number(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4


# Возвращает номер дня в году
def days_count_since_year_beginning(day, month):
    days = 0
    for i in range(1, month):
        days += int(day_month_dict[i].split(sep=' ')[1])
    return days + day


# Возвращает наименование года по китайскому календарю
def year_animal(year):
    for i in range(1970, 1982):
        if (year - i) % 12 == 0:
            return china_calendar_dict[i]


# Возвращает количество дней с 01.01.1970
def days_count_since_period_beginning(day, month, year):
    year_days = 0
    for i in range(1970, year):
        if leap_year_check(i):
            year_days += 366
        else:
            year_days += 365
    return days_count_since_year_beginning(day, month) + year_days


# Возвращает день недели, принимает количество дней с 01.01.1970
def day_of_week(days):
    for i in range(1, 8):
        if (days - i) % 7 == 0:
            return day_of_week_dict[i]


if len(sys.argv) == 1:
    # Список из дня, месяца, года, введённый пользователем
    a = input('Введите дату в формате dd.mm.yyyy: ').replace(' ', '').split(sep='.')
elif len(sys.argv) == 2:
    random_y = random.randint(1970, 2022)
    leap_year_fixing(random_y)
    random_m = random.randint(1, 12)
    random_d = random.randint(1, int(day_month_dict[random_m].split(sep=' ')[1]))
    if sys.argv[1] == '-r':
        a = [random_d, random_m, random_y]


while len(a) != 3:
    a = input('Некорректный ввод. Введите дату в формате dd.mm.yyyy: '). \
        replace(' ', '').split(sep='.')


# Проверка на корректность даты
while int(a[2]) < 1970:
    a = input('Некорректный ввод. Значение раннее 01.01.1970. Введите дату позднее 01.01.1970 в формате dd.mm.yyyy: ')\
        .replace(' ', '').split(sep='.')
else:
    while int(a[1]) < 1 or int(a[1]) > 12:
        a = input('Некорректный ввод. Некоректное значение месяца. Введите дату в формате dd.mm.yyyy: '). \
            replace(' ', '').split(sep='.')
    else:
        while int(a[0]) > int(day_month_dict[int(a[1])].split(sep=' ')[1]):
            a = input('Некорректный ввод. Некоректное значение дня. Введите дату в формате dd.mm.yyyy: '). \
                replace(' ', '').split(sep='.')
        else:
            d, m, y = int(a[0]), int(a[1]), int(a[2])

            leap_year_fixing(y)

            if len(str(d)) == 1:
                dd = '0' + str(d)
            else:
                dd = d

            if len(str(m)) == 1:
                mm = '0' + str(m)
            else:
                mm = m

            if leap_year_check(y):
                leap_year_desc = 'Високосный год'
            else:
                leap_year_desc = 'Обычный год'


# Итоговый вывод
            print(dd, '.', mm, '.', y, ' - ', leap_year_desc, sep='')
            print(y, ' - ', year_animal(y), sep='')
            print(quarter_number(m), '-й квартал', sep='')
            print(mm, ' - ', day_month_dict[m].split(sep=' ')[0], sep='')
            print(dd, '-й день', sep='')
            print(days_count_since_year_beginning(d, m), 'дней прошло с начала года')
            print(day_of_week(days_count_since_period_beginning(d, m, y)))
