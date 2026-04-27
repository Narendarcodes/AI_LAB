# Week 7: Hidden Markov Model (Forward Algorithm)

states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']

start_prob = {
    'Rainy': 0.6,
    'Sunny': 0.4
}

transition_prob = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}

emission_prob = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

obs_sequence = ['walk', 'shop', 'clean']


def forward_algorithm():
    forward = []

    # Initialization
    f0 = {}
    for state in states:
        f0[state] = start_prob[state] * emission_prob[state][obs_sequence[0]]
    forward.append(f0)

    # Recursion
    for t in range(1, len(obs_sequence)):
        ft = {}
        for curr_state in states:
            prob = 0
            for prev_state in states:
                prob += forward[t - 1][prev_state] * transition_prob[prev_state][curr_state]
            ft[curr_state] = prob * emission_prob[curr_state][obs_sequence[t]]
        forward.append(ft)

    # Termination
    total_prob = sum(forward[-1][state] for state in states)
    return total_prob


print("Probability:", forward_algorithm())