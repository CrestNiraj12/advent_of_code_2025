def get_largest_rect() -> int:
    largest_area = 0
    with open("../input.txt") as f:
        coords = [tuple(map(int, line.strip().split(","))) for line in f]
        coords.sort(key=lambda x: x[0])
        total_coords = len(coords)
        only_ys = [y for _, y in coords]
        max_possible_height = max(only_ys) - min(only_ys) + 1
        for i in range(total_coords - 1):
            x, y = coords[i]
            for j in range(total_coords - 1, i, -1):
                x2, y2 = coords[j]
                width = x2 - x + 1
                if width * max_possible_height <= largest_area:
                    break

                height = abs(y - y2) + 1
                largest_area = max(largest_area, width * height)
    return largest_area


if __name__ == "__main__":
    print("Largest area of rectange:", get_largest_rect())
