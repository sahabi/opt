import numpy as np
from maze import Env 
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from datetime import datetime
from safelearn2 import Shield

import argparse

parser = argparse.ArgumentParser(description='Car')
parser.add_argument("-c", "--collect-data", dest="collect_data_file", help="Provide a file for collecting convergence data")
parser.add_argument('-s', "--shield_options", dest='shield', help='Indicate whether a shield should be used or not', action='store_true', default=False)
parser.add_argument('-v', "--viz_options", dest='viz', help='Indicate whether to visualize or not', action='store_true', default=False)
parser.add_argument('-vv', "--vizviz_options", dest='all', help='Indicate whether to visualize training or not', action='store_true', default=False)
parser.add_argument('-n', "--negative-reward", dest='neg_reward', help='Indicated whether negative reward should be used for unsafe actions', action='store_true', default=False)
parser.add_argument('-m', "--manual", dest='manual', help='Indicated whether input is from user or agent', action='store_true', default=False)
parser.add_argument("--num-steps", dest='num_steps', help='Number of interactions', type=int, default=20)

args = parser.parse_args()
env_args = {}

if args.shield:
    shield = Shield()
    ENV_NAME = 'Car_Maze_shield'
    filename = 'reward-shielded.csv'

else:
    shield = None
    ENV_NAME = 'Car_Maze_noshield'
    filename = 'reward-noshield.csv'

if args.manual:
    filename = 'manual-' + filename

if args.viz:
    env_args['viz'] = True
    
env = Env(**env_args)
if args.manual or args.all:
    env.render(mode=True)
else:
    env.render(mode=False)
# Get the environment and extract the number of actions.
np.random.seed(123)
nb_actions = env.action_space.n

model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(20))
model.add(Activation('relu'))
model.add(Dense(20))
model.add(Activation('relu'))
model.add(Dense(20))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
memory = SequentialMemory(limit=500000, window_length=1)
policy = BoltzmannQPolicy()
if args.manual:
    dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
                   target_model_update=1e-2, policy=policy,shield=shield, maze=True, manual=True)
else:
    dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
                   target_model_update=1e-2, policy=policy,shield=shield, maze=True, manual=False)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])

print "model initiated"

steps = 10000
n_tests = int(args.num_steps)
target = open(filename, 'w')
for run in range(n_tests):
    print 'fitting... {}/{} \n'.format(run+1,n_tests+1)
    train_history = dqn.fit(env, nb_steps=steps, visualize=False, verbose=0)
    print 'testing...\n'
    env.render()
    test_history = dqn.test(env, nb_episodes=1, visualize=True, verbose=0)
    score = np.mean(test_history.history['episode_reward'])
    target.write(str(score))
    target.write("\n")
    if args.manual or args.all:
        env.render(mode=True)
    else:
        env.render(mode=False)
target.close()
>>>>>>> 866725ff857dcc90bf4872978aa59d95efa5cd32
