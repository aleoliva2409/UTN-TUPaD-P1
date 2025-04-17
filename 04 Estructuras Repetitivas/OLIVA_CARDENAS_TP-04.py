from random import randrange
from statistics import mean


# EXERCISE 1:
def exercise_1():
    for i in range(0, 101):
        print(i)


# EXERCISE 2:
def exercise_2():
    number = int(input('Ingrese un número: '))
    number_to_string = str(number)
    quantity = 0

    for i in range(len(number_to_string)):
        quantity += 1

    print(f'El número tiene {quantity} dígitos')


# EXERCISE 3:
def exercise_3():
    number_1 = int(input('Ingrese un número: '))
    number_2 = int(input('Ingrese otro número: '))
    total_sum = 0

    for i in range(number_1, number_2):
        if i == number_1:
            continue

        total_sum += i

    print(f'La suma total es: {total_sum}')


# EXERCISE 4:
def exercise_4():
    acc = 0
    number_input = None

    while number_input != 0:
        number_input = int(input('Ingrese un número para sumar: '))
        acc += number_input

    print(f'La suma total de los nros ingresados es: {acc}')


# EXERCISE 5:
def exercise_5():
    random_number = randrange(0, 10)
    tries = 0
    number_input = None
    print('Adivina el número aleatorio')

    while number_input != random_number:
        number_input = int(input('Ingrese un número: '))
        tries += 1

    print(f'Necesitaste {tries} intentos')


# EXERCISE 6:
def exercise_6():
    for i in range(100, -1, -2):
        print(i)


# EXERCISE 7:
def exercise_7():
    number_input = int(input('Ingrese un número: '))
    acc = 0

    for i in range(0, number_input + 1):
        acc += i

    print(f'La suma total es: {acc}')


# EXERCISE 8:
def exercise_8():
    odds = []
    evens = []
    positives = []
    negatives = []

    for i in range(100):
        number_input = int(input('Ingrese un número: '))

        if number_input == 0:
            continue

        if number_input > 0:
            positives.append(number_input)
        else:
            negatives.append(number_input)

        if number_input % 2 == 0:
            evens.append(number_input)
        else:
            odds.append(number_input)

    print(f'Números pares: {evens}')
    print(f'Números impares: {odds}')
    print(f'Números positivos: {positives}')
    print(f'Números negativos: {negatives}')


# EXERCISE 9:
def exercise_9():
    numbers = []
    for i in range(5):
        number_input = int(input('Ingrese un número: '))
        numbers.append(number_input)

    print(f'La media de los números ingresados es: {mean(numbers)}')


# EXERCISE 10:
def exercise_10():
    number_input = int(input('Ingrese un número: '))
    reverse_number = int(str(number_input)[::-1])

    print(f'El número al revés es: {reverse_number}')
