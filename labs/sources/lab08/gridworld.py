import math

import numpy as np


class Gridworld:
    def __init__(self, height, width, goal_position=None, traps=[]):
        self.height = height
        self.width = width

        self.goal_position = goal_position
        self.traps = traps

        while self.goal_position is None:
            goal_x = np.random.uniform(0, self.width)
            goal_y = np.random.uniform(0, self.height)
            self.goal_position = (goal_y, goal_x)

            for trap in self.traps:
                if self.get_distance(self.goal_position, trap) < 1:
                    self.goal_position = None

        self.agent_position = None

    def get_distance(self, p1, p2):
        p1_y, p1_x = p1
        p2_y, p2_x = p2

        return math.sqrt((p1_x - p2_x) ** 2 + (p1_y - p2_y) ** 2)

    def reset(self):
        self.agent_position = None

        while self.agent_position is None:
            agent_x = np.random.uniform(0, self.width)
            agent_y = np.random.uniform(0, self.height)
            self.agent_position = (agent_y, agent_x)

            for check in self.traps + [self.goal_position]:
                if self.get_distance(self.agent_position, check) < 1:
                    self.agent_position = None
                    break

        return self.agent_position

    def calculate_reward(self, new_state):
        if self.get_distance(new_state, self.goal_position) < 1:
            return 10

        for trap in self.traps:
            if self.get_distance(new_state, trap) < 1:
                return -10

        return -1

    def is_done(self):
        for check in self.traps + [self.goal_position]:
            if self.get_distance(self.agent_position, check) < 1:
                return True

        return False

    def get_change(self, angle):
        return math.cos(angle), math.sin(angle)

    def step(self, action_angle):
        agent_y, agent_x = self.agent_position

        dx, dy = self.get_change(action_angle)

        new_y = max(min(agent_y + dy, self.height), 0)
        new_x = max(min(agent_x + dx, self.width), 0)

        self.agent_position = (new_y, new_x)

        reward = self.calculate_reward(self.agent_position)
        done = self.is_done()
        info = dict()

        return self.agent_position, reward, done, info

    def render(self):
        pass


if __name__ == '__main__':
    world = Gridworld(3, 3, goal_position=(3, 3), traps=[(2, 2)])

    state = world.reset()
    done = False
    while not done:
        action = np.random.choice([0, math.pi / 2, math.pi, -math.pi / 2])
        new_state, reward, done, _ = world.step(action)
        print("{} - {} -> {}; reward {}; done {}".format(state, action, new_state, reward, done))
        state = new_state
