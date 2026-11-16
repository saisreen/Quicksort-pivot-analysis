"""Reproducible benchmark: python benchmark.py (writes results.csv)."""
import csv
import random
import statistics
import time
from pathlib import Path
from quicksort import deterministic_quicksort, randomized_quicksort

SIZES = (100, 300, 600, 1000, 1500)
TRIALS = 9


def make_input(kind, size, seed):
    if kind == 'random':
        rng = random.Random(seed)
        return [rng.randint(-size * 10, size * 10) for _ in range(size)]
    if kind == 'sorted':
        return list(range(size))
    if kind == 'reverse_sorted':
        return list(range(size, 0, -1))
    if kind == 'many_duplicates':
        rng = random.Random(seed)
        return [rng.randint(0, 9) for _ in range(size)]
    raise ValueError(kind)


def main():
    rows = []
    for kind in ('random', 'sorted', 'reverse_sorted', 'many_duplicates'):
        for size in SIZES:
            for name, function in (('fixed_last', deterministic_quicksort),
                                   ('randomized', randomized_quicksort)):
                samples = []
                for trial in range(TRIALS):
                    original = make_input(kind, size, 7000 + trial)
                    data = original.copy()
                    start = time.perf_counter_ns()
                    if name == 'randomized':
                        function(data, random.Random(9000 + trial))
                    else:
                        function(data)
                    elapsed = time.perf_counter_ns() - start
                    assert data == sorted(original)
                    samples.append(elapsed / 1_000_000)
                rows.append({'distribution': kind, 'size': size,
                             'algorithm': name, 'median_ms': round(statistics.median(samples), 4),
                             'trials': TRIALS})
    path = Path(__file__).with_name('results.csv')
    with path.open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f'Wrote {len(rows)} rows to {path}')
    for row in rows:
        if row['size'] == 1500:
            print(row)


if __name__ == '__main__':
    main()
