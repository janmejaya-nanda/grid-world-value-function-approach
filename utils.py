from parameters import COORDINATE_TO_STATE


def convert_coordinate_to_state(coord):
    """
    A Raw coordinate obtained from Tkinter Canvas coords object is converted into Agent's co-ordinate saved in params
    :param coord: A tuple(x, y) representing x, y coordinate of the agent
    :return: int: a number representing our internal state
    """
    agents_coord = (int(coord[0]), int(coord[1]))
    return COORDINATE_TO_STATE[agents_coord]


def convert_state_to_coordinate(state):
    state_to_coordinate = {COORDINATE_TO_STATE[key]: key for key in COORDINATE_TO_STATE}
    return state_to_coordinate[state]
