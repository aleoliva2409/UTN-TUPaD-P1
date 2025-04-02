from random import randint
from statistics import mode, median, mean


# EXERCISE 1:
def exercise_1():
    age = int(input('Ingrese su edad: '))

    if age >= 18:
        print('Es mayor de edad')


# EXERCISE 2:
def exercise_2():
    score = int(input('Ingrese la nota: '))

    if score >= 6:
        print('Aprobado')
    else:
        print('Desaprobado')


# EXERCISE 3:
def exercise_3():
    number = int(input('Ingrese un número: '))

    if number % 2 == 0:
        print('Ha ingresado un número par')
    else:
        print('Por favor, ingrese un número par')


# EXERCISE 4:
def exercise_4():
    age = int(input('Ingrese su edad: '))

    if 1 <= age < 12:
        print('Niño/a')
    elif 12 <= age < 18:
        print('Adolescente')
    elif 18 <= age < 30:
        print('Adulto/a joven')
    elif age >= 30:
        print('Adulto/a')
    else:
        print('La edad no es válida')


# EXERCISE 5:
def exercise_5():
    password = input('Ingrese la contraseña: ')

    if 8 <= len(password) <= 14:
        print('Ha ingresado una contraseña correcta')
    else:
        print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')


# EXERCISE 6:
def exercise_6():
    random_numbers = [randint(1, 100) for i in range(50)]
    mean_number = mean(random_numbers)
    median_number = median(random_numbers)
    mode_number = mode(random_numbers)

    if mean_number > median_number > mode_number:
        print('Sesgo positivo o a la derecha')
    elif mean_number < median_number < mode_number:
        print('Sesgo negativo o a la izquierda')
    elif mean_number == median_number == mode_number:
        print('Sin sesgo')
    else:
        print('No cumple ninguna condición')


# EXERCISE 7:
def exercise_7():
    phrase = input('Ingrese una frase o palabra: ')
    last_character = phrase[len(phrase) - 1].lower()

    if last_character == 'a' or last_character == 'e' or last_character == 'i' or last_character == 'o' or last_character == 'u':
        print(f'{phrase}!')
    else:
        print(phrase)


# EXERCISE 8:
def exercise_8():
    name = input('Ingrese tu nombre: ')
    print('Elegí una opción para capitalizar tu nombre')
    print('1. En mayúsculas')
    print('2. En minúsculas')
    print('3. Primera letra en mayúscula')
    option = int(input('Opción seleccionada: '))

    if option == 1:
        print(name.upper())
    elif option == 2:
        print(name.lower())
    elif option == 3:
        print(name.title())
    else:
        print('La opción no es válida')


# EXERCISE 9:
def exercise_9():
    size = int(input('Ingrese magnitud del terremoto: '))

    if size < 3:
        print('Muy leve')
    elif size == 3:
        print('Leve')
    elif size == 4:
        print('Moderado')
    elif size == 5:
        print('Fuerte')
    elif size == 6:
        print('Muy Fuerte')
    elif size >= 7:
        print('Extremo')
    else:
        print('La magnitud no es válida')


# EXERCISE 10:
def exercise_10():
    hemisphere = input('Indique en que hemisferio se encuentra(N/S): ')
    month_selected = int(input('Indique el nro del mes actual: '))
    day_selected = int(input('Indique el día actual: '))

    if hemisphere != 'N' and hemisphere != 'S':
        print('Ingrese un "N" o "S"')
        return

    if month_selected == 1 or month_selected == 2:
        if hemisphere == 'N':
            print('Invierno')
        else:
            print('Verano')

    if month_selected == 4 or month_selected == 5:
        if hemisphere == 'N':
            print('Primavera')
        else:
            print('Otoño')

    if month_selected == 7 or month_selected == 8:
        if hemisphere == 'N':
            print('Verano')
        else:
            print('Invierno')

    if month_selected == 10 or month_selected == 11:
        if hemisphere == 'N':
            print('Otoño')
        else:
            print('Primavera')

    if month_selected == 12:
        if 1 <= day_selected <= 20:
            if hemisphere == 'N':
                print('Otoño')
            else:
                print('Primavera')
        elif 21 <= day_selected <= 31:
            if hemisphere == 'N':
                print('Invierno')
            else:
                print('Verano')

    if month_selected == 3:
        if 1 <= day_selected <= 20:
            if hemisphere == 'N':
                print('Invierno')
            else:
                print('Verano')
        elif 21 <= day_selected <= 31:
            if hemisphere == 'N':
                print('Primavera')
            else:
                print('Otoño')

    if month_selected == 6:
        if 1 <= day_selected <= 20:
            if hemisphere == 'N':
                print('Primavera')
            else:
                print('Otoño')
        elif 21 <= day_selected <= 30:
            if hemisphere == 'N':
                print('Verano')
            else:
                print('Invierno')

    if month_selected == 9:
        if 1 <= day_selected <= 20:
            if hemisphere == 'N':
                print('Verano')
            else:
                print('Invierno')
        elif 21 <= day_selected <= 30:
            if hemisphere == 'N':
                print('Otoño')
            else:
                print('Primavera')
