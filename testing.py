import numpy as np
from env_road3 import Env 
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

ENV_NAME = 'Car_RL4'

steps = 5000
# Get the environment and extract the number of actions.
np.random.seed(123)
env = Env()
nb_actions = env.action_space.n
#sys.exit()
# Next, we build a very simple model.
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
# model.add(Dense(16))
# model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
model.load_weights('Car_RL4_weights.h5f')
print(model.summary())
env = Env(net=model)
# Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
# even the metrics!
memory = SequentialMemory(limit=500000, window_length=1)
policy = BoltzmannQPolicy()
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
               target_model_update=1e-2, policy=policy)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

# Okay, now it's time to learn something! We visualize the training here for show, but this
# slows down training quite a lot. You can always safely abort the training prematurely using
# Ctrl + C.
# dqn.load_weights('dqn_{}_weights.h5f'.format(ENV_NAME))
score = 0
fscore = 0
counter = 0
while counter < 80.0:
	counter += 1
	#train_history = dqn.fit(env, nb_steps=steps, visualize=False, verbose=2)
	# After training is done, we save the final weights.
	env.render()
	# Finally, evaluate our algorithm for 5 episodes.
	test_history = dqn.test(env, nb_episodes=1, visualize=True)

print('It took {} steps'.format(counter*steps))
