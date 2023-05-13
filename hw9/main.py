from command_generator import command_generator
from commands import *

COMMANDS = {
    "good bye": good_bye,
    "close": close,
    "exit": exit,
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all,
}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except KeyError:
            print("Key error")
        except ValueError:
            print("Value error")
        except IndexError:
            print("Index error")
        else:
            return result

    return wrapper


@input_error
def get_handler(command):
    return COMMANDS[command]


def main():
    for com in command_generator(COMMANDS):
        get_handler(com[0])(com[1:])


if __name__ == "__main__":
    main()
