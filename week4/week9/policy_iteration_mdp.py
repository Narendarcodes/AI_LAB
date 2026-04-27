# Week 9: Policy Iteration

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


def policy_iteration(mdp, gamma=0.9):
    policy = {s: np.random.choice(mdp.actions) for s in mdp.states}
    V = {s: 0 for s in mdp.states}

    while True:
        # Policy Evaluation
        while True:
            delta = 0
            for state in mdp.states:
                if state == mdp.goal or state == mdp.trap:
                    continue

                action = policy[state]
                next_state = mdp.get_next_state(state, action)
                r = mdp.reward(next_state)

                new_v = r + gamma * V[next_state]
                delta = max(delta, abs(V[state] - new_v))
                V[state] = new_v

            if delta < 0.01:
                break

        # Policy Improvement
        stable = True
        for state in mdp.states:
            if state == mdp.goal or state == mdp.trap:
                continue

            old_action = policy[state]

            best_action = None
            best_value = float('-inf')

            for action in mdp.actions:
                next_state = mdp.get_next_state(state, action)
                r = mdp.reward(next_state)
                val = r + gamma * V[next_state]

                if val > best_value:
                    best_value = val
                    best_action = action

            policy[state] = best_action

            if old_action != best_action:
                stable = False

        if stable:
            break

    return policy, V


# Run
mdp = GridWorldMDP(3, (2, 2), (1, 1))
policy, values = policy_iteration(mdp)

print("Policy Iteration Output:")
for s in policy:
    print(s, "->", policy[s], "| Value:", values[s])