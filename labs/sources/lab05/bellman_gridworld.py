from itertools import product

import numpy as np

A = np.identity(35)

# v_s11, v_s12, v_s22, v_s23, v_s31, v_s32, v_s33
#    -7,    -6,    -5,    -4,    -3,    -2,    -1
A[0][-7] = -0.8
A[1][-6] = -0.8
A[3][-7] = -0.8

A[4][-6] = -0.8
A[6][-5] = -0.8
A[7][-7] = -0.8

A[8][-6] = -0.8
A[9][-4] = -0.8
A[10][-2] = -0.8

A[13][-4] = -0.8
A[14][-1] = -0.8
A[15][-5] = -0.8

A[17][-2] = -0.8
A[18][-3] = -0.8
A[19][-3] = -0.8

A[20][-5] = -0.8
A[21][-1] = -0.8
A[22][-2] = -0.8
A[23][-3] = -0.8

A[24][-4] = -0.8
A[25][-1] = -0.8
A[26][-1] = -0.8
A[27][-2] = -0.8

B = np.array([
    -1.0, -1.0, -10.0, -1.0,
    -1.0, 10.0, -1.0, -1.0,
    -1.0, -1.0, -1.0, -10.0,
    10.0, -1.0, -1.0, -1.0,
    -10.0, -1.0, -1.0, -1.0,
    -1.0, -1.0, -1.0, -1.0,
    -1.0, -1.0, -1.0, -1.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
])


all_combinations = list(product(
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2, 3]
))

for combination in all_combinations:
    A_copy = np.copy(A)
    for i in range(-len(combination), 0, 1):
        action_id = (i + 7) * 4 + combination[i]
        A_copy[i][action_id] = -1.0

    X = np.linalg.solve(A_copy, B)
    solution = True
    for state in range(7):
        start = state * 4
        end = start + 4
        state_id = -7 + state
        # print("({};{}) {}".format(start, end, state_id))
        # print(X[start:end], X[state_id])
        if abs(np.max(X[start:end]) - X[state_id]) > 1e-10:
            solution = False
            continue

    if solution:
        for idx, s in enumerate([0, 1, 4, 5, 6, 7, 8]):
            print("V(s{}) = {}".format(s, X[-7 + idx]))

        for s_idx, s in enumerate([0, 1, 4, 5, 6, 7, 8]):
            for a_idx, a in enumerate(['N', 'E', 'S', 'W']):
                print("Q(s{}, {}) = {}".format(
                    s, a, X[4 * s_idx + a_idx]
                ))
        break
