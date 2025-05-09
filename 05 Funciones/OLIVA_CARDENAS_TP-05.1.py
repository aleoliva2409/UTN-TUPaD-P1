# EXERCISE 1:
def exercise_1():
    numbers = list(range(4, 100, 4))

    print(f'Lista: {numbers}')


# EXERCISE 2:
def exercise_2():
    my_list = ['string', 99, True]
    
    print(f'El penúltimo dato de la lista es: {my_list[-2]}')


# EXERCISE 3:
def exercise_3():
    my_list = []

    my_list.append('Alejandro')
    my_list.append('Facundo')
    my_list.append('Roberto')

    print(f'Lista: {my_list}')


# EXERCISE 4:
def exercise_4():
    animals = ["perro", "gato", "conejo", "pez"]

    animals[1] = 'loro'
    animals[-1] = 'oso'

    print(f'Animales: {animals}')


# EXERCISE 5:
## Se elimina el numero mas alto la lista "numeros" y se imprime por pantalla


# EXERCISE 6:
def exercise_6():
    numbers = list(range(10, 30, 5))

    print(f'Primer nro: {numbers[0]}')
    print(f'Segundo nro: {numbers[1]}')


# EXERCISE 7:
def exercise_7():
    cars = ["sedan", "polo", "suran", "gol"]

    cars[1] = 'BMW'
    cars[2] = 'Audi'

    print(f'Autos: {cars}')


# EXERCISE 8:
def exercise_8():
    dobles = []

    dobles.append(10)
    dobles.append(20)
    dobles.append(30)

    print(f'Lista: {dobles}')


# EXERCISE 9:
def exercise_9():
    buys = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

    buys[2].append('jugo')
    buys[1][1] = 'tallarines'
    buys[0].remove('pan')

    print(f'Lista: {buys}')


# EXERCISE 10:
def exercise_10():
    list_nested = []

    list_nested.append(15)
    list_nested.append(True)
    list_nested.append([25.5, 57.9, 30.6])
    list_nested.append(False)

    print(f'Lista: {list_nested}')
