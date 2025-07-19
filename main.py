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

# def generator_numbers(text: str):
#     # Розбиваємо текст на слова за пробілами
#     for word in text.split():
#         try:
#             # Пробуємо перетворити слово на float
#             # Якщо вдається — це дійсне число доходу, повертаємо його
#             yield float(word)
#         except ValueError:
#             # Ігноруємо якщо перетворення не вдалося 
#             continue

# def sum_profit(text: str, func):
#     # Викликаємо генератор і підсумовуємо всі знайдені числа
#     return sum(func(text))



# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")

# ***************************************************************

# Завдання 4

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return wrapper

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue  # ignore empty lines

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
