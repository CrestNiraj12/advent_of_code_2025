from typing import List, Literal, TypeAlias

State: TypeAlias = tuple[int, ...]
Button: TypeAlias = tuple[int, ...]


def min_presses_greedy_v2(
    target: tuple[int, ...], buttons: List[tuple[int, ...]]
) -> int:
    """
    Greedy: Always press the button that makes the most progress toward
    unsatisfied counters while not overshooting any counter.
    """
    n_counters = len(target)
    state = [0] * n_counters
    presses = 0

    max_presses = sum(target) * 2  # Safety limit

    while tuple(state) != target and presses < max_presses:
        best_button = None
        best_score = -1

        for button in buttons:
            # Can we press this button?
            if any(state[i] >= target[i] for i in button):
                continue

            # Score this button by how much it helps
            score = 0
            for i in button:
                if state[i] < target[i]:
                    # Prioritize counters that are further behind
                    deficit = target[i] - state[i]
                    score += deficit

            if score > best_score:
                best_score = score
                best_button = button

        if best_button is None:
            return -1  # No valid button found

        # Press the best button
        for i in best_button:
            state[i] += 1
        presses += 1

    if tuple(state) == target:
        return presses
    return -1


def total_min_button_presses() -> int:
    presses = 0
    with open("../input.txt") as f:
        for line_num, line in enumerate(f, 1):
            data = [s.strip() for s in line.split()[1:]]
            target = tuple(
                int(d) for d in get_data_from_string(data.pop(), "{}").split(",")
            )
            buttons = [
                tuple(map(int, get_data_from_string(n).split(","))) for n in data
            ]

            print(f"Line {line_num}: target={target}")
            result = min_presses_greedy_v2(target, buttons)

            if result == -1:
                print("  ERROR: No solution found!")
                return -1

            print(f"  Result: {result} presses")
            presses += result

    return presses


def get_data_from_string(s: str, presuff: Literal["()", "{}"] = "()") -> str:
    return s.removeprefix(presuff[0]).removesuffix(presuff[1])


if __name__ == "__main__":
    print("Total minimum button presses:", total_min_button_presses())
