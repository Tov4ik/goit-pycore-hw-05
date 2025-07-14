# Завдання 1

# def caching_fibonacci():
#     cache = {}  # Локальний словник для збереження обчислених значень

#     def fibonacci(n):
#         if n <= 0:
#             return 0
#         if n == 1:
#             return 1
#         if n in cache:
#             return cache[n]
        
#         # Рекурсивно обчислюємо значення, якщо його ще нема в кеші
#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return cache[n]

#     return fibonacci

# fib = caching_fibonacci()

# print(fib(10))  # ➜ 55
# print(fib(15))  # ➜ 610
# print(fib(35))  # ➜ 9227465 (швидко, бо з кешем)

# ***************************************************************

# Завдання 2

def generator_numbers(text: str):
    # Розбиваємо текст на слова за пробілами
    for word in text.split():
        try:
            # Пробуємо перетворити слово на float
            # Якщо вдається — це дійсне число доходу, повертаємо його
            yield float(word)
        except ValueError:
            # Ігноруємо якщо перетворення не вдалося 
            continue

def sum_profit(text: str, func):
    # Викликаємо генератор і підсумовуємо всі знайдені числа
    return sum(func(text))



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
