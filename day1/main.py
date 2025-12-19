def getPassword() -> int:
    p = 0
    ii = 50
    with open("./input.txt") as f:
        for line in f:
            line = line.strip()
            dir = line[0]
            rot = int(line[1:])
            ii = (ii + (rot if dir == "R" else -rot)) % 100
            if ii == 0:
                p += 1
    return p


if __name__ == "__main__":
    password = getPassword()
    print("The password is:", password)
