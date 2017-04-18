'''
OpenAI-Gym Cartpole-v0 LSTM experiment
Giuseppe Bonaccorso (http://www.bonaccorso.eu)
'''

import gym
import numpy as np
import time

from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
from keras import backend as K

# Result location
result_location = 'D://ml_data//cartpole-lstm-1'

# Number of episodes
nb_episodes = 100

# Max execution time (in seconds)
max_execution_time = 120

# Set random seed
np.random.seed(1000)


class CartPoleController(object):
    def __init__(self, n_input=4, n_hidden=10, n_output=1, initial_state=0.1, training_threshold=1.5):
        self.n_input = n_input
        self.n_hidden = n_hidden
        self.n_output = n_output
        self.initial_state = initial_state
        self.training_threshold = training_threshold
        self.step_threshold = 0.5

        # Action neural network
        # Dense input -> (1 x n_input)
        # LSTM -> (n_hidden)
        # Dense output -> (n_output)
        self.action_model = Sequential()

        self.action_model.add(LSTM(self.n_hidden, input_shape=(1, self.n_input)))
        self.action_model.add(Activation('tanh'))
        self.action_model.add(Dense(self.n_output))
        self.action_model.add(Activation('sigmoid'))

        self.action_model.compile(loss='mse', optimizer='adam')

    def action(self, obs, prev_obs=None, prev_action=None):
        x = np.ndarray(shape=(1, 1, self.n_input)).astype(K.floatx())

        if prev_obs is not None:
            prev_norm = np.linalg.norm(prev_obs)

            if prev_norm > self.training_threshold:
                # Compute a training step
                x[0, 0, :] = prev_obs

                if prev_norm < self.step_threshold:
                    y = np.array([prev_action]).astype(K.floatx())
                else:
                    y = np.array([np.abs(prev_action - 1)]).astype(K.floatx())

                self.action_model.train_on_batch(x, y)

        # Predict new value
        x[0, 0, :] = obs
        output = self.action_model.predict(x, batch_size=1)

        return self.step(output)

    def step(self, value):
        if value > self.step_threshold:
            return int(1)
        else:
            return int(0)


if __name__ == '__main__':
    print('OpenAI-Gym CartPole-v0 LSTM experiment')

    env = gym.make('CartPole-v0')
    cart_pole_controller = CartPoleController()

    total_reward = []

    for episode in range(nb_episodes):
        # Reset environment
        observation = env.reset()
        previous_observation = observation

        action = cart_pole_controller.action(observation)
        previous_action = action

        done = False
        t = 0
        partial_reward = 0.0
        start_time = time.time()
        elapsed_time = 0

        while not done and elapsed_time < max_execution_time:
            t += 1
            elapsed_time = time.time() - start_time

            env.render()
            observation, reward, done, info = env.step(action)
            partial_reward += reward

            action = cart_pole_controller.action(observation, previous_observation, previous_action)
            previous_observation = observation
            previous_action = action

        print('Episode %d finished after %d timesteps. Total reward: %1.0f. Elapsed time: %d s' %
              (episode+1, t+1, partial_reward, elapsed_time))

        total_reward.append(partial_reward)

    total_reward = np.array(total_reward)
    print('Average reward: %3.2f' % np.mean(total_reward))