binarios = [0, 1]


def gate_not(input_1):
    return 1 if input_1 == 0 else 0


def gate_and(input_1, input_2):
    return input_1 * input_2


def gate_or(input_1, input_2):
    result_suma = input_1 + input_2
    return 1 if result_suma == 2 else result_suma


def gate_xor(input_1, input_2):
    return 0 if input_1 == input_2 else 1


def main():
    input_1 = None
    input_2 = None

    while not (input_1 in binarios and input_2 in binarios):
        if not (input_1 is None and input_2 is None):
            print('ERROR: Las entradas deberian ser 0 y 1')

        input_1 = int(input('Entrada 1: '))
        input_2 = int(input('Entrada 2: '))

    print('')
    print('Salida NOT entrada 1:', gate_not(input_1))
    print('Salida NOT entrada 2:', gate_not(input_2))
    print('')
    print('Salida AND:', gate_and(input_1, input_2))
    print('Salida NAND:', gate_not(gate_and(input_1, input_2)))
    print('')
    print('Salida OR:', gate_or(input_1, input_2))
    print('Salida NOR:', gate_not(gate_or(input_1, input_2)))
    print('Salida XOR:', gate_xor(input_1, input_2))


main()
