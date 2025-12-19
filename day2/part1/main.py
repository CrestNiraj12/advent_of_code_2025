def sum_of_invalid_ids() -> int:
    iid = 0
    with open("../input.txt") as f:
        ranges = [
            list(map(lambda x: int(x), r.split("-")))
            for r in f.readline().strip().split(",")
        ]
        for r in ranges:
            if len(r) != 2:
                continue

            for i in range(r[0], r[1] + 1):
                str_i = str(i)
                if len(str_i) % 2 != 0:
                    continue

                mi = len(str_i) // 2
                if str_i[:mi] == str_i[mi:]:
                    iid += i

    return iid


if __name__ == "__main__":
    sii = sum_of_invalid_ids()
    print("The sum of invalid ids are:", sii)
