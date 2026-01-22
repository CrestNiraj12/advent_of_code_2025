def get_beam_split_times() -> int:
    ENTRY, SPLITTER = "S", "^"
    prev_indices, beam_indices = set(), set()
    first_line = True
    split_count = 0
    last_index = 0
    with open("../input.txt") as f:
        for ln in f:
            line = ln.strip()
            if first_line:
                last_index = len(line) - 1
                entry_index = line.find(ENTRY)
                assert entry_index != -1, "There must be a tachyon entry point"

                prev_indices.add(entry_index)
                first_line = False
                continue

            for i in prev_indices:
                if line[i] == SPLITTER:
                    if i < last_index:
                        beam_indices.add(i + 1)

                    if i > 0:
                        beam_indices.add(i - 1)

                    split_count += 1
                else:
                    beam_indices.add(i)

            prev_indices, beam_indices = beam_indices, prev_indices
            beam_indices.clear()

    return split_count


if __name__ == "__main__":
    bst = get_beam_split_times()
    print("The beam splitted", bst, "time(s)")
