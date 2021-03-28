from gridworld import Gridworld


class MonteCarloAgent:
    def __init__(self, env, gamma=0.8, epsilon=0.1):
        pass

    def generate_episode(self):
        pass

    def train_on_episode(self, episode):
        pass

    def train(self, episodes=10):
        pass


if __name__ == '__main__':
    world = None
    # world = Gridworld()
    # world.render()
    agent = MonteCarloAgent(world)

    agent.train(episodes=1000)
