from __future__ import annotations

from typing import Dict, Tuple

INF = 10**18

State = Tuple[int, ...]
Button = Tuple[int, ...]


def parse_line(line: str) -> tuple[list[Button], State]:
    parts = line.split()
    # parts[0] is the lights diagram; ignore
    tokens = parts[1:]

    target_tok = tokens[-1]
    target = tuple(int(x) for x in target_tok[1:-1].split(","))

    buttons: list[Button] = []
    for tok in tokens[:-1]:
        inner = tok[1:-1]
        if inner == "":
            continue

        buttons.append(tuple(int(x) for x in inner.split(",")))
    return buttons, target


def pattern(vec: State) -> int:
    p = 0
    for i, v in enumerate(vec):
        if v & 1:  # check if the value is odd
            p |= 1 << i
    return p


def solve_machine(buttons: list[Button], target: State) -> int:
    n = len(target)
    m = len(buttons)

    combos_by_pattern: Dict[int, list[tuple[int, State]]] = {}

    for mask in range(1 << m):
        presses = 0
        joltage = [0] * n

        for j in range(m):
            if (mask >> j) & 1 == 0:
                continue
            presses += 1
            for i in buttons[j]:
                joltage[i] += 1

        jv = tuple(joltage)
        pat = pattern(jv)
        combos_by_pattern.setdefault(pat, []).append((presses, jv))

    # Memoized recursion: T = Ar + 2Ay  =>  y solves (T - Ar)/2
    cache: Dict[State, int] = {}

    def count_presses(t: State) -> int:
        if t in cache:
            return cache[t]

        # Reject negative, accept all-zero
        only_zeros = True
        for v in t:
            if v < 0:
                return INF
            if v > 0:
                only_zeros = False
        if only_zeros:
            return 0

        pat = pattern(t)
        combos = combos_by_pattern.get(pat)
        if not combos:
            cache[t] = INF
            return INF

        best = INF
        # try all parity-compatible subsets
        for presses, jv in combos:
            # compute (t - jv) / 2 (guaranteed integer if parity matches)
            half = []
            ok = True
            for i in range(n):
                diff = t[i] - jv[i]
                if diff < 0:
                    ok = False
                    break
                half.append(diff // 2)
            if not ok:
                continue

            sub = count_presses(tuple(half))
            if sub >= INF:
                continue

            total = presses + 2 * sub
            if total < best:
                best = total

        cache[t] = best
        return best

    ans = count_presses(target)
    if ans >= INF:
        raise ValueError(f"Unreachable target: {target}")
    return ans


def total_min_button_presses() -> int:
    total = 0
    with open("../input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            buttons, target = parse_line(line)
            total += solve_machine(buttons, target)
    return total


if __name__ == "__main__":
    print("Total minimum button presses:", total_min_button_presses())
