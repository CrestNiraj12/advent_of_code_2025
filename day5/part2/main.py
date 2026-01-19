def get_total_fresh_ingredients() -> int:
    fresh_count = 0
    ranges: list[tuple[int, int]] = []
    with open("../input.txt") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            r1, r2 = tuple(map(int, line.split("-")))
            ranges.append((r1, r2))

        ranges.sort()
        i = 0
        ranges_len = len(ranges)
        while i < ranges_len:
            r1, r2 = ranges[i]
            li = i + 1
            while li < ranges_len and ranges[li][0] <= r2:
                r2 = max(ranges[li][1], r2)
                li += 1
            fresh_count += r2 - r1 + 1
            i = li

    return fresh_count


if __name__ == "__main__":
    tfi = get_total_fresh_ingredients()
    print("Total fresh ingredients:", tfi)
