from line_profiler import LineProfiler

from profiler import main, memory_intensive_function, optimized_fast_function, slow_function, sum_of_squares


def profile_main():
    profiler = LineProfiler(slow_function, optimized_fast_function, memory_intensive_function,
                            sum_of_squares)
    profiler.runcall(main)
    profiler.print_stats()


if __name__ == "__main__":
    profile_main()
