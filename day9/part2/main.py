from collections import deque


def get_largest_valid_rect() -> int:
    with open("../input.txt") as f:
        coords = [(x, y) for line in f for x, y in [map(int, line.strip().split(","))]]
        total_coords = len(coords)

        xs = sorted({x + dx for x, _ in coords for dx in (-1, 0, 1)})
        ys = sorted({y + dy for _, y in coords for dy in (-1, 0, 1)})
        x_id = {x: i for i, x in enumerate(xs)}
        y_id = {y: i for i, y in enumerate(ys)}
        boundary = set()

        # Compressed boundary tracing
        for i in range(total_coords):
            cx, cy = coords[i]  # current coords
            nx, ny = coords[(i + 1) % total_coords]  # next

            x1, y1 = x_id[cx], y_id[cy]
            x2, y2 = x_id[nx], y_id[ny]

            dx = 0 if x1 == x2 else (1 if x1 < x2 else -1)
            dy = 0 if y1 == y2 else (1 if y1 < y2 else -1)

            x, y = x1, y1
            while (x, y) != (x2, y2):
                boundary.add((x, y))
                x += dx
                y += dy
            boundary.add((x2, y2))

        W, H = len(xs), len(ys)
        queue = deque([(0, 0)])
        outside = {(0, 0)}
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # Flood filling the outside
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy

                if (
                    not (0 <= nx < W and 0 <= ny < H)
                    or (nx, ny) in outside
                    or (nx, ny) in boundary
                ):
                    continue

                outside.add((nx, ny))
                queue.append((nx, ny))

        # Fill the grid with 1s and 0s
        # 1 if the coordinate is outside the boundary
        grid_map = [[1 if (x, y) in outside else 0 for x in range(W)] for y in range(H)]

        # Fill the grid with prefix sums (sum of curr, left and up tile)
        for y in range(H):
            for x in range(W):
                up = grid_map[y - 1][x] if y > 0 else 0
                left = grid_map[y][x - 1] if x > 0 else 0
                up_left = grid_map[y - 1][x - 1] if x > 0 and y > 0 else 0
                grid_map[y][x] = grid_map[y][x] + up + left - up_left

        def ps(y, x):
            if x < 0 or y < 0:
                return 0
            return grid_map[y][x]

        # Compressed red tiles
        comp_red = {(x_id[x], y_id[y]) for (x, y) in coords}
        largest_area = 0

        # Find the largest area of valid tiles
        for rx1, ry1 in comp_red:
            for rx2, ry2 in comp_red:
                x1, x2 = sorted((rx1, rx2))
                y1, y2 = sorted((ry1, ry2))
                outside_count = (
                    ps(y2, x2) - ps(y1 - 1, x2) - ps(y2, x1 - 1) + ps(y1 - 1, x1 - 1)
                )

                # rectangle is valid when prefix sum is 0
                if outside_count == 0:
                    width = abs(xs[x2] - xs[x1]) + 1
                    height = abs(ys[y2] - ys[y1]) + 1
                    largest_area = max(largest_area, width * height)

        return largest_area


if __name__ == "__main__":
    print(
        "Largest area of rectangle using only red and green tiles:",
        get_largest_valid_rect(),
    )
