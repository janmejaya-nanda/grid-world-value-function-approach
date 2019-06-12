import random

from parameters import EPSILON_START, EPSILON_CHANGE_RATE, MINIMUM_EPSILON, ACTIONS, CURRENT_STATE_TO_NEXT_STATE
from value_network import ValueNetwork


class Agent(object):
    def __init__(self):
        self.epsilon = EPSILON_START
        self.value_network = ValueNetwork()

    def train(self, current_state, reward, next_state):
        self.value_network.train(current_state, reward, next_state)

    def get_reward(self, state):
        return self.value_network.get_reward(state)

    def get_next_state(self, current_state):
        if random.random() < self.epsilon:
            # explore
            print('RANDOM STATE ', random.choice(CURRENT_STATE_TO_NEXT_STATE[current_state]))
            return random.choice(CURRENT_STATE_TO_NEXT_STATE[current_state])
        else:
            # exploit
            print('EXploit Action ', )
            return self.value_network.get_best_next_state(current_state)

    def get_states_value(self):
        return self.value_network.state_value

    def update_epsilon(self):
        if self.epsilon - EPSILON_CHANGE_RATE > MINIMUM_EPSILON:
            self.epsilon -= EPSILON_CHANGE_RATE
        else:
            self.epsilon = MINIMUM_EPSILON
