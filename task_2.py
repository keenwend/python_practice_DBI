# 1 - високосный год; 0 - оьычный год
def leap_year_check(year):
    if year % 4 == 0 and year % 100 != 0:
        return 1
    elif year % 100 == 0 and year % 400 == 0:
        return 1
    else:
        return 0


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


# Список из дня, месяца, года, введённый пользователем
a = input('Введите дату в формате dd.mm.yyyy: ').replace(' ', '').split(sep='.')


d, m, y = int(a[0]), int(a[1]), int(a[2])


if leap_year_check(y) == 1:
    day_month_dict[2] = 'февраль 29'


for i in range(1, 13):
    print(
        int(day_month_dict[i].split(sep=' ')[1])
    )
