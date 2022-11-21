import random
import os
import logging
from datetime import datetime


if os.path.exists('Logs') and not os.path.isfile('Logs'):
    a = 0  # placeholder
else:
    os.mkdir('Logs')


os.chdir('Logs')


file_name = os.path.basename(__file__).split('.')[0]


log_name = file_name + '_' + datetime.now().strftime('%d-%m-%Y_%H-%M-%S') + '.log'


logging.basicConfig(filename=log_name, level=logging.INFO)


logging.info('Game started at' + ' ' + datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))


def equal_check(rand, user):
    if abs(rand - user) <= 5:
        return 'Very hot'
    elif abs(rand - user) <= 10:
        return 'Hot'
    elif abs(rand - user) <= 20:
        return 'Warm'
    elif abs(rand - user) <= 50:
        return 'Cold'
    elif abs(rand - user) <= 100:
        return 'Very cold'


def direction_check(rand, user_list):
    if len(user_list) == 1:
        return ''
    elif len(user_list) > 1:
        if abs(rand - user_list[len(user_list) - 1]) > abs(rand - user_list[len(user_list) - 2]):
            return 'Wrong direction.'
        elif abs(rand - user_list[len(user_list) - 1]) < abs(rand - user_list[len(user_list) - 2]):
            return 'Right direction.'


rand_num = random.randint(1, 100)


user_num = int(input('Угадайте загаданное программой число: '))


logging.info('users values: ' + str(user_num))


user_num_list = [user_num]


while rand_num != user_num:
    print(equal_check(rand_num, user_num), '. ', direction_check(rand_num, user_num_list), sep='')
    user_num = int(input('Try again: '))
    user_num_list.append(user_num)
    logging.info('users values: ' + str(user_num))
else:
    print('Nice.')
    logging.info('Game finished at' + ' ' + datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
    logging.info('users tries: ' + str(len(user_num_list)))

