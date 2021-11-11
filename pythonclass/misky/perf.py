"""In which I mess around with preformance profiling.

* https://docs.python.org/3/library/profile.html
"""

import timeit
from pathlib import Path
from statistics import mean
import cProfile

def measure_time():
    """Measuring execution time using the timeit module

    * https://www.guru99.com/timeit-python-examples.html
    * https://docs.python.org/3/library/timeit.html
    """
    init = "from big_o import has_animal"
    code = "has_animal('fox')"
    times = 5

    print(init)
    print(code, "\n")

    results = timeit.timeit(code, setup=init)
    print(results)

    results = timeit.repeat(code, setup=init, repeat=times)
    print("Average of", len(results), "runs:", mean(results))

    timer = timeit.Timer(code, setup=init)
    results = timer.timeit()
    print(results)

    timer = timeit.Timer(code, setup=init)
    results = timeit.repeat(times)
    print("Average of", times, "runs:", results)

def profile():
    from big_o import has_animal
    code = "has_animal('fox')"

    cProfile.run(code)

if __name__ == "__main__":
    #  measure_time()
    profile()
