NEIGHBORS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def getTotalAccessiblePapers() -> int:
    roll = "@"
    accessible_rolls = 0

    with open("../input.txt") as f:
        lines = [ln.strip() for ln in f.readlines()]
        total_lines = len(lines)
        if total_lines <= 0:
            return 0

        line_length = len(lines[0])

        for line_count, line in enumerate(lines):
            for i in range(line_length):
                if line[i] != roll:
                    continue

                adj_roll_count = 0
                for r, c in NEIGHBORS:
                    curr_ln = line_count + r
                    if curr_ln < 0 or curr_ln >= total_lines:
                        continue

                    ch_index = i + c
                    if ch_index >= 0 and ch_index < line_length:
                        isRoll = lines[curr_ln][ch_index] == roll
                        if isRoll:
                            adj_roll_count += 1

                if adj_roll_count < 4:
                    accessible_rolls += 1
        return accessible_rolls


if __name__ == "__main__":
    tap = getTotalAccessiblePapers()
    print("Total accessible papers:", tap)
