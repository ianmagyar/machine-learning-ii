import numpy as np


CODE_TO_INDEX = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
ACTIONS = ["N", "E", "S", "W"]


class Gridworld:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.states = np.arange(self.height * self.width)

        # copy goal_position or select randomly
        # cannot be in the same position as a wall or trap
        self.goal = 2

        self.trap = 4

        self.build_arrays()

    def build_arrays(self):
        N_STATES = self.height * self.width
        N_ACTIONS = 4
        self.P = np.zeros((N_STATES, N_ACTIONS, N_STATES))
        self.R = np.full((N_STATES, N_ACTIONS, N_STATES), -1.0)

        self.P[0, 0, 0] = 0.6
        self.P[0, 0, 1] = 0.4
        self.P[0, 1, 1] = 1.0
        self.P[0, 2, 3] = 0.6
        self.P[0, 2, 1] = 0.4
        self.P[0, 3, 0] = 1.0

        self.P[1, 0, 1] = 0.6
        self.P[1, 0, 2] = 0.4
        self.P[1, 1, 2] = 1.0
        self.P[1, 2, 4] = 0.6
        self.P[1, 2, 2] = 0.4
        self.P[1, 3, 0] = 0.6
        self.P[1, 3, 1] = 0.4

        self.P[3, 0, 0] = 0.6
        self.P[3, 0, 4] = 0.4
        self.P[3, 1, 4] = 1.0
        self.P[3, 2, 6] = 0.6
        self.P[3, 2, 4] = 0.4
        self.P[3, 3, 3] = 1.0

        self.P[5, 0, 2] = 1.0
        self.P[5, 1, 5] = 1.0
        self.P[5, 2, 8] = 1.0
        self.P[5, 3, 4] = 1.0

        self.P[6, 0, 3] = 1.0
        self.P[6, 1, 7] = 1.0
        self.P[6, 2, 6] = 1.0
        self.P[6, 3, 6] = 1.0

        self.P[7, 0, 4] = 1.0
        self.P[7, 1, 8] = 1.0
        self.P[7, 2, 7] = 1.0
        self.P[7, 3, 6] = 1.0

        self.P[8, 0, 5] = 1.0
        self.P[8, 1, 8] = 1.0
        self.P[8, 2, 8] = 1.0
        self.P[8, 3, 7] = 1.0

        self.R[:, :, self.goal] = 10.0  # set reward for reaching goal
        self.R[:, :, self.trap] = -10.0  # set reward for reaching trap

    def reset(self):
        # generate a random position
        # check if position is empty
        self.agent_position = np.random.randint(0, 9)
        while self.agent_position in [self.goal, self.trap]:
            self.agent_position = np.random.randint(0, 9)

        return self.agent_position

    def calculate_reward(self, state, action, new_state):
        # 10 if agent reached goal
        # -10 if agent is in trap
        # -1 for all other steps
        return self.R[state, action, new_state]

    def is_done(self):
        return self.agent_position in [self.goal, self.trap]

    def move_agent(self, state, action):
        if action not in [0, 1, 2, 3]:
            raise ValueError("Unknown action {}".format(action))

        weights = self.P[state, action]
        return np.random.choice(self.states, p=weights)

    def step(self, action):
        # new state, reward, done, info
        # N - 0, E - 1, S - 2, W - 3
        new_state = self.move_agent(self.agent_position, action)

        reward = self.calculate_reward(self.agent_position, action, new_state)

        self.agent_position = new_state
        done = self.is_done()

        info = dict()

        return self.agent_position, reward, done, info

    def render(self):
        print("#" * (self.width + 2))
        for y in range(self.height):
            line = "#"
            for x in range(self.width):
                state = y * self.width + x
                if state == self.goal:
                    line += "X"
                elif state == self.trap:
                    line += "O"
                else:
                    line += " "
            line += "#"
            print(line)
        print("#" * (self.width + 2))


if __name__ == '__main__':
    world = Gridworld()
    world.render()
    state = world.reset()
    done = False
    while not done:
        action = np.random.randint(0, 4)
        new_state, reward, done, _ = world.step(action)
        print("s{} - {} -> s{}; reward {}; done {}".format(
            CODE_TO_INDEX[state], ACTIONS[action],
            CODE_TO_INDEX[new_state], reward, done
        ))
        state = new_state
