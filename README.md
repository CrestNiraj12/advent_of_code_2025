# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) problems.

## Progress

| Day | Problem | Solution | Status |
|-----|---------|----------|--------|
| 1 | Rotation-based Password | [Python](day1/main.py) | ✅ |
| 2 | Password Range Validator | [Part 1](day2/part1/main.py), [Part 2](day2/part2/main.py) | ✅ |
| 3 | Maximum Joltage Calculator | [Part 1](day3/part1/main.py), [Part 2](day3/part2/main.py) | ✅ |
| 4 | Accessible Papers | [Part 1](day4/part1/main.py), [Part 2](day4/part2/main.py) | ✅ |
| 5 | Fresh Ingredients | [Part 1](day5/part1/main.py), [Part 2](day5/part2/main.py) | ✅ |
| 6 | Column Calculator | [Part 1](day6/part1/main.py), [Part 2](day6/part2/main.py) | ✅ |
| 7-25 | TBD | - | ⏳ |

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

**Part 1:** The solution validates password ranges by finding "mirror" numbers within given ranges. For each range, it identifies numbers where the first half of the digits exactly match the second half (e.g., 123123), then sums all valid IDs found across all ranges.

**Part 2:** Extends validation to find numbers with any repeating pattern. It checks if a number can be formed by repeating a smaller block of digits multiple times (e.g., 121212 = 12 repeated 3 times, or 111111 = 1 repeated 6 times).

**Files:** [Part 1](day2/part1/main.py), [Part 2](day2/part2/main.py)

### Day 3: Maximum Joltage Calculator

**Part 1:** The solution processes lines of numerical data to calculate total output joltage. For each line, it identifies the two highest single-digit values and sums them. Lines with 2 or fewer characters are treated as direct values and added to the total.

**Part 2:** Uses a sliding-window strategy to build a 12-digit value from each line. It repeatedly selects the highest digit within the current valid range, appends it to the result, and shifts the window until 12 digits are chosen, then sums these values across all lines.

**Files:** [Part 1](day3/part1/main.py), [Part 2](day3/part2/main.py)

### Day 4: Accessible Papers

**Part 1:** Counts how many '@' cells in the grid have fewer than four adjacent '@' neighbors. Adjacency is checked in all 8 directions (including diagonals).

**Part 2:** Iteratively removes accessible '@' cells (those with fewer than four adjacent '@' neighbors) until no more are removable, and returns the total removed across all iterations.

**Files:** [Part 1](day4/part1/main.py), [Part 2](day4/part2/main.py)

### Day 5: Fresh Ingredients

**Part 1:** Given a list of fresh ingredient ranges and individual ingredient values, counts how many ingredients fall within any of the fresh ranges.

**Part 2:** Merges overlapping fresh ingredient ranges and counts the total number of fresh ingredients by summing the span of each merged range.

**Files:** [Part 1](day5/part1/main.py), [Part 2](day5/part2/main.py)

### Day 6: Column Calculator

**Part 1:** Reads a grid of numbers and operators column by column. For each column, collects numbers until an operator (+, -, *) is found, then applies that operator to all collected numbers using reduce and adds the result to the grand total.

**Part 2:** Processes the grid columns from right to left, building multi-digit numbers from consecutive digits in each column. When an operator (+, -, *) is encountered, applies the operation to all numbers collected in that column using functools.reduce and adds the result to the grand total. Skips processing the next column if it's empty following an operator.

**Files:** [Part 1](day6/part1/main.py), [Part 2](day6/part2/main.py)

## Notes

- All solutions are written in Python 3
- Each solution reads its input from a local `input.txt` file
- Solutions focus on correctness and clarity over optimization
