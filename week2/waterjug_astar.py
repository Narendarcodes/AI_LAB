import heapq

A = 4
B = 3
target = 2

def heuristic(x, y):
    return min(abs(x - target), abs(y - target))

visited = set()
pq = []

h0 = heuristic(0, 0)
heapq.heappush(pq, (h0, 0, 0, 0))

found = False

while pq:
    f, g, x, y = heapq.heappop(pq)

    if x == target or y == target:
        print(f"Target achieved at ({x}, {y})")
        found = True
        break

    if (x, y) in visited:
        continue

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
            ng = g + 1
            nh = heuristic(nx, ny)
            nf = ng + nh
            heapq.heappush(pq, (nf, ng, nx, ny))

if not found:
    print("Target cannot be achieved")
