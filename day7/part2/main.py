from collections import defaultdict


def get_total_timelines() -> int:
    ENTRY, SPLITTER = "S", "^"
    last_index = 0
    col_map = defaultdict(int)

    with open("../input.txt") as f:
        first_line = next(f).strip()
        last_index = len(first_line) - 1
        entry_index = first_line.find(ENTRY)
        assert entry_index != -1, "There must be a tachyon entry point"

        col_map[entry_index] = 1

        for ln in f:
            line = ln.strip()
            next_map = defaultdict(int)
            for i, p in col_map.items():
                if line[i] == SPLITTER:
                    if i < last_index:
                        next_map[i + 1] += p
                    if i > 0:
                        next_map[i - 1] += p
                else:
                    next_map[i] += p

            col_map = next_map
    return sum(col_map.values())


if __name__ == "__main__":
    total_timelines = get_total_timelines()
    print("There are total of", total_timelines, "different timelines")
