from sys import argv
from random import randint


def main():
    welcome()
    numbers = get_numbers()
    winning_number = get_randon_number(numbers[0], numbers[1])
    game(winning_number)


def welcome():
    print('welcome to the guessing game!')


def get_numbers():
    try:
        num1 = int(argv[1])
        num2 = int(argv[2])
        return [num1, num2]
    except ValueError:
        print('please be sure to use only numbers')


def get_randon_number(num1, num2):
    return randint(num1, num2)


def game(winning_num):
    print(winning_num)
    while True:
        try:
            users_guess = int(input('Take a guess at which number im thinking about. :'))
            if users_guess == winning_num:
                print('congrats! thats the winning number!!')
                break
            else:
                print('No no no, try again')
        except ValueError:
            print('Its numbers game not a letters one. Provide a number: ')


if __name__ == '__main__':
    main()
