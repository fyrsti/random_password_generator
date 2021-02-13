# import random as ra


def send_function_message(text: str):
    def outer(f):
        def wrapper(*args: tuple, **kwargs: dict):
            print(text)
            return f(*args, **kwargs)
        return wrapper
    return outer


def randomize_symbols() -> str:
    pass


def construct_password() -> None:
    pass


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


if __name__ == '__main__':
    main()
