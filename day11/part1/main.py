from collections import deque


def let_me_out_combinations() -> int:
    with open("../input.txt", "r") as f:
        graph = {}
        for ln in f:
            if ": " not in ln:
                continue

            key, rhs = ln.strip().split(": ", 1)
            graph[key] = rhs.split()

        stack = deque([("you", False)])
        seen = {"out": 1}

        while stack:
            p, traversed = stack.pop()

            if p in seen:
                continue

            if p == "out":
                continue

            if not traversed:
                stack.append((p, True))
                for n in graph.get(p, []):
                    if n not in seen:
                        stack.append((n, False))
                continue

            total = 0
            for n in graph.get(p, []):
                total += seen.get(n, 0)
            seen[p] = total

        return seen.get("you", 0)


if __name__ == "__main__":
    lmec = let_me_out_combinations()
    print("I can take", lmec, "different paths")
