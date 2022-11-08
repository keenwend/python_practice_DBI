a = input('Введите свой рост, вес и возраст через запятую: ').replace(' ', '').split(sep=',')

try:
    float(a[0])
    float(a[1])
    float(a[2])
except ValueError:
    print('Input text, please enter the numbers')
else:
    if len(a) > 3:
        print('Please enter only 3 numbers')
    elif len(a) < 3:
        print('Please enter ALL needed numbers')
    else:
        height, weight, age = float(a[0]), float(a[1]), float(a[2])


if height <= 0 or weight <= 0 or age <= 0:
    print('Negative values')

if height > 5:
    height = height / 100

def imt(rost,ves):
    return ves / (rost ** 2)

print(imt(height, weight))


