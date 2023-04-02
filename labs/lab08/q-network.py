from collections import deque
import math
import random

import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam

from gridworld import Gridworld


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.learning_rate = 0.001
        self.gamma = 0.95

        self.epsilon = 1.0
        self.epsilon_min = 0.1
        self.epsilon_decay = 0.999995

        self.model = self._build_model()
        self.target_model = self._build_model()
        # self.target_model.set_weights(self.model.get_weights())
        self.tau = 0.125

        self.memory = deque(maxlen=2000)

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        # model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def act(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.action_size)

        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def learn(self, state, action, reward, next_state, done):
        target = reward
        if not done:
            target += self.gamma * np.amax(self.target_model.predict(next_state)[0])

        target_out = self.model.predict(state)
        target_out[0][action] = target

        self.model.fit(state, target_out, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def train_target_network(self):
        weights = self.model.get_weights()
        target_weights = self.target_model.get_weights()
        for i in range(len(target_weights)):
            target_weights[i] = (
                self.tau * weights[i] + (1 - self.tau) * target_weights[i]
            )

        self.target_model.set_weights(target_weights)

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return

        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            self.learn(state, action, reward, next_state, done)


if __name__ == '__main__':
    world = Gridworld(3, 3, goal_position=(3, 3), traps=[(2, 2)])

    agent = DQNAgent(2, 4)
    ANGLES = [math.pi / 2, 0, -math.pi / 2, math.pi]

    episodes = 500
    batch_size = 32
    memory_length = 20
    last_results = deque(maxlen=memory_length)

    for e in range(episodes):
        state = world.reset()
        state = np.expand_dims(state, 0)

        for time_step in range(500):
            action = agent.act(state)
            angle = ANGLES[action]
            next_state, reward, done, _ = world.step(angle)

            next_state = np.expand_dims(next_state, 0)

            agent.remember(state, action, reward, next_state, done)
            state = next_state
            agent.replay(batch_size)

            if done:
                success = reward == 10
                last_results.append(success)
                print("episode: {}/{}, {:.2%} over last {} episodes".format(
                    e + 1, episodes, sum(last_results) / len(last_results),
                    memory_length))
                break

        if not done:
            last_results.append(False)
            print("episode: {}/{}, {:.2%} over last {} episodes".format(
                e + 1, episodes, sum(last_results) / len(last_results),
                memory_length))

        agent.train_target_network()
