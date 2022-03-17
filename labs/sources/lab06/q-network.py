import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.learning_rate = 0.001
        self.gamma = 0.95

        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995

        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def act(self, state):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        if np.random.rand() < self.epsilon:
            return np.random.randint(self.action_size)

        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def learn(self, state, action, reward, next_state, done):
        target = reward
        if not done:
            target += self.gamma * np.amax(self.model.predict(next_state)[0])

        target_out = self.model.predict(state)
        target_out[0][action] = target

        self.model.fit(state, target_out, epochs=1, verbose=0)


if __name__ == '__main__':
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    agent = DQNAgent(state_size, action_size)

    episodes = 50
    for e in range(episodes):
        state = env.reset()
        state = np.expand_dims(state, 0)

        for time_step in range(500):
            env.render()

            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)

            next_state = np.expand_dims(next_state, 0)

            agent.learn(state, action, reward, next_state, done)
            state = next_state

            if done:
                print("episode: {}/{}, score: {}".format(
                    e + 1, episodes, time_step))
                break
