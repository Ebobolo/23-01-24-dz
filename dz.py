def texst():
    ex1 = "“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.\n\t\t\t\t\t”Bill Gates"

    print(ex1)
texst()
#№2
def display_even_numbers(start, end):
    """
    Функция отображает все четные числа между двумя числами

    Аргументы:
    start {int} -- начальное число
    end {int} -- конечное число
    """
    # Если начальное число больше конечного, меняем их местами
    if start > end:
        start, end = end, start

    # Отображаем все четные числа между ними
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)


# Пример использования функции
display_even_numbers(10, 20)

#№3
def draw_square(side_length, symbol, filled=True):
    """
    Функция отображает пустой или заполненный квадрат из некоторого символа

    Аргументы:
    side_length {int} -- длина стороны квадрата
    symbol {str} -- символ, которым заполняется квадрат
    filled {bool} -- True, если квадрат заполненный, False, если пустой (по умолчанию: True)
    """
    # Если квадрат пустой, то заполняем его пробелами
    if not filled:
        symbol = ' '

    # Отображаем квадрат из символов
    for _ in range(side_length):
        print(symbol * side_length)


# Пример использования функции
draw_square(5, '*', filled=True)
draw_square(0, '*', filled=False)

#№4

def min_of_five(a, b, c, d, e):
    """
    Функция возвращает минимальное значение из пяти чисел
    """
    # Сравниваем числа и возвращаем минимальное значение
    return min(a, b, c, d, e)

# Пример использования функции
result = min_of_five(10, 5, 7, 1, 2)
print(f"Минимальное значение: {result}")

#№5

def product_of_range(lower, upper):
    """
    Функция возвращает произведение чисел в указанном диапазоне.
    """
    # Поменяем местами границы диапазона, если это необходимо
    if lower > upper:
        lower, upper = upper, lower

    # Инициализируем переменную для хранения произведения чисел
    product = 1

    # Перебираем числа в диапазоне и обновляем значение переменной product
    for num in range(lower, upper + 1):
        product *= num

    # Возвращаем произведение чисел
    return product

# Пример использования функции
result = product_of_range(5, 10)
print(f"Произведение чисел: {result}")

#№6

def count_digits(number):
    """
    Функция считает количество цифр в числе.
    """
    # Переводим число в строку и считаем количество символов в строке
    count = len(str(number))

    # Возвращаем количество цифр
    return count

# Пример использования функции
result = count_digits(3456)
print(f"Количество цифр: {result}")

#№7

def is_palindrome(number):
    """
    Функция проверяет является ли число палиндромом.
    """
    # Переводим число в строку и удаляем знак минуса, если он есть
    str_number = str(number).replace('-', '')

    # Проверяем, равны ли строка числа и её обратная
    is_palindrome = str_number == str_number[::-1]

    # Возвращаем результат проверки
    return is_palindrome

# Пример использования функции
result = is_palindrome(123321)

print(f"Является ли число палиндромом: {result}")
def print_primes(number):
    """
    Функция выводит в консоль все простые числа, меньшие или равные передаваемому в функцию числу.
    """
    # Проверяем, является ли число меньше 2
    if number < 2:
        print("Введите число, большее или равное 2")
        return

    # Ищем все простые числа
    primes = []
    for num in range(2, number + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    # Выводим простые числа в консоль
    print("Простые числа:")
    for prime in primes:
        print(prime)

# Пример использования функции
print_primes(50)