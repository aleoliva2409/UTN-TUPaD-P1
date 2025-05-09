from statistics import mean
from math import pi


# EXERCISE 1:
def exercise_1():
    imprimir_hola_mundo()


# EXERCISE 2:
def exercise_2():
    name = input('Ingrese un nombre: ')
    print(saludar_usuario(name))


# EXERCISE 3:
def exercise_3():
    name = input('Nombre: ')
    last_name = input('Apellido: ')
    age = int(input('Edad: '))
    place_of_residence = input('Lugar de residencia: ')
    print(informacion_personal(name, last_name, age, place_of_residence))


# EXERCISE 4:
def exercise_4():
    radio = int(input('Ingrese el radio: '))

    area = calcular_area_circulo(radio)
    perimeter = calcular_perimetro_circulo(radio)

    print(f'El área es: {area}')
    print(f'El perímetro es: {perimeter}')


# EXERCISE 5:
def exercise_5():
    seconds = int(input('Ingrese los segundos a convertir: '))

    print(f'Los segundos son {segundos_a_horas(seconds)} en horas')


# EXERCISE 6:
def exercise_6():
    number_input = int(input('Ingrese un número para generar la tabla: '))

    tabla_multiplicar(number_input)


# EXERCISE 7:
def exercise_7():
    number_1 = int(input('Ingrese un número: '))
    number_2 = int(input('Ingrese otro número: '))

    print(operaciones_basicas(number_1, number_2))


# EXERCISE 8:
def exercise_8():
    print('Ingrese los siguentes datos para calcular su IMC')
    height = float(input('Altura en metros: '))
    weight = float(input('Peso en Kg: '))

    print(f'Su IMC es de {calcular_imc(height, weight)}')


# EXERCISE 9:
def exercise_9():
    print('Ingrese la temperatura que desea convertir')
    temp_in_celsius = int(input('Grados celsius: '))

    print(f'La temperatura en Fahrenheit es de {celsius_a_fahrenheit(temp_in_celsius)}')


# EXERCISE 10:
def exercise_10():
    print('Ingrese tres números')
    num_1 = int(input('Primer número: '))
    num_2 = int(input('Segundo número: '))
    num_3 = int(input('Tercer número: '))

    print(f'El promedio de los tres números ingresados es {calcular_promedio(num_1, num_2, num_3)}')


# FUNCTIONS
def imprimir_hola_mundo():
    print('Hola Mundo!')


def saludar_usuario(name):
    return f'Hola {name}!'


def informacion_personal(name, last_name, age, residence):
    return f'Soy {name} {last_name}, tengo {age} años y vivo en {residence}'


def calcular_area_circulo(radio):
    return pi * radio ** 2


def calcular_perimetro_circulo(radio):
    return 2 * pi * radio


def segundos_a_horas(seconds):
    return (seconds / 60) / 60


def tabla_multiplicar(number):
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


def operaciones_basicas(a, b):
    result_sum = a + b
    result_sub = a - b
    result_multiply = a * b
    result_division = a / b
    results = (
        f'Suma: {result_sum}', f'Resta: {result_sub}', f'Multiplicación: {result_multiply}',
        f'División: {result_division}')

    return results


def calcular_imc(height, weight):
    return round(weight / height ** 2, 2)


def celsius_a_fahrenheit(celsius):
    return (9 / 5 * celsius) + 32


def calcular_promedio(a, b, c):
    return mean([a, b, c])
