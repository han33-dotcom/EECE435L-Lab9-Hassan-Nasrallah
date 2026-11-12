import time
import unittest

from memory_profiler import memory_usage

from profiler import memory_intensive_function, optimized_fast_function, slow_function


class TestProfiler(unittest.TestCase):
    def time_function(self, function):
        start = time.perf_counter()
        result = function()
        return result, time.perf_counter() - start

    def test_slow_function(self):
        result, duration = self.time_function(slow_function)
        print(f"slow_function executed in {duration:.6f} seconds.")
        self.assertEqual(result, 333_283_335_000)
        self.assertLess(duration, 1.0)

    def test_fast_function(self):
        result, duration = self.time_function(optimized_fast_function)
        print(f"{optimized_fast_function.__name__} executed in {duration:.6f} seconds.")
        self.assertEqual(result, 328_350)
        self.assertLess(duration, 1.0)

    def test_memory_intensive_function(self):
        before = memory_usage(-1, interval=0.1, timeout=0.1)[0]
        result, duration = self.time_function(memory_intensive_function)
        after = memory_usage(-1, interval=0.1, timeout=0.1)[0]
        print(f"memory_intensive_function executed in {duration:.6f} seconds.")
        print(f"Process RSS before: {before:.2f} MiB, after: {after:.2f} MiB.")
        self.assertEqual(result, 333_333_283_333_335_000_000)
        self.assertLess(duration, 5.0)


if __name__ == "__main__":
    unittest.main()
