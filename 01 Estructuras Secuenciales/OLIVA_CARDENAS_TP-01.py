import math


# EXERCISE 1:
def exercise_1():
    print('Hola Mundo!')


# EXERCISE 2:
def exercise_2():
    name = input('Ingrese su nombre: ')
    print(f'Hola {name}!')


# EXERCISE 3:
def exercise_3():
    print('Ingrese los siguentes datos')
    name = input('Nombre: ')
    last_name = input('Apellido: ')
    age = input('Edad: ')
    place_of_residence = input('Lugar de residencia: ')

    print(f'Soy {name} {last_name}, tengo {age} años y vivo en {place_of_residence}')


# EXERCISE 4:
def exercise_4():
    radio = int(input('Ingrese el radio de un círculo: '))

    area = math.pi * radio ** 2
    perimeter = 2 * math.pi * radio

    print(f'El área es {area}')
    print(f'El perímetro es {perimeter}')


# EXERCISE 5:
def exercise_5():
    time_in_seconds = int(input('Ingrese una cantidad de segundos: '))
    time_in_hours = time_in_seconds / 3600

    print(f'Los segundos ingresados equivalen a {time_in_hours} horas')


# EXERCISE 6:
def exercise_6():
    number = int(input('Ingrese un número para generar la tabla: '))

    print(f'{number} x 1 = {number * 1}')
    print(f'{number} x 2 = {number * 2}')
    print(f'{number} x 3 = {number * 3}')
    print(f'{number} x 4 = {number * 4}')
    print(f'{number} x 5 = {number * 5}')
    print(f'{number} x 6 = {number * 6}')
    print(f'{number} x 7 = {number * 7}')
    print(f'{number} x 8 = {number * 8}')
    print(f'{number} x 9 = {number * 9}')
    print(f'{number} x 10 = {number * 10}')


# EXERCISE 7:
def exercise_7():
    print('Ingrese dos números distintos de cero')
    num_1 = int(input('Primer número: '))
    num_2 = int(input('Segundo número: '))

    print('Suma')
    print(f'{num_1} + {num_2} = {num_1 + num_2}')
    print('Resta')
    print(f'{num_1} - {num_2} = {num_1 - num_2}')
    print('Multiplicación')
    print(f'{num_1} * {num_2} = {num_1 * num_2}')
    print('División')
    print(f'{num_1} / {num_2} = {num_1 / num_2}')


# EXERCISE 8:
def exercise_8():
    print('Ingrese los siguentes datos para calcular su IMC')
    height = float(input('Altura en metros: '))
    weight = float(input('Peso en Kg: '))

    imc = weight / height ** 2

    print(f'Su IMC es de {imc}')


# EXERCISE 9:
def exercise_9():
    print('Ingrese la temperatura que desea convertir')
    temp_in_celsius = int(input('Grados celsius: '))

    temp_in_fahrenheit = (9 / 5 * temp_in_celsius) + 32

    print(f'La temperatura en Fahrenheit es de {temp_in_fahrenheit}')


# EXERCISE 10:
def exercise_10():
    print('Ingrese tres números')
    num_1 = int(input('Primer número: '))
    num_2 = int(input('Segundo número: '))
    num_3 = int(input('Tercer número: '))

    average = (num_1 + num_2 + num_3) / 3

    print(f'El promedio de los tres números ingresados es {average}')
