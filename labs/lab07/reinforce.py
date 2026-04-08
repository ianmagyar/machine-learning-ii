import numpy as np
import random

from typing import Optional
type State = int
type Action = int
type QValue = float


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


class Reinforce():
    def __init__(self, env: object, gamma: float, n: int, **kwargs):

        self.gamma = gamma
        self.n = n

        self.actions = list(range(env.action_space.n))

        self.policy = Policy(self.actions, **kwargs)

        self.qfunction =  QValueFunction(env.observation_space.shape[0],
                                         len(self.actions), **kwargs)

        self.buffer = []

    def _train(self) -> tuple[float, bool]:

        if len(self.buffer) >= self.n+1 or self.buffer[-1][-1]:

            state1, action1, reward, _, done = self.buffer[0]
            target = reward
            for i in range(1, self.n):
                if done:
                    break
                _, _, next_reward, _, done = self.buffer[i]
                target += next_reward * self.gamma ** (i)

            if not done:
                state2, action2, _, _, _ = self.buffer[self.n]
                q_state = self.qfunction.get_value(state2, action2)
                target += self.gamma ** self.n * q_state

            self.qfunction.update(state1, action1, target)

            self.buffer = self.buffer[1:]

            episode_end = self.buffer == [] and done

        else:
            reward = 0
            episode_end = False

        return reward, episode_end

    def _generate_data(self, env: object, next_state: State) -> None:

        if next_state is None:
            state, _ = env.reset()
        else:
            state = next_state

        if self.buffer == [] or not self.buffer[-1][-1]:
            action = self.predict(state, deterministic = False)
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            self.buffer.append((state, action, reward, next_state, done))

        return next_state

    def learn(self,
              env: object,
              num_episodes: int,
              reset_opt: Optional[dict] = {}) -> list[float]:

        rewards = list()

        for e in range(num_episodes):

            episode_reward = 0
            episode_done = False

            last_state = None
            while not episode_done:
                last_state = self._generate_data(env, last_state)
                reward, episode_done = self._train()
                episode_reward += reward

            rewards.append(episode_reward)

            print(f"EPIZODE {e=} {episode_reward=}")

        return rewards

    def predict(self, state: State, deterministic: bool = True) -> Action:

        qvalues = [
            self.qfunction.get_value(state, action)
            for action in self.actions
        ]

        if deterministic == True:
            action = self.policy.deterministic_policy(qvalues)
        else:
            action = self.policy.stochastic_policy(qvalues)

        return action
