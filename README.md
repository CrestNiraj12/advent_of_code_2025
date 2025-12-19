# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) problems.

## Progress

| Day | Problem | Solution | Status |
|-----|---------|----------|--------|
| 1 | Rotation-based Password | [Python](day1/main.py) | ✅ |
| 2 | Password Range Validator | [Python](day2/part1/main.py) | 🔄 |
| 3-25 | TBD | - | ⏳ |

## Structure

Each day's solution is organized in its own directory:
```
day{N}/
├── input.txt        # Puzzle input
├── part1/
│   └── main.py      # Part 1 solution
└── part2/
    └── main.py      # Part 2 solution (if completed)
```

Alternatively, for single-file solutions:
```
day{N}/
├── main.py          # Solution implementation
└── input.txt        # Puzzle input
```

## Running Solutions

To run a specific day's solution:
```bash
cd day1
python main.py
```

Or for multi-part solutions:
```bash
cd day2/part1
python main.py
```

## About

This repository contains my personal solutions to the Advent of Code 2025 challenges. Each solution is written in Python and focuses on solving the problem efficiently and clearly.

## Solutions

### Day 1: Rotation-based Password

The solution processes directional rotation instructions (L/R followed by a number) to calculate a password by tracking position changes that wrap around 100 and counting how many times the position hits zero.

**File:** [day1/main.py](day1/main.py)

### Day 2: Password Range Validator

The solution validates password ranges by finding "mirror" numbers within given ranges. For each range, it identifies 6-digit numbers where the first three digits exactly match the last three digits, then sums all valid IDs found across all ranges.

**File:** [day2/part1/main.py](day2/part1/main.py)

## Notes

- All solutions are written in Python 3
- Each solution reads its input from a local `input.txt` file
- Solutions focus on correctness and clarity over optimization
