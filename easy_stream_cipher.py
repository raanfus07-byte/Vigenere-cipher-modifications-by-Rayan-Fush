def start(mes, a):
    global arr

    mes2 = []
    for i in range(len(mes)):
        if mes[i] in arr:
            mes2.append(arr.index(mes[i]))
        else:
            print(f'символа {mes[i]} нет, он заменен на пробел, раздел 0')
            mes2.append(32)

    print(mes2)

    if a == '1':
        pass
        code_stream_cipher(mes2)
    elif a == '2':
        encode_stream_cipher(mes2)
    else:
        print('Error:start:if-else-block:1') # защита от неверных команд
        return


def code_stream_cipher(mes):
    global arr
    mes2 = []
    for i in range(len(mes)):
        if mes[i] % 2 == 0:
            mes2.append((mes[i] + i) % len(arr))
        else:
            mes2.append((mes[i] - i) % len(arr))

    print(mes2)

    mes3 = ''
    for x in range(len(mes2)):
        mes3 += arr[mes2[x]]
    print(mes3)

def encode_stream_cipher(mes):
    global arr
    mes2 = []
    for i in range(len(mes)):
        if ((mes[i] - i) % len(arr)) % 2 == 0:
            mes2.append((mes[i] - i) % len(arr))
        else:
            mes2.append((mes[i] + i) % len(arr))

    print(mes2)

    mes3 = ''
    for x in range(len(mes2)):
        mes3 += arr[mes2[x]]
    print(mes3)

arr = 'абвгдежзийклмнопрстуфхцчшщъыьэюя 1234567890!?,.(){}[]:;№#$-—_+=*&^%@"№/|`~<>«»'
print('---'*10)
print('Поточный шифр'
      f'\nдоступный ряд символов(остальные символы изменяются на пробел автоматически): {arr}')
print('---'*10)
while True:
    a = input('\nВведите опцию \n[1] зашифровать \n[2] расшифровать \n[0] выход \n:')

    if a == '1':
        mes = input('введите сообщение что нужно зашифровать \n:')
        start(mes, a)
    elif a == '2':
        mes = input('введите сообщение что нужно расшифровать \n:')
        start(mes, a)
    else:
        print('выход из программы')
        break