import random


class RiverCrossingEnv():

    action_space = type("Discrete", (), {"n":4})
    observation_space = type("Discrete", (), {"n":16})

    target_state = 15


    def __init__(self):

        self.current_state = None
        self.done = None


    @classmethod
    def _decode_state(self, state):

        farmer = state % 2
        state >>= 1
        wolf = state % 2
        state >>= 1
        goat = state % 2
        state >>= 1
        cabbage = state % 2

        return cabbage, goat, wolf, farmer


    @classmethod
    def _valid_state(self, state):

        cabbage, goat, wolf, farmer = self._decode_state(state)

        if farmer != wolf and wolf == goat:
            return False
        elif farmer != goat and goat == cabbage:
            return False
        else:
            return True


    def reset(self, *, seed = None, options = None):

        self.current_state = 0
        self.done = False

        observation = self.current_state
        return observation, {}


    @classmethod
    def _valid_action(self, state, action):

        cabbage, goat, wolf, farmer = self._decode_state(state)

        if action == 1:
            return farmer == wolf
        elif action == 2:
            return farmer == goat
        elif action == 3:
            return farmer == cabbage
        else:
            return True


    @classmethod
    def _bit_flip(self, pattern, bit):

        mask = 2 ** bit
        if pattern & mask > 0:
            return pattern - mask
        else:
            return pattern + mask


    @classmethod
    def _calculate_reward(self, old_state, new_state):

        if old_state == new_state:
            reward = -10
        elif self.target_state == new_state:
            reward = 10
        elif not self._valid_state(new_state):
            reward = -20
        else:
            reward = -1
        return reward


    def _change_state(self, old_state, action):

        new_state = self._bit_flip(old_state, action)
        if action > 0:
            new_state = self._bit_flip(new_state, 0)
        return new_state


    def step(self, action):

        old_state = self.current_state

        if self._valid_action(old_state, action):
            new_state = self._change_state(old_state, action)
            self.current_state = new_state
        else:
            new_state = old_state

        reward = self._calculate_reward(old_state, new_state)

        terminated = False
        if self.target_state == new_state:
            self.done = True
            terminated = True

        observation = self.current_state
        return observation, reward, terminated, False, {}


    def close(self):
        pass


if __name__ == '__main__':
    env = RiverCrossingEnv()

    observation, info = env.reset()
    print(f"{observation=}")

    end = False
    while not end:
        action = random.choice(range(env.action_space.n))
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            end = True
        print(f"{observation=},{reward=},{terminated=}")
    env.close()

