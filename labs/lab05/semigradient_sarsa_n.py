import numpy as np
import random

from typing import Optional, Callable
type State = int
type Action = int
type QValue = float
type NDArray = np._typing.NDArray


class Policy():
    def __init__(self, actions: list[Action], epsilon: float, **kwargs):

        self.actions = actions
        self.epsilon = epsilon

    def _best_action(self, qvalues: list[QValue]) -> Action:

        best_action = max(zip(self.actions[:], qvalues[:]),
                          key=lambda x: x[1])[0]
        return best_action

    def get_distribution(self, qvalues: list[QValue]) -> list[float]:

        distribution = [self.epsilon / len(qvalues) for _ in qvalues]
        action = self._best_action(qvalues)
        distribution[action] += 1 - self.epsilon
        return distribution

    def stochastic_policy(self, qvalues: list[QValue]) -> Action:

        probs = self.get_distribution(qvalues)
        [action] = random.choices(self.actions, probs)
        return action

    def deterministic_policy(self, qvalues: list[QValue]) -> Action:

        best_action = self._best_action(qvalues)
        return best_action


class QValueFunction():
    def __init__(self, num_features: int, num_actions: int, alpha: float,**kwargs):

        self.num_actions = num_actions
        self.alpha = alpha
        self.weights = np.zeros((self.num_actions, num_features))

    def get_values(self, state: State) -> list[QValue]:

        qvalues = [self.get_value(state, a) for a in range(self.num_actions)]
        return qvalues

    def get_value(self, state: State, action: Action) -> QValue:

        qvalue = self.weights[action].dot(state)
        return qvalue

    def update(self, state: State, action: Action, value: float) -> None:

        delta = value - self.get_value(state, action)
        self.weights[action] += self.alpha * delta * state


def get_feature_generator(env: object, granularity: list[int]) -> tuple[Callable, int]:

    low_limits = env.observation_space.low
    high_limits = env.observation_space.high

    bin_separators = [
        np.linspace(low_limits[i], high_limits[i], granularity[i]+1)
        for i in range(env.observation_space.shape[0])
    ]
    bins = [list(zip(s[:-1],s[1:])) for s in bin_separators]

    def feature_generator(state: list[float]) -> NDArray:

        features_code = []
        for feature_value, feature_bins in zip(state, bins):
            code = [
                1.0 if bin[0] <= feature_value <= bin[1] else 0.0
                for bin in feature_bins
            ]
            features_code += code

        return np.array(features_code, dtype=np.float32)

    return feature_generator, sum(granularity)


class SemiSarsaN():
    def __init__(self, env: object, gamma: float, n: int, granularity: list[int],
                 **kwargs):

        self.gamma = gamma
        self.n = n

        self.actions = list(range(env.action_space.n))

        self.code, code_length = get_feature_generator(env, granularity)

        self.policy = Policy(self.actions, **kwargs)

        self.qfunction =  QValueFunction(code_length, len(self.actions), **kwargs)

        self.buffer = []

    def _train(self) -> tuple[float, bool]:

        state1, action1, reward, _, done = self.buffer[0]
        target = reward
        for i in range(self.n - 1):
            if done:
                break
            _, _, next_reward, _, done = self.buffer[i+1]
            target += next_reward * self.gamma ** (i+1)

        if not done:
            state2, action2, _, _, _ = self.buffer[self.n]
            q_state = self.qfunction.get_value(self.code(state2), action2)
            target += self.gamma ** self.n * q_state

        self.qfunction.update(self.code(state1), action1, target)

        self.buffer = self.buffer[1:]

        return reward, self.buffer == []

    def _generate_step(self, env: object, state: State) -> None:

        action = self.predict(state, deterministic = False)
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        self.buffer.append((state, action, reward, next_state, done))

    def _generate_data(self, env: object, reset_opt: dict) -> None:

        if self.buffer == []:
            state, _ = env.reset(options=reset_opt)
            for _ in range(self.n):
                self._generate_step(env, state)
                _, _, _, state, done = self.buffer[-1]
                if done:
                    break

        _, _, _, state, done = self.buffer[-1]
        if not done:
            self._generate_step(env, state)

    def learn(self,
              env: object,
              num_episodes: int,
              reset_opt: Optional[dict] = {}) -> list[float]:

        rewards = list()

        for _ in range(num_episodes):

            episode_reward = 0
            episode_done = False

            while not episode_done:
                self._generate_data(env, reset_opt)
                reward, episode_done = self._train()
                episode_reward += reward

            rewards.append(episode_reward)

        return rewards

    def predict(self, state: State, deterministic: bool = True) -> Action:

        qvalues = [
            self.qfunction.get_value(self.code(state), action)
            for action in self.actions
        ]

        if deterministic == True:
            action = self.policy.deterministic_policy(qvalues)
        else:
            action = self.policy.stochastic_policy(qvalues)

        return action
