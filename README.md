# EECE435L Lab 9 — Profiling in Python

Hassan Nasrallah · Fall 2026–2027

The [lab report](lab9_Hassan_Nasrallah.docx) contains the terminal evidence, the profiling analysis, and the before-and-after comparison. Both versions include the workload, line and memory profiling drivers, and a unittest suite.

| Version | Source | HTML coverage |
| --- | --- | --- |
| Baseline | [baseline](baseline/) | [index.html](coverage/baseline/index.html) |
| Optimized | [optimized](optimized/) | [index.html](coverage/optimized/index.html) |

## Reproduce the results

Install the dependencies from the repository root with Python 3.11.

```sh
python -m venv .venv
```

Activate the virtual environment, then run:

```sh
python -m pip install -r requirements.txt
```

Run the following from the repository root to measure the baseline.

```sh
cd baseline
python -m cProfile -s time profiler.py
python profiler_lineprofiler.py
python -m memory_profiler profiler_memoryprofiler.py
python -m coverage run --source=profiler -m unittest discover
python -m coverage report -m
python -m coverage html -d ../coverage/baseline
```

Repeat from `optimized/` and change the last output path to `../coverage/optimized`. The baseline memory profile can take several minutes because it samples process memory on each traced line event in the ten-million-iteration loop. To view a coverage report, clone or download the repository and open its `index.html` locally so the accompanying HTML, CSS, and JavaScript files are available.
