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


def main():
    shield = Shield()

    ENV_NAME = 'Car_RL4_noshield'

    steps = 10000
    # Get the environment and extract the number of actions.
    np.random.seed(123)
    env = Env()
    nb_actions = env.action_space.n
    #sys.exit()
    # Next, we build a very simple model.
    model = Sequential()
    model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
    model.add(Dense(20))
    model.add(Activation('relu'))
    model.add(Dense(20))
    model.add(Activation('relu'))
    model.add(Dense(20))
    model.add(Activation('relu'))
    # model.add(Dense(16))
    # model.add(Activation('relu'))
    model.add(Dense(nb_actions))
    model.add(Activation('linear'))
    #model.load_weights('Car_RL4_weights_cp.h5f')
    #print(model.summary())
    print "model initiated"
    # Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
    # even the metrics!
    memory = SequentialMemory(limit=500000, window_length=1)
    policy = BoltzmannQPolicy()
    dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
                   target_model_update=1e-2, policy=policy,shield=shield,maze=True)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])

    # Okay, now it's time to learn something! We visualize the training here for show, but this
    # slows down training quite a lot. You can always safely abort the training prematurely using
    # Ctrl + C.
    # dqn.load_weights('dqn_{}_weights.h5f'.format(ENV_NAME))
    score = 0
    fscore = 0
    counter = 0
    start=datetime.now()
    #env.render()
    while fscore <= 28000.0:
        counter += 1
        print 'fitting...'
        train_history = dqn.fit(env, nb_steps=steps, visualize=True, verbose=0)
        print 'testing...'
        # After training is done, we save the final weights.
        env.render()
        # Finally, evaluate our algorithm for 5 episodes.
        test_history = dqn.test(env, nb_episodes=1, visualize=True, verbose=0)
        score = np.mean(test_history.history['episode_reward'])
        print score
        if score > 28000:
            end = datetime.now()
            test_history = dqn.test(env, nb_episodes=1, visualize=True).history['episode_reward']
            fscore = np.mean(test_history)
            print score
            dqn.save_weights('{}_weights.h5f'.format(ENV_NAME), overwrite=True)
        else:
            fscore = 0
        env.render(mode=False)

    print('It took {} steps and {} seconds'.format(counter*steps,end-start))

if __name__ == '__main__':
    main()