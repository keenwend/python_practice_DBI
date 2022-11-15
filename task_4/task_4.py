# import random
#
#
# a = random.randint(1, 100)
#
#
# b = int(input('Угадайте загаданное программой число: '))
#
# while a != b:
#     if a < b:
#         print('left')
#         b = int(input('Угадайте загаданное программой число: '))
#     elif a > b:
#         print('right')
#         b = int(input('Угадайте загаданное программой число: '))
# else:
#     print('nice')


test_dict = {0: 1, 1: 2, 2: 3}
k = list(test_dict.keys())
print(k)
print(type(k))
print(0 == k[0])