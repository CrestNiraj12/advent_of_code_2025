def get_total_fresh_ingredients() -> int:
    fi_count = 0
    fresh_ranges = []
    with open("../input.txt") as f:
        start_check = False
        for line in f:
            line = line.strip()
            if start_check:
                ingredient = int(line)
                fi_count += int(
                    any(
                        ingredient >= r1 and ingredient <= r2
                        for (r1, r2) in fresh_ranges
                    )
                )
                continue

            if line == "":
                start_check = True
                continue

            f_range = tuple(map(int, line.split("-")))
            fresh_ranges.append(f_range)
    return fi_count


if __name__ == "__main__":
    tfi = get_total_fresh_ingredients()
    print("Total fresh ingredients:", tfi)
