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
        lines = f.read().splitlines()
        if not lines:
            return 0

        line_len = len(lines[0])
        nums: list[int] = []
        skip_empty_column = False

        for col in range(line_len - 1, -1, -1):
            if skip_empty_column:
                skip_empty_column = False
                continue

            num = None
            for line in lines:
                if col >= len(line):
                    continue

                n = line[col]
                if n == " ":
                    continue

                if n in ops:
                    if num is not None:
                        nums.append(num)

                    if nums:
                        grand_total += reduce(ops[n], nums)

                    nums.clear()
                    skip_empty_column = True
                    break

                num = num * 10 + int(n) if num is not None else int(n)

            if not skip_empty_column and num is not None:
                nums.append(num)

    return grand_total


if __name__ == "__main__":
    gt = get_grand_total()
    print("Grand total is", gt)
