import numpy as np


class QLearning:
    def __init__(self, env, learning_rate=0.2, discount_factor=0.8, epsilon=0.1):
        self.env = env
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon

        self.init_qtable()

    def init_qtable(self):
        self.actions = ['N', 'E', 'S', 'W']
        self.env_height, self.env_width = self.env.height, self.env.width

        self.q_table = np.zeros(
            (self.env_height, self.env_height, len(self.actions)))

    def train_episode(self):
        curr_pos = self.env.reset()

        while not self.env.is_done():
            action = self.propose_action(curr_pos)

            new_pos, reward, done, _ = self.env.step(action)

            # print("Moved from {} to {} (action {}) with reward {}"
            #       .format(curr_pos, new_pos, action, reward))

            self.learn(curr_pos, new_pos, action, reward)
            curr_pos = new_pos

    def train(self, episodes=1000):
        for _ in range(episodes):
            self.train_episode()

    def get_epsilon(self, state):
        return self.epsilon

    def propose_action(self, state):
        row = self.q_table[state]
        maxQ = np.max(row)

        if np.random.random() < self.get_epsilon(state):
            return np.random.randint(0, len(self.actions))

        indeces = np.where(row == maxQ)[0]
        if len(indeces) > 1:
            act = np.random.choice(indeces)
            return act
        else:
            return indeces[0]

    def compute_new_q_value(self, old_val, reward, next_value):
        return (old_val + self.learning_rate * (reward + self.discount_factor * next_value - old_val))

    def learn(self, old_state, new_state, action, reward):
        old_val = self.q_table[old_state][action]
        next_value = np.max(self.q_table[new_state])
        # print(old_state, action, reward, new_state)
        new_q_value = self.compute_new_q_value(old_val, reward, next_value)

        self.q_table[old_state][action] = new_q_value

    def print_values(self):
        height, width, _ = self.q_table.shape

        for r in range(1, height - 1):
            for c in range(1, width - 1):
                for a_id, a in enumerate(self.actions):
                    print("q(s{}{}, {}) = {:.3f}".format(
                        r, c, a, self.q_table[r, c, a_id]))
                print()


if __name__ == '__main__':
    from gridworld import Gridworld

    env = Gridworld(5, 5, goal_position=(1, 3), traps=[(2, 1)])
    env.render()

    agent = QLearning(env)
    agent.train(episodes=1000)

    agent.print_values()
