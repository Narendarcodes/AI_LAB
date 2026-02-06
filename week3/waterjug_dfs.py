A = 4
B = 3
target = 2

visited = set()

def dfs(x, y):
    if x == target or y == target:
        print(f"Target achieved at ({x}, {y})")
        return True

    visited.add((x, y))

    next_states = [
        (A, y),
        (x, B),
        (0, y),
        (x, 0),
        (x - min(x, B - y), y + min(x, B - y)),
        (x + min(y, A - x), y - min(y, A - x))
    ]

    for nx, ny in next_states:
        if 0 <= nx <= A and 0 <= ny <= B and (nx, ny) not in visited:
            if dfs(nx, ny):
                return True

    return False

if not dfs(0, 0):
    print("Target cannot be achieved")
