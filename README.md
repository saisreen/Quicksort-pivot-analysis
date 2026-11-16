# Assignment 5 — Quicksort: Pivot Choice and Input Order

This project compares two in-place Quicksort versions: a deterministic last-element pivot and a uniformly randomized pivot. It studies an often overlooked point: randomizing the pivot helps on ordered input, but does not fix the duplicate-key problem of two-way partitioning.

## Files
- `quicksort.py` — documented implementations
- `test_quicksort.py` — unit tests and edge cases
- `benchmark.py` — repeatable timing experiment
- `results.csv` — measured medians from one run (milliseconds)
- `Assignment_5_Quicksort_Report.docx` — analysis and discussion

## Run (Python 3.9+; standard library only)
```bash
python -m unittest -v
python benchmark.py
```
Run commands from this repository directory. Benchmark execution replaces `results.csv` with new measurements. Timing depends on the machine and current system load.

## Main findings
- Last-element pivot Quicksort slows substantially on already sorted and reverse-sorted inputs.
- Randomized pivot usually avoids those input-order slowdowns, with some pivot-selection overhead.
- Both use two-way Lomuto partitioning, so many equal values can still produce unbalanced partitions.
- Both sort in place; sorting the smaller partition recursively and processing the larger one in a loop limits call-stack depth to O(log n), including worst-case inputs.

## Experiment design
Sizes: 100, 300, 600, 1000, 1500. Distributions: random, sorted, reverse-sorted, many duplicates. Nine runs per combination; median reported. Seeds make inputs and pivot choices reproducible, but runtime is not identical across computers.
