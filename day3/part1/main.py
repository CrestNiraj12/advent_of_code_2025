def getMaximumJoltage() -> int:
    with open("../input.txt") as f:
        total = 0
        for line in f:
            line = line.strip()
            line_len = len(line)
            if line_len <= 2:
                total += int(line)
                continue

            ai = 0
            best_a, best_b = line[0], line[1]
            for i in range(1, line_len):
                sn = line[i]
                n = int(sn)
                if i < line_len - 1 and n > int(best_a):
                    best_a = sn
                    ai = i
                    best_b = line[i + 1]
                elif n > int(best_b) and i > ai:
                    best_b = sn
            total += int(best_a + best_b)
        return total


if __name__ == "__main__":
    toj = getMaximumJoltage()
    print("The total output joltage is:", toj)
