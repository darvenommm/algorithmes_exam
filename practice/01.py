# Даны два числа a и b в десятичной системе счисления и основание
# некоторой системы счисления c. Найдите сумму этих чисел в системе
# счисления c. Результат представить в виде строки.

def convert(number: int, base: int) -> str:
    if base < 1:
        raise ValueError('The base has to be more 0!')

    is_negative: bool = number < 0
    number = abs(number)

    result: str = ''

    while True:
        result += str(number % base)
        number = number // base

        if number < base:
            return ('-' if is_negative else '') + str(number) + result

def main(first_number: int, second_number: int, base: int) -> str:
    sum_numbers: int = first_number + second_number

    return convert(sum_numbers, base)


# print(main(12, 4, 4))
