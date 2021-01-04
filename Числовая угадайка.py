from random import *


def game_on():
    n = int(input('Определите максимальную границу чисел '))

    n_comp = randint(1, n)
    print('Добро пожаловать в числовую угадайку')

    def is_valid(s):
        return s.isdigit() and 1 <= int(s) <= n

    def compare_numbers(comp, user):
        if user < comp:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user > comp:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            nonlocal Flag
            Flag = False

    Flag = True
    count = 0
    while Flag:
        string = input(f'Введите число от 1 до {n}.')
        if is_valid(string):
            n_user = int(string)
            compare_numbers(n_comp, n_user)
            count += 1
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')

    print(f'Вы угадали с {count} попытки')
    answer = input('Сыграем еще раз? "д" - да, "н" - нет')
    if answer == 'д':
        return game_on()
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


game_on()
