def getMaximumJoltage() -> int:
    with open("../input.txt") as f:
        total = 0
        for line in f:
            line = line.strip()
            len_line = len(line)
            if len_line <= 12:
                total += int(line)
                break

            i = 1
            req_len = 12
            end = len_line - req_len
            best_i = 0
            result = ""
            while i < end + 1 and end < len_line:
                n = line[i]
                if n > line[best_i]:
                    best_i = i

                i += 1
                if i > end:
                    result += line[best_i]
                    i = best_i + 1
                    end = len_line - req_len + len(result)
                    best_i = i
            total += int(result)
        return total


if __name__ == "__main__":
    toj = getMaximumJoltage()
    print("The total output joltage is:", toj)
