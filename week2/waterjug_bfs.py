from collections import deque

A = 4
B = 3
target = 2

visited = set()
q = deque()

q.append((0, 0))
visited.add((0, 0))

found = False

while q:
    x, y = q.popleft()

    if x == target or y == target:
        print(f"Target achieved at ({x}, {y})")
        found = True
        break

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
            visited.add((nx, ny))
            q.append((nx, ny))

if not found:
    print("Target cannot be achieved")
