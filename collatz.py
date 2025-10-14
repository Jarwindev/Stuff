def main():
    integer = int(input("Enter a positive integer: "))
    journey = collatz(integer)
    print(journey)


def collatz(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("number must be a positive integer")

    journey = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        journey.append(number)

    return journey


if __name__ == "__main__":
    main()

