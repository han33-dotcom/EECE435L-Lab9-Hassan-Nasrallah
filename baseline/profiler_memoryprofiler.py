from memory_profiler import profile

from profiler import fast_function, memory_intensive_function, slow_function


def main():
    profile(slow_function)()
    profile(fast_function)()
    profile(memory_intensive_function)()


if __name__ == "__main__":
    main()
