from memory_profiler import profile

from profiler import memory_intensive_function, optimized_fast_function, slow_function


def main():
    profile(slow_function)()
    profile(optimized_fast_function)()
    profile(memory_intensive_function)()


if __name__ == "__main__":
    main()
