def fft_dac_combinations() -> int:
    graph = {}
    with open("../input.txt", "r") as f:
        for ln in f:
            if ": " not in ln:
                continue
            key, rhs = ln.strip().split(": ", 1)
            graph[key] = rhs.split()

    memo = {}

    def count(a, b):
        if a == b:
            return 1

        if (a, b) in memo:
            return memo[(a, b)]

        res = sum(count(n, b) for n in graph.get(a, []))
        memo[(a, b)] = res
        return res

    path_a = count("svr", "fft") * count("fft", "dac") * count("dac", "out")
    path_b = count("svr", "dac") * count("dac", "fft") * count("fft", "out")

    return path_a + path_b


if __name__ == "__main__":
    fdc = fft_dac_combinations()
    print(fdc, "of those paths visit both dac and fft.")
