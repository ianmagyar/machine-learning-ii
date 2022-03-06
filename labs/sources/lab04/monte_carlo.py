import numpy as np

STATES = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
actions = ['N', 'E', 'S', 'W']
N_STATES = 9
N_ACTIONS = 4

P = np.zeros((N_STATES, N_ACTIONS, N_STATES))
R = np.full((N_STATES, N_ACTIONS, N_STATES), -1.0)

P[0, 0, 0] = 0.6
P[0, 0, 1] = 0.4
P[0, 1, 1] = 1.0
P[0, 2, 3] = 0.6
P[0, 2, 1] = 0.4
P[0, 3, 0] = 1.0

P[1, 0, 1] = 0.6
P[1, 0, 2] = 0.4
P[1, 1, 2] = 1.0
P[1, 2, 4] = 0.6
P[1, 2, 2] = 0.4
P[1, 3, 0] = 0.6
P[1, 3, 1] = 0.4

P[3, 0, 0] = 0.6
P[3, 0, 4] = 0.4
P[3, 1, 4] = 1.0
P[3, 2, 6] = 0.6
P[3, 2, 4] = 0.4
P[3, 3, 3] = 1.0

P[5, 0, 2] = 1.0
P[5, 1, 5] = 1.0
P[5, 2, 8] = 1.0
P[5, 3, 4] = 1.0

P[6, 0, 3] = 1.0
P[6, 1, 7] = 1.0
P[6, 2, 6] = 1.0
P[6, 3, 6] = 1.0

P[7, 0, 4] = 1.0
P[7, 1, 8] = 1.0
P[7, 2, 7] = 1.0
P[7, 3, 6] = 1.0

P[8, 0, 5] = 1.0
P[8, 1, 8] = 1.0
P[8, 2, 8] = 1.0
P[8, 3, 7] = 1.0

R[1, 1, 2] = 10.0
R[1, 0, 2] = 10.0
R[1, 2, 2] = 10.0
R[5, 0, 2] = 10.0

R[1, 2, 4] = -10.0
R[3, 0, 4] = -10.0
R[3, 1, 4] = -10.0
R[3, 2, 4] = -10.0
R[5, 3, 4] = -10.0
R[7, 0, 4] = -10.0

gamma = 0.8

policy = np.full((N_STATES, N_ACTIONS), 0.25)
Q = np.zeros((N_STATES, N_ACTIONS))
returns = dict()
epsilon = 0.1


episodes = [
    [(8, 1, -1.0), (8, 2, -1.0), (8, 1, -1.0), (8, 1, -1.0), (8, 1, -1.0), (8, 0, -1.0), (5, 1, -1.0), (5, 1, -1.0), (5, 0, 10.0)],
    [(8, 1, -1.0), (8, 1, -1.0), (8, 3, -1.0), (7, 3, -1.0), (6, 3, -1.0), (6, 3, -1.0), (6, 1, -1.0), (7, 2, -1.0), (7, 0, -10.0)],
    [(0, 2, -1.0), (1, 1, 10.0)],
    [(1, 0, -1.0), (1, 3, -1.0), (0, 3, -1.0), (0, 0, -1.0), (1, 1, 10.0)],
    [(6, 0, -1.0), (3, 1, -10.0)],
    [(0, 1, -1.0), (1, 0, 10.0)],
    [(5, 0, 10.0)],
    [(6, 0, -1.0), (3, 2, -1.0), (6, 3, -1.0), (6, 0, -1.0), (3, 0, -10.0)],
    [(8, 1, -1.0), (8, 0, -1.0), (5, 2, -1.0), (8, 0, -1.0), (5, 3, -10.0)],
    [(8, 0, -1.0), (5, 0, 10.0)]
]


def generate_episode():
    steps = list()
    state = np.random.choice([0, 1, 3, 5, 6, 7, 8])
    while state not in [2, 4]:
        action = np.random.choice(np.arange(N_ACTIONS), p=policy[state])
        weights = P[state, action]
        next_state = np.random.choice(STATES, p=weights)
        reward = R[state, action, next_state]
        steps.append((state, action, reward))
        state = next_state
    return steps


# episodes = [generate_episode() for _ in range(10)]
# print(episodes)

for i in range(len(episodes)):
    episode = episodes[i]
    print(episode)
    G = 0.0
    for i in reversed(range(len(episode))):
        state, action, reward = episode[i]
        G = gamma * G + reward
        if (state, action) not in [(x[0], x[1]) for x in episode[:i]]:
            if (state, action) in returns:
                returns[(state, action)].append(G)
            else:
                returns[(state, action)] = [G]

            state_returns = returns[(state, action)]
            Q[state][action] = sum(state_returns) / len(state_returns)

            best_action = np.argmax(Q[state])
            policy[state] = epsilon / N_ACTIONS
            policy[state][best_action] += 1 - epsilon

    print(returns)
    print(Q)

for s in range(N_STATES):
    print("S{}: {}".format(s, actions[np.argmax(policy[s])]))
