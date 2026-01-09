def getTotalAccessiblePapers() -> int:
    roll = "@"
    accessible_rolls = 0

    with open("./input.txt") as f:
        lines = [ln.strip() for ln in f.readlines()]
        totalLines = len(lines)
        if totalLines <= 0:
            return 0

        line_length = len(lines[0])
        directions = (-1, 0, 1)

        for line_count, line in enumerate(lines):
            for i in range(line_length):
                if line[i] != roll:
                    continue

                adj_roll_count = 0
                # up -1, curr 0 or down +1
                for ln in directions:
                    curr_ln = line_count + ln
                    if curr_ln < 0 or curr_ln >= totalLines:
                        continue

                    # left -1, curr 0 or right +1
                    for ch in directions:
                        ch_index = i + ch
                        if ln == 0 and ch_index == i:
                            continue

                        if ch_index >= 0 and ch_index < line_length:
                            isRoll = lines[curr_ln][ch_index] == roll
                            if isRoll:
                                adj_roll_count += 1

                if adj_roll_count < 4:
                    accessible_rolls += 1

            line_count += 1
        return accessible_rolls


if __name__ == "__main__":
    tap = getTotalAccessiblePapers()
    print("Total accessible papers:", tap)
