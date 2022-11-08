a = input('Введите свой рост, вес и возраст через запятую: ').replace(' ', '').split(sep=',')

try:
    float(a[0])
    float(a[1])
    float(a[2])
except ValueError:
    print('Введены текстовые значения. Введите цифровые значения.')
else:
    if len(a) > 3:
        print('Введите только три числа')
    elif len(a) < 3:
        print('Введите все необходимые числа')
    else:
        height, weight, age = float(a[0]), float(a[1]), float(a[2])


if height <= 0 or weight <= 0 or age <= 0:
    print('Введены отрицательные значения')

if height > 5:
    height = height / 100


def imt_calc(x, y):
    return round((y / (x ** 2)), 2)


imt_desc_dict = {
    1: 'Выраженный дефицит массы тела',
    2: 'Недостаточная (дефицит) масса тела',
    3: 'Норма',
    4: 'Избыточная масса тела (предожирение)',
    5: 'Ожирение первой степени',
    6: 'Ожирение второй степени',
    7: 'Ожирение третьей степени (морбидное)'
}


age_desc_dict = {
    1: 'Младенец',
    2: 'Ребенок',
    3: 'Подросток',
    4: 'Взрослый',
    5: 'Пожилой'
}


def imt_desc(x):
    i = 0
    if x <= 16:
        i = 1
    elif 16 < x <= 18.5:
        i = 2
    elif 18.5 < x <= 25:
        i = 3
    elif 25 < x <= 30:
        i = 4
    elif 30 < x <= 35:
        i = 5
    elif 35 < x <= 40:
        i = 6
    elif x > 40:
        i = 7
    return imt_desc_dict[i]


def age_category(x):
    i = 0
    if x <= 1:
        i = 1
    elif 1 < x <= 10:
        i = 2
    elif 10 < x <= 18:
        i = 3
    elif 18 < x <= 60:
        i = 4
    elif x > 60:
        i = 5
    return age_desc_dict[i]


print(
    'Ваш ИМТ - ', imt_calc(height, weight), ' (', imt_desc(imt_calc(height, weight)), ')', '\n',
    'Ваша возрастная категория - ', age_category(age), sep=''
)


