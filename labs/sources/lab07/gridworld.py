import numpy as np


class Gridworld:
    def __init__(self, height, width, goal_position=None, walls=[], traps=[]):
        self.height = height
        self.width = width

        # copy goal_position or select randomly
        # cannot be in the same position as a wall or trap
        self.goal_position = goal_position

        self.walls = walls
        self.traps = traps

        while self.goal_position is None:
            goal_x = np.random.randint(1, self.width - 1)
            goal_y = np.random.randint(1, self.height - 1)
            self.goal_position = (goal_y, goal_x)
            if self.goal_position in self.walls or self.goal_position in self.traps:
                self.goal_position = None

    def reset(self):
        # generate a random position
        # check if position is empty
        self.agent_position = None
        while self.agent_position is None:
            agent_x = np.random.randint(1, self.width - 1)
            agent_y = np.random.randint(1, self.height - 1)
            self.agent_position = (agent_y, agent_x)
            if (self.agent_position in self.walls or self.agent_position in self.traps or self.agent_position == self.goal_position):
                self.agent_position = None

        return self.agent_position

    def calculate_reward(self, new_state):
        # 10 if agent reached goal
        # -10 if agent is in trap
        # -1 for all other steps
        if new_state == self.goal_position:
            return 10
        if new_state in self.traps:
            return -10
        return - 1

    def is_done(self):
        if self.agent_position == self.goal_position:
            return True
        if self.agent_position in self.traps:
            return True
        return False

    def step(self, action):
        # new state, reward, done, info
        # N - 0, E - 1, S - 2, W - 3
        agent_y, agent_x = self.agent_position
        if action == 0:
            agent_y -= 1
        elif action == 1:
            agent_x += 1
        elif action == 2:
            agent_y += 1
        elif action == 3:
            agent_x -= 1
        else:
            raise ValueError('Unknown action', action)

        if agent_x != 0 and agent_x != self.width - 1 and agent_y != 0 and agent_y != self.height - 1 and (agent_y, agent_x) not in self.walls:
            self.agent_position = (agent_y, agent_x)

        reward = self.calculate_reward(self.agent_position)

        done = self.is_done()

        info = dict()

        return self.agent_position, reward, done, info

    def render(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if y in [0, self.height - 1] or x in [0, self.width - 1]:
                    row += "#"
                elif (y, x) in self.walls:
                    row += "#"
                elif (y, x) in self.traps:
                    row += "O"
                elif (y, x) == self.goal_position:
                    row += "X"
                else:
                    row += " "
            # row += "\n"
            print(row)


if __name__ == '__main__':
    # #####
    # #O O#
    # #   #
    # # #X#
    # #####
    world = Gridworld(
        height=5,
        width=5,
        goal_position=(3, 3),
        walls=[(3, 2)],
        traps=[(1, 1), (1, 3)]
    )
    state = world.reset()
    done = False
    while not done:
        action = np.random.randint(0, 4)
        new_state, reward, done, _ = world.step(action)
        print("{} - {} -> {}; reward {}; done {}".format(state, action, new_state, reward, done))
        state = new_state
