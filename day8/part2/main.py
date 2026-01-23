def get_mul_of_xs() -> int:
    circuitsMap = {}
    x1, x2 = 0, 0
    with open("../input.txt") as f:
        lines = [tuple(map(int, ln.strip().split(","))) for ln in f if ln.strip()]
        edges = sorted(
            (
                (
                    (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2,
                    (x1, y1, z1),
                    (x2, y2, z2),
                )
                for i, (x1, y1, z1) in enumerate(lines)
                for j, (x2, y2, z2) in enumerate(lines)
                if j > i
            ),
            key=lambda x: x[0],
        )

        ci = 0
        for _, coord1, coord2 in edges:
            in1 = coord1 in circuitsMap
            in2 = coord2 in circuitsMap

            if in1 and in2:
                c1, c2 = circuitsMap[coord1], circuitsMap[coord2]
                if c1 == c2:
                    continue

                x1, x2 = coord1[0], coord2[0]
                for k in list(circuitsMap.keys()):
                    if circuitsMap[k] == c2:
                        circuitsMap[k] = c1

            elif in1:
                circuitsMap[coord2] = circuitsMap[coord1]
            elif in2:
                circuitsMap[coord1] = circuitsMap[coord2]
            else:
                circuitsMap[coord1] = ci
                circuitsMap[coord2] = ci
                ci += 1

    return x1 * x2


if __name__ == "__main__":
    print(
        "Multiplying together the X coordinates of the last two junction boxes, we get:",
        get_mul_of_xs(),
    )
