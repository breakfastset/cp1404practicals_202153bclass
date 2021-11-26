import random


def get_random_boolean():
    """Return True if number is 0, False otherwise"""
    number = random.randint(0, 1)
    return number == 0


def get_random_boolean_version_2():
    """Return True if number is even"""
    number = random.randint(1, 10)
    return number % 2 == 0


def get_random_boolean_version_3():
    """Return True if number is greater than 5"""
    number = random.randint(1, 10)
    return number > 5


def main():
    """Start program"""
    is_happy = get_random_boolean()
    print("Is Happy? ", is_happy)

    is_sad = get_random_boolean_version_2()
    print("Is Sad? ", is_sad)

    is_excited = get_random_boolean_version_3()
    print("Is Excited? ", is_excited)


if __name__ == '__main__':
    main()
