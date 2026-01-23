def get_beam_split_times() -> int:
    ENTRY, SPLITTER = "S", "^"
    prev_indices = set()
    split_count = 0
    last_index = 0
    with open("../input.txt") as f:
        first_line = next(f).strip()
        last_index = len(first_line) - 1
        entry_index = first_line.find(ENTRY)
        assert entry_index != -1, "There must be a tachyon entry point"

        prev_indices.add(entry_index)

        for ln in f:
            line = ln.strip()
            beam_indices = set()
            for i in prev_indices:
                if line[i] == SPLITTER:
                    if i < last_index:
                        beam_indices.add(i + 1)

                    if i > 0:
                        beam_indices.add(i - 1)

                    split_count += 1
                else:
                    beam_indices.add(i)

            prev_indices = beam_indices

    return split_count


if __name__ == "__main__":
    bst = get_beam_split_times()
    print("The beam splitted", bst, "time(s)")
