import random
import symbols as sm
# because we don't want to get duplicates of the same letter, symbol, number


def count():
    """Get the number of required letters, symbols and numbers"""
    letter_trigger = True
    while letter_trigger:
        try:
            how_letters = int(input("How many letters would you like in your password? "))
            letter_trigger = False
            break
        except ValueError:
            print("\nWARNING: VALUE ERROR!!! \nPLEASE ENTER CORRECT NUMBER OF REQUIRED LETTERS (NUMBER ONLY!)\n")
            continue
    numbers_trigger = True
    while numbers_trigger:
        try:
            how_numbers = int(input("How many numbers would you like in your password? "))
            numbers_trigger = False
            break
        except ValueError:
            print("\nWARNING: VALUE ERROR!!! \nPLEASE ENTER CORRECT NUMBER OF REQUIRED NUMBERS (NUMBER ONLY!)\n")
            continue
    symbols_trigger = True
    while symbols_trigger:
        try:
            how_symbols = int(input("How many symbols would you like in your password? "))
            symbols_trigger = False
            break
        except ValueError:
            print("\nWARNING: VALUE ERROR!!! \nPLEASE ENTER CORRECT NUMBER OF REQUIRED SYMBOLS (NUMBER ONLY!)\n")
            continue

    result = (how_letters, how_numbers, how_symbols)
    return result


def generation(count_letter: int, count_number: int, count_symbol: int) -> str:
    """Generation password"""
    letters = random.choices(sm.symbols["letters"], k=count_letter)
    numbers = random.choices(sm.symbols["numbers"], k=count_number)
    symbols = random.choices(sm.symbols["symbols"], k=count_symbol)
    pre_list = []
    for item in letters:
        pre_list.append(item)
    for item in numbers:
        pre_list.append(str(item))
    for item in symbols:
        pre_list.append(item)
    random.shuffle(pre_list)
    password = ''.join(pre_list)
    answer = f'Your password is: {password}'
    return answer


if __name__ == '__main__':
    counter = count()
    print(generation(counter[0], counter[1], counter[2]))

