import random as ra

PUNCTUATION_CODES = (33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                     47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96)


def send_function_message(text: str):
    def outer(f):
        def wrapper(*args: tuple, **kwargs: dict):
            print(text)
            return f(*args, **kwargs)
        return wrapper
    return outer


def randomize_symbols(n: bool, p: bool, r: bool) -> int:
    if n and p and r:
        return ra.choice((ra.randint(48, 57),
                          ra.randint(65, 90),
                          ra.randint(97, 122),
                          ra.choice(PUNCTUATION_CODES))
                         )
    elif n and p:
        return ra.choice((ra.randint(48, 57),
                          ra.randint(97, 122),
                          ra.choice(PUNCTUATION_CODES))
                         )
    elif n and r:
        return ra.choice((ra.randint(48, 57),
                          ra.randint(65, 90),
                          ra.randint(97, 122))
                         )
    elif p and r:
        return ra.choice((ra.randint(65, 90),
                          ra.randint(97, 122),
                          ra.choice(PUNCTUATION_CODES),)
                         )
    elif n:
        return ra.choice((ra.randint(48, 57), ra.randint(97, 122)))
    elif p:
        return ra.choice((ra.choice(PUNCTUATION_CODES), ra.randint(97, 122)))
    elif r:
        return ra.choice((ra.randint(65, 90), ra.randint(97, 122)))
    else:
        return ra.randint(97, 122)


def construct_password(length: int, numbers: bool, punct: bool, register: bool) -> str:
    result = list()
    for _ in range(length):
        while 1:
            if (n := chr(randomize_symbols(numbers, punct, register))) not in result:
                print(chr(randomize_symbols(numbers, punct, register)))
                result.append(n)
                break
    return "".join(result)


@send_function_message("Укажите длину пароля в символах [от 3 до 32]")
def asknumber(minborder: float, maxborder: float) -> int:
    while 1:
        response = get_input()
        if validate_number(response, minborder, maxborder): return int(response)
        else:
            print(f'Вы указали неверное значение. Число должно быть в промежутке от {minborder} до {maxborder}')


def validate_number(input_str: str, minborder: float, maxborder: float) -> bool:
    try:
        if float(input_str) < minborder or float(input_str) > maxborder or int(input_str) != float(input_str):
            raise ValueError
    except ValueError:
        return False
    else:
        return True


def askyesno() -> bool:
    return True if get_input() == '+' else False


def get_input() -> str:
    return input()


def main() -> None:
    password_length: int = asknumber(3, 32)
    print("\n[+ - для положительного ответа]\n[Нажмите \"Enter\" для отрицательного ответа]\n")
    include_numbers = send_function_message("Использовать числа в пароле?: ")(askyesno)()
    include_punc = send_function_message("Использовать знаки пунктуации в пароле?: ")(askyesno)()
    register = send_function_message("Учитывать регистр символов в пароле?: ")(askyesno)()
    print(f'Ваш пароль: {construct_password(password_length, include_numbers, include_punc, register)}')


if __name__ == '__main__':
    main()
