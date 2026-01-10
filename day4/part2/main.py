NEIGHBORS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def getTotalAccessiblePapers() -> int:
    roll = "@"
    accessible_rolls = 0

    with open("../input.txt") as f:
        grid = [list(ln.strip()) for ln in f.readlines()]
        total_lines = len(grid)
        if total_lines <= 0:
            return 0

        line_length = len(grid[0])

        while True:
            acc_indeces: list[tuple[int, int]] = []

            for line_count, line in enumerate(grid):
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
                            isRoll = grid[curr_ln][ch_index] == roll
                            if isRoll:
                                adj_roll_count += 1

                    if adj_roll_count < 4:
                        acc_indeces.append((line_count, i))

            for r, c in acc_indeces:
                grid[r][c] = "."

            total_acc = len(acc_indeces)
            if total_acc <= 0:
                break

            accessible_rolls += total_acc
        return accessible_rolls


if __name__ == "__main__":
    tap = getTotalAccessiblePapers()
    print("Total accessible papers:", tap)
