import numpy as np

states = [0, 1, 2, 3, 4, 5, 6, 7, 8]
actions = ['N', 'E', 'S', 'W']
N_STATES = 9
N_ACTIONS = 4

P = np.zeros((N_STATES, N_ACTIONS, N_STATES))
R = np.full((N_STATES, N_ACTIONS, N_STATES), -1.0)

P[0, 0, 0] = 1.0
P[0, 1, 1] = 1.0
P[0, 2, 3] = 1.0
P[0, 3, 0] = 1.0

P[1, 0, 1] = 1.0
P[1, 1, 2] = 1.0
P[1, 2, 4] = 1.0
P[1, 3, 0] = 1.0

P[4, 0, 1] = 1.0
P[4, 1, 5] = 1.0
P[4, 2, 7] = 1.0
P[4, 3, 3] = 1.0

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

R[0, 2, 3] = -10.0
R[1, 1, 2] = 10.0
R[4, 3, 3] = -10.0
R[5, 0, 2] = 10.0
R[6, 0, 3] = -10.0

gamma = 0.8
theta = 1.0

V = np.zeros(N_STATES)

delta = 1.1  # so we can start the iteration
count = 0
while delta > theta:
    delta = 0.0
    print("Iteration {}".format(count))
    count += 1
    for s in range(N_STATES):
        prev_value = V[s]
        action_values = list()
        for action in range(N_ACTIONS):
            action_value = sum([P[s, action, s1] * (R[s, action, s1] + gamma * V[s1]) for s1 in range(N_STATES)])
            action_values.append(action_value)
            print("Q(S{}, {}) = {}".format(s, actions[action], action_value))
        V[s] = max(action_values)
        delta = max(delta, abs(prev_value - V[s]))

policy = np.zeros((N_STATES, N_ACTIONS), dtype=float)
for s in range(N_STATES):
    action_values = list()
    for action in range(N_ACTIONS):
        action_value = sum([P[s, action, s1] * (R[s, action, s1] + gamma * V[s1]) for s1 in range(N_STATES)])
        action_values.append(action_value)
    best_action = np.argmax(action_values)
    policy[s][best_action] = 1.0

    print("π(s{}) = {}".format(s, actions[best_action]))
