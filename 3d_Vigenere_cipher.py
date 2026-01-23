def start(arr, arr2, fkey, skey, mes, a):
    mes2 = []
    fkey2 = []
    skey2 = []

    for i in range(len(mes)):
        mes2.append(arr2.index(mes[i]))

    for i in range(len(skey)):
        skey2.append(arr2.index(skey[i]))

    for i in range(len(fkey)):
        fkey2.append(arr2.index(fkey[i]))

    print(f'fkey2: {fkey2}')
    print(f'skey2: {skey2}')
    print(f'mes2: {mes2}')

    while True:
        if len(mes2) > len(fkey2):
            fkey2 += fkey2
        elif len(mes) < len(fkey2):
            fkey2.pop(-1)
        else:
            break

    while True:
        if len(mes2) > len(skey2):
            skey2 += skey2
        elif len(mes2) < len(skey2):
            skey2.pop(-1)
        else:
            break

    if a == '1':
        mes3 = code(arr, fkey2, skey2, mes2)
    elif a == '2':
        mes3 = encode(arr, fkey2, skey2, mes2)
    elif a == '3':
        mes3 = math_code(fkey2, skey2, mes2)
    elif a == '4':
        mes3 = math_encode(fkey2, skey2, mes2)
    else:
        print('Error:start:if-else-block:1')
        return
    print('---')
    print(f'mes3: {mes3}')

    mes4 = ''
    for x in range(len(mes3)):
        mes4 += arr2[mes3[x]]
    print(mes4)

def code(arr, fkey, skey, mes):
    mes2 = []
    for i in range(len(mes)):
        mes2.append(arr[fkey[i]][skey[i]][mes[i]])
    return mes2


def encode(arr, fkey, skey, mes):

    mes2 = []
    for i in range(len(mes)):
        search_line = arr[fkey[i]][skey[i]]
        try:
            original_idx = search_line.index(mes[i])
            mes2.append(original_idx)
        except ValueError:
            print('Error:encode')
            mes2.append(None)

    return mes2

def math_code(fkey, skey, mes):
    global N

    mes2 = []

    for i in range(len(mes)):
        mis = (fkey[i] + skey[i] + mes[i]) % N
        mes2.append(mis)

    print(f'math_code mes2: {mes2}')
    return mes2

def math_encode(fkey, skey, mes):
    global N
    mes2 = []

    for i in range(len(mes)):
        mis = (mes[i] - fkey[i] - skey[i]) % N
        mes2.append(mis)

    print(f'math_encode mes2: {mes2}')
    return mes2

arr2 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя 1234567890!?,.(){}[]:;№#$-_+=*&^%@"№/|`~<>'
N = len(arr2)
print(f'N: {N}')
arr = [[[(x + y + z) % N for x in range(N)] for y in range(N)] for z in range(N)]

print('---'*10)
print('Внимание! шифровка специфична, и не может взаимодействовать с онлайн шифровщиками Виженера, '
      '\nона сделана настолько криво что сообщения могут быть расшифрованы только подобным кодом'
      '\nв отличии от иных шифровщиков виженера, тут шифруются все, что вы вводите, от пробелов и обычных букв до спецсимволов и чисел'
      f'\nдоступный ряд символов: {arr2}')
print('---'*10)

while True:
    a = input('\nВведите опцию \n[1] зашифровать \n[2] расшифровать \n[3] зашифровать математическим методом \n[4] расшифровать математическим методом \n[0] выход \n:')

    if a == '1':
        fkey = input('введите первый ключ: ').lower().replace('ё', 'е')
        skey = input('введите второй ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно зашифровать: \n').lower().replace('ё', 'е')
        start(arr, arr2, fkey, skey, mes, a)
    elif a == '2':
        fkey = input('введите первый ключ: ').lower().replace('ё', 'е')
        skey = input('введите второй ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно расшифровать: \n').lower().replace('ё', 'е')
        start(arr, arr2, fkey, skey, mes, a)
    elif a == '3':
        fkey = input('введите первый ключ: ').lower().replace('ё', 'е')
        skey = input('введите второй ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно зашифровать: \n').lower().replace('ё', 'е')
        start(arr, arr2, fkey, skey, mes, a)
    elif a == '4':
        fkey = input('введите первый ключ: ').lower().replace('ё', 'е')
        skey = input('введите второй ключ: ').lower().replace('ё', 'е')
        mes = input('введите сообщение которое нужно расшифровать: \n').lower().replace('ё', 'е')
        start(arr, arr2, fkey, skey, mes, a)
    elif a == '0':
        print('выход из программы')
        break
    else:
        print('неверная команда')
