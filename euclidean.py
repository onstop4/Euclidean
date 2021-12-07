from argparse import ArgumentParser


def euclidean(N: int, a: int) -> int:
    """
    Uses the Euclidean Algorithm to calculate the GCD of `N` and `a`.
    """
    remainder = N % a
    if remainder == 0:
        return a
    return euclidean(a, remainder)


def _eGCD(a: int, b: int) -> tuple[int, int, int]:
    """
    Private function that assists in calculating the modular inverse.
    """
    quotient, remainder = divmod(a, b)
    if remainder == 0:
        return (b, 0, 1)
    d, X, Y = _eGCD(b, remainder)
    return (d, Y, X - Y * quotient)


def extended_euclidean(N: int, a: int) -> int:
    """
    Uses the Extended Euclidean Algorithm to calculate the modular inverse of :math:`a`
    in :math:`a mod N`. Raises :exc:`ValueError` if the inverse does not exist.
    """
    d, X, Y = _eGCD(a, N)  # pylint: disable=unused-variable
    if d != 1:
        raise ValueError("No inverse found")
    return X % N


def parse_args():
    """
    Parses and returns command line arguments.
    """
    parser = ArgumentParser()
    parser.add_argument(
        "ALGORITHM",
        type=str.upper,
        choices=["EA", "EEA"],
        help='Use "EA" to find GCD using the Euclidean Algorithm. '
        'Use "EEA" to find inverse using Extended Euclidean Algorithm.',
    )
    parser.add_argument("MODULUS", type=int)
    parser.add_argument("INTEGER", type=int)

    return parser.parse_args()


def main():
    """
    Main function that will be called when running this file as a script.
    """
    args = parse_args()

    modulus = args.MODULUS
    integer = args.INTEGER

    try:
        if args.ALGORITHM == "EA":
            result = euclidean(modulus, integer)
        else:
            result = extended_euclidean(modulus, integer)
        print(result)

    except ValueError:
        print("No inverse found.")

    except ZeroDivisionError:
        print("Inputted values should be greater than zero.")


if __name__ == "__main__":
    main()
