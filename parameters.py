class Move:
    up = 'up'
    down = 'down'
    left = 'left'
    right = 'right'

NUMBER_OF_STATES = 12
COORDINATE_TO_STATE = {
    (70, 290): 0,
    (180, 290): 3,
    (180, 180): 4,
    (290, 290): 6,
    (400, 290): 9,
    (70, 180): 1,
    (290, 180): 7,
    (400, 180): 10,
    (70, 70): 2,
    (180, 70): 5,
    (290, 70): 8,
    (400, 70): 11
}
CURRENT_STATE_TO_NEXT_STATE = {
    0: [1, 3],
    1: [2, 4],
    2: [5],
    3: [0, 4, 6],
    5: [2, 4, 8],
    6: [3, 7, 9],
    7: [4, 6, 10, 8],
    8: [11, 5, 7],
    9: [6, 10],
    10: [],
    11: []
}
BLOCK_STATES = [4]
TERMINAL_STATES = [10, 11]
ACTIONS = [Move.up, Move.down, Move.left, Move.right]

GAMMA = 0.8
LEARNING_RATE = 0.01
EPSILON_START = 0.5
EPSILON_CHANGE_RATE = 1e-5
MINIMUM_EPSILON = 0.05
