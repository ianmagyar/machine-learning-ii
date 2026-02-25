class RiverCrossingEnv():

    action_space = None
    observation_space = None


    def __init__(self):
        pass


    def reset(self, *, seed = None, options = None):
        pass
        # return observation, info


    def step(self, action):
        pass
        # return observation, reward, terminated, truncated, info


    def render(self):
        pass


if __name__ == '__main__':
    env = RiverCrossingEnv()
    print(env)
