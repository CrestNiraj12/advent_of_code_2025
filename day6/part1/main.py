import operator
from functools import reduce


def get_grand_total() -> int:
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    grand_total = 0
    with open("../input.txt") as f:
        lines = [ln.split() for ln in f.readlines()]
        if not lines:
            return 0

        total_lines = len(lines)
        line_len = len(lines[0])
        for j in range(line_len):
            nums = []
            for i in range(total_lines):
                n = lines[i][j]
                if nums and n in ops:
                    grand_total += reduce(ops[n], nums)
                    break
                nums.append(int(n))

    return grand_total


if __name__ == "__main__":
    gt = get_grand_total()
    print("Grand total is", gt)
