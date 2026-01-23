def get_password() -> int:
    p = 0
    ii = 50
    with open("../input.txt") as f:
        for line in f:
            line = line.strip()
            dir = line[0]
            rot = int(line[1:])
            delta = rot if dir == "R" else -rot
            start = ii
            end = start + delta

            if delta > 0:
                p += end // 100 - start // 100
            else:
                p += (start - 1) // 100 - (end - 1) // 100

            ii = end % 100
    return p


if __name__ == "__main__":
    password = get_password()
    print("The password using method 0x434C49434B is:", password)
