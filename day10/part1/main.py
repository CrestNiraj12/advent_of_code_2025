from collections import deque
from typing import Literal


def total_min_button_presses() -> int:
    presses = 0
    with open("../input.txt") as f:
        for ln in f:
            line = [s.strip() for s in ln.split(" ")]
            indi_lights = get_data_from_string(line[0])

            target = 0
            for i, ch in enumerate(indi_lights):
                if ch == "#":
                    target |= 1 << i

            def mask_from_indices(indices):
                m = 0
                for i in indices:
                    m |= 1 << i
                return m

            buttons = [
                mask_from_indices(map(int, get_data_from_string(s, "()").split(",")))
                for s in line[1:-1]
            ]

            q = deque([0])
            ps = {0: 0}
            min_press = 0

            while q:
                s = q.popleft()
                if s == target:
                    min_press = ps[s]
                    break

                for b in buttons:
                    ns = s ^ b
                    if ns not in ps:
                        ps[ns] = ps[s] + 1
                        q.append(ns)
            presses += min_press
    return presses


def get_data_from_string(s: str, presuff: Literal["[]", "()"] = "[]") -> str:
    return s.removeprefix(presuff[0]).removesuffix(presuff[1])


if __name__ == "__main__":
    print("Total minimum button presses:", total_min_button_presses())
