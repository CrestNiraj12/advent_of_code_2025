# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) problems.

## Progress

| Day | Problem | Solution | Status |
|-----|---------|----------|--------|
| 1 | Rotation-based Password | [Python](day1/main.py) | ✅ |
| 2-25 | TBD | - | ⏳ |

## Structure

Each day's solution is organized in its own directory:
```
day{N}/
├── main.py      # Solution implementation
└── input.txt    # Puzzle input
```

## Running Solutions

To run a specific day's solution:
```bash
cd day1
python main.py
```

## About

This repository contains my personal solutions to the Advent of Code 2025 challenges. Each solution is written in Python and focuses on solving the problem efficiently.

## Day 1: Rotation-based Password

The solution processes directional rotation instructions (L/R followed by a number) to calculate a password by tracking position changes that wrap around 100 and counting how many times the position hits zero.
