import heapq
from collections import Counter
from math import prod


def get_largest_circuits_mul() -> int:
    circuits_map = {}
    with open("../input.txt") as f:
        lines = [tuple(map(int, ln.strip().split(","))) for ln in f if ln.strip()]
        edges = (
            (
                (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2,
                (x1, y1, z1),
                (x2, y2, z2),
            )
            for i, (x1, y1, z1) in enumerate(lines)
            for j, (x2, y2, z2) in enumerate(lines)
            if j > i
        )
        sorted_top_ds = heapq.nsmallest(1000, edges, key=lambda x: x[0])

        ci = 0
        for _, coord_1, coord_2 in sorted_top_ds:
            in1 = coord_1 in circuits_map
            in2 = coord_2 in circuits_map

            if in1 and in2:
                c1, c2 = circuits_map[coord_1], circuits_map[coord_2]
                if c1 == c2:
                    continue

                for k in list(circuits_map.keys()):
                    if circuits_map[k] == c2:
                        circuits_map[k] = c1

            elif in1:
                circuits_map[coord_2] = circuits_map[coord_1]
            elif in2:
                circuits_map[coord_1] = circuits_map[coord_2]
            else:
                circuits_map[coord_1] = ci
                circuits_map[coord_2] = ci
                ci += 1

    sizes = Counter(circuits_map.values())
    top3 = sorted(sizes.values(), reverse=True)[:3]
    return prod(top3)


if __name__ == "__main__":
    print("The 3 largest circuit sizes multiplied is:", get_largest_circuits_mul())
