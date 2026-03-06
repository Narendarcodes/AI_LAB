import math

# Possible actions
attacks = {
    "Phishing": -2,
    "Malware": -3,
    "DDoS": -4
}

defenses = {
    "Firewall": 2,
    "Security Training": 1,
    "Patch Update": 3
}

# Evaluate system security
def evaluate(security_score):
    return security_score

# Minimax function
def minimax(depth, security_score, is_attacker):

    # Stop condition
    if depth == 0 or security_score <= 0 or security_score >= 10:
        return evaluate(security_score)

    # Attacker tries to minimize security
    if is_attacker:
        best = math.inf

        for attack, impact in attacks.items():
            new_score = security_score + impact
            score = minimax(depth-1, new_score, False)
            best = min(best, score)

        return best

    # Defender tries to maximize security
    else:
        best = -math.inf

        for defense, impact in defenses.items():
            new_score = security_score + impact
            score = minimax(depth-1, new_score, True)
            best = max(best, score)

        return best


# Choose best move
def best_attack(security_score):
    best_val = math.inf
    best_move = None

    for attack, impact in attacks.items():
        new_score = security_score + impact
        value = minimax(3, new_score, False)

        if value < best_val:
            best_val = value
            best_move = attack

    return best_move


def best_defense(security_score):
    best_val = -math.inf
    best_move = None

    for defense, impact in defenses.items():
        new_score = security_score + impact
        value = minimax(3, new_score, True)

        if value > best_val:
            best_val = value
            best_move = defense

    return best_move


# Simulation
def simulate():

    security_score = 5

    print("Initial System Security Score:", security_score)

    for turn in range(5):

        attack = best_attack(security_score)
        security_score += attacks[attack]
        print("\nAttacker uses:", attack)
        print("Security score:", security_score)

        if security_score <= 0:
            print("System Compromised!")
            break

        defense = best_defense(security_score)
        security_score += defenses[defense]
        print("Defender uses:", defense)
        print("Security score:", security_score)

        if security_score >= 10:
            print("System Fully Secured!")
            break


simulate()