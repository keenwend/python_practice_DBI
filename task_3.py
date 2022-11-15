def fib_recursion(n):
    if n > 2:
        return fib_recursion(n - 1) + fib_recursion(n - 2)
    else:
        return 1


def factorial_recursion(n):
    if n >= 2:
        return n * factorial_recursion(n - 1)
    else:
        return 1


def fib(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


a = int(input('Введите номер числа Фибоначчи, которое хотите получить. '
              'Первые два значения (1 и 1) не учитываются при расчёте: '))


if a >= 1:
    for i in range(3, a + 3):
        print(i - 2, 'iteration:', fib_recursion(i))
    print('Overall ', a, ' iterations. Factorial of ', a, '!', ' = ', factorial_recursion(a), sep='')
else:
    print('Error.')


# a1 = 1
# a2 = 1
# a3 = 2
# a4 = 3
# a5 = 5
# a6 = 8
# a7 = 13