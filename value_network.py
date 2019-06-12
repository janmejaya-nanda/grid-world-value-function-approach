import numpy as np

from parameters import NUMBER_OF_STATES, LEARNING_RATE, GAMMA, CURRENT_STATE_TO_NEXT_STATE
from parameters import TERMINAL_STATES
from parameters import BLOCK_STATES


class ValueNetwork(object):
    def __init__(self):
        self._reset_network()

    def _reset_network(self):
        self.state_value = np.zeros([NUMBER_OF_STATES])
        self.state_reward = np.zeros([NUMBER_OF_STATES])

        for state in TERMINAL_STATES + BLOCK_STATES:
            self.state_value[state] = 0
        self.state_reward[10] = -1
        self.state_reward[11] = 1

    def train(self, current_state, reward, next_state):
        assert current_state not in TERMINAL_STATES + BLOCK_STATES

        # Value Update Rule
        self.state_value[current_state] += LEARNING_RATE * (
            reward + GAMMA * self.state_value[next_state] - self.state_value[current_state]
        )

    def get_reward(self, state):
        return self.state_reward[state]

    def get_best_next_state(self, current_state):
        possible_next_states = CURRENT_STATE_TO_NEXT_STATE[current_state]
        best_next_state_value = np.max(self.state_value[possible_next_states])
        best_value_states = np.where(self.state_value == best_next_state_value)[0]
        next_states_with_highest_value = [state for state in best_value_states if state in possible_next_states]
        return next_states_with_highest_value[0]

