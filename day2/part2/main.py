def sum_of_invalid_ids() -> int:
    iid = 0
    with open("../input.txt") as f:
        ranges = [
            tuple(map(int, line.split("-")))
            for lines in f
            for line in lines.strip().split(",")
        ]
        for r1, r2 in ranges:
            for n in range(r1, r2 + 1):
                str_n = str(n)
                len_n = len(str_n)
                for div in range(1, (len_n // 2) + 1):
                    if len_n % div != 0:
                        continue

                    part = len_n // div
                    block = str_n[:div]
                    if block * part == str_n:
                        iid += n
                        break

    return iid


if __name__ == "__main__":
    sii = sum_of_invalid_ids()
    print("The sum of invalid ids are:", sii)
