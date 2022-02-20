from itertools import product

import numpy as np

A = np.identity(35)

# v_s11, v_s12, v_s21, v_s23, v_s31, v_s32, v_s33
#    -7,    -6,    -5,    -4,    -3,    -2,    -1
A[0][-7] = -0.48   # s11, N
A[0][-6] = -0.32   # s11, N
A[1][-6] = -0.8    # s11, E
A[2][-6] = -0.32   # s11, S
A[2][-5] = -0.48   # s11, S
A[3][-7] = -0.8    # s11, W

A[4][-6] = -0.48   # s12, N
# A[5]               s12, E
# A[6]               s12, S
A[7][-7] = -0.48   # s12, W
A[7][-6] = -0.32   # s12, W

A[8][-7] = -0.48   # s21, N
# A[9]             # s21, E
A[10][-3] = -0.48  # s21, S
A[11][-5] = -0.8   # s21, W

# A[12]              s23, N
A[13][-4] = -0.8   # s23, E
A[14][-1] = -0.8   # s23, S
# A[15]              s23, W

A[16][-5] = -0.8   # s31, N
A[17][-2] = -0.8   # s31, E
A[18][-3] = -0.8   # s31, S
A[19][-3] = -0.8   # s31, W

# A[20]              s32, N
A[21][-1] = -0.8   # s32, E
A[22][-2] = -0.8   # s32, S
A[23][-3] = -0.8   # s32, W

A[24][-4] = -0.8   # s33, N
A[25][-1] = -0.8   # s33, E
A[26][-1] = -0.8   # s33, S
A[27][-2] = -0.8   # s33, W

B = np.array([
    -1.0, -1.0, -1.0, -1.0,
    3.4, 10.0, -2.0, -1.0,
    -4.6, -10.0, -4.6, -1.0,
    10.0, -1.0, -1.0, -10.0,
    -1.0, -1.0, -1.0, -1.0,
    -10.0, -1.0, -1.0, -1.0,
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
        print(X)
        print(combination)
        # break
