def sum_of_squares(count):
    """Sum the squares of the integers from zero through count minus one."""
    return (count - 1) * count * (2 * count - 1) // 6


def slow_function():
    return sum_of_squares(10_000)


def optimized_fast_function():
    return sum_of_squares(100)


def memory_intensive_function():
    return sum_of_squares(10_000_000)


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()
