def sum_of_invalid_ids() -> int:
    iid = 0
    with open("../input.txt") as f:
        ranges = [
            tuple(map(int, r.split("-"))) for r in f.readline().strip().split(",")
        ]
        for start, end in ranges:
            for n in range(start, end + 1):
                s = str(n)
                mi = len(s) // 2
                if len(s) % 2 == 0 and s[:mi] == s[mi:]:
                    iid += n

    return iid


if __name__ == "__main__":
    sii = sum_of_invalid_ids()
    print("The sum of invalid ids are:", sii)
