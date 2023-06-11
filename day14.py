def build_pattern(n, m):
    # Validate input conditions
    if n % 2 == 0 or m != 3 * n:
        print("Invalid input. The number 'n' must be odd and 'm' must be 3 times 'n'.")
        return

    # Top part of the pattern
    for i in range(n // 2):
        pattern = "-".join(["."] * ((m - 3 * (i * 2 + 1)) // 2))
        print(f"{'-' * (3 * i)}{pattern}|{pattern[::-1]}{'-' * (3 * i)}")

    # Middle part of the pattern
    print(f"{'-' * ((m - 7) // 2)}WELCOME{'-' * ((m - 7) // 2)}")

    # Bottom part of the pattern
    for i in reversed(range(n // 2)):
        pattern = "-".join(["."] * ((m - 3 * (i * 2 + 1)) // 2))
        print(f"{'-' * (3 * i)}{pattern}|{pattern[::-1]}{'-' * (3 * i)}")


# Test the function
n = 7
m = 21
build_pattern(n, m)
