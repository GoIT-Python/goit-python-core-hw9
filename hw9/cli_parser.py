import re


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except KeyError:
            print(KeyError)
        except ValueError:
            print(ValueError)
        except IndexError:
            print(IndexError)
        else:
            return result

    return wrapper


# @input_error
def cli_parser(commands):
    cli = []
    query = input().strip().casefold()
    for command in map(lambda command: rf"{command}", commands):
        res = re.match(command, query, flags=re.IGNORECASE)
        if res:
            cli.append(res.group())
            cli.extend(re.sub(command, "", query).split(" ")[1:])
    # if not cli[0] in commands:
    #     raise ValueError("Wrong command")
    return cli


if __name__ == "__main__":
    pass
    # cli_parser(commands)
