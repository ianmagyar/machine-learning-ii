import numpy as np

states = [0, 1, 2, 3, 4, 5, 6, 7, 8]
actions = [0, 1, 2, 3]
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

policy = np.zeros((N_STATES, N_ACTIONS), dtype=np.float32)
for s_idx in range(N_STATES):
    if s_idx != 2 and s_idx != 3:
        a = np.random.randint(0, N_ACTIONS)
        policy[s_idx][a] = 1.0

V = np.zeros(N_STATES)

count = 1
policy_stable = False
while not policy_stable:
    print("Iteration {}".format(count))
    count += 1
    keep_evaluating = True
    iteration = 1
    while keep_evaluating:
        # print("ITERATION {}".format(iteration))
        max_change = 0.0
        changes = list()
        for s in range(N_STATES):
            new_v = 0
            for action in actions:
                new_v += sum([policy[s, action] * P[s, action, s1] * (R[s, action, s1] + gamma * V[s1]) for s1 in range(N_STATES)])

            print("V(s{}) = {}".format(s, new_v))
            changes.append(abs(new_v - V[s]))
            V[s] = new_v
        # print("------")
        iteration += 1

        if max(changes) < theta:
            keep_evaluating = False

    # policy improvement
    policy_stable = True
    for s in range(N_STATES):
        if s == 2 or s == 3:
            print("State S{}: {}".format(s, policy[s]))
            continue
        old_policy = policy[s].copy()
        action_values = list()
        for action in actions:
            action_val = sum([P[s, action, s1] * (R[s, action, s1] + gamma * V[s1]) for s1 in range(N_STATES)])
            # print("State S{}, action {}: {}".format(s, action, action_val))
            action_values.append(action_val)
        new_policy = np.zeros((4,))
        new_policy[np.argmax(action_values)] = 1.0
        policy[s] = new_policy.copy()
        print("State S{}: {}".format(s, policy[s]))
        # print("{} vs {}: {}".format(old_policy, new_policy, (old_policy == new_policy).all()))
        if not (old_policy == new_policy).all():
            policy_stable = False
    print("-----")
