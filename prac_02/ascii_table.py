LOWER = 33
UPPER = 127


def display_ascii_table():
    for code in range(LOWER, UPPER + 1):
        print(f"{code:<4} {chr(code):>4}")


def main():
    character = input("Enter a character: ")
    print(f"The Ascii code for {character} is {ord(character)}")

    number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
    while number < LOWER or number > UPPER:
        print(f"  <Error> - Number must be between {LOWER} and {UPPER} !!!")
        number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
    print(f"The character for {number} is {chr(number)}")

    display_ascii_table()


if __name__ == '__main__':
    main()
