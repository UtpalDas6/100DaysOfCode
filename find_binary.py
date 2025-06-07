"""Convert an integer to its binary representation."""

def binary(num: int) -> str:
    """Return the binary representation of ``num``.

    Parameters
    ----------
    num : int
        The non-negative integer to convert.

    Returns
    -------
    str
        Binary string without leading ``0b`` prefix.
    """

    if num == 0:
        return "0"

    val = ""
    while num > 0:
        val = str(num % 2) + val
        num //= 2
    return val


if __name__ == "__main__":
    num = int(input("Enter any number: "))
    print("Binary Equivalent: ", binary(num))
