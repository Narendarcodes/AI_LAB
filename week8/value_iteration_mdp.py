# Week 8: Value Iteration

import numpy as np

class GridWorldMDP:
    def __init__(self, size, goal, trap):
        self.size = size
        self.goal = goal
        self.trap = trap
        self.states = [(i, j) for i in range(size) for j in range(size)]
        self.actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    def get_next_state(self, state, action):
        i, j = state

        if action == 'UP':
            i -= 1
        elif action == 'DOWN':
            i += 1
        elif action == 'LEFT':
            j -= 1
        elif action == 'RIGHT':
            j += 1

        i = max(0, min(i, self.size - 1))
        j = max(0, min(j, self.size - 1))

        return (i, j)

    def reward(self, state):
        if state == self.goal:
            return 0
        elif state == self.trap:
            return -10
        return -1


def value_iteration(mdp, gamma=0.9, epsilon=0.01):
    V = {s: 0 for s in mdp.states}

    while True:
        delta = 0
        new_V = V.copy()

        for state in mdp.states:
            if state == mdp.goal or state == mdp.trap:
                continue

            values = []
            for action in mdp.actions:
                next_state = mdp.get_next_state(state, action)
                r = mdp.reward(next_state)
                values.append(r + gamma * V[next_state])

            new_V[state] = max(values)
            delta = max(delta, abs(V[state] - new_V[state]))

        V = new_V

        if delta < epsilon:
            break

    return V


# Run
mdp = GridWorldMDP(3, (2, 2), (1, 1))
values = value_iteration(mdp)

print("Value Iteration Output:")
for s in values:
    print(s, ":", values[s])