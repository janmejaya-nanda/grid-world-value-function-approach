import time
import tkinter as tk

from agent import Agent
from parameters import BLOCK_STATES, TERMINAL_STATES, NUMBER_OF_STATES
from utils import convert_coordinate_to_state, convert_state_to_coordinate


class GridWorld(object):
    def __init__(self):
        self.frame = tk.Canvas(bg='black', height=400, width=500)
        self.frame.pack()

        self.agent = Agent()
        self.episodes = 0

        self.create_gridworld()

    def create_gridworld(self):
        self.frame.create_rectangle(30, 30, 470, 360, fill='black')
        self.frame.create_rectangle(360, 30, 470, 140, fill='sea green')
        self.frame.create_rectangle(140, 140, 250, 250, fill='grey')
        self.frame.create_rectangle(360, 140, 470, 250, fill='red')
        self.frame.create_line(370, 40, 460, 40, 460, 130, 370, 130, 370, 40, fill='white', width=2)

        # terminal state rewards text
        self.frame.create_text(415, 85, text=1, font="Verdana 10 bold", fill='white')
        self.frame.create_text(415, 195, text=-1, font="Verdana 10 bold", fill='white')
        # Annotating States
        self.frame.create_text(45, 260, text='S0', font="Verdana 10 bold", fill='white', tag='states')
        self.frame.create_text(45, 150, text='S1', font="Verdana 10 bold", fill='white', tag='states')
        self.frame.create_text(45, 40, text='S2', font="Verdana 10 bold", fill='white', tag='states')
        self.frame.create_text(155, 260, text='S3', font="Verdana 10 bold", fill='white', tag='states')
        self.frame.create_text(155, 40, text='S5', font="Verdana 10 bold", fill='white', tag='states')
        self.frame.create_text(265, 260, text='S6', font="Verdana 10 bold", fill='white', tag='states')
        self.frame.create_text(265, 150, text='S7', font="Verdana 10 bold", fill='white', tag='states')
        self.frame.create_text(265, 40, text='S8', font="Verdana 10 bold", fill='white', tag='states')
        self.frame.create_text(375, 260, text='S9', font="Verdana 10 bold", fill='white', tag='states')
        # Annotating state values
        self.frame.create_text(415, 305, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        self.frame.create_text(305, 85, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        self.frame.create_text(305, 195, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        self.frame.create_text(305, 305, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        self.frame.create_text(195, 85, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        # self.frame.create_text(195, 195, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        self.frame.create_text(195, 305, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        self.frame.create_text(85, 85, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        self.frame.create_text(85, 195, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        self.frame.create_text(85, 305, text=0, font="Verdana 10 bold", fill='white', tag='state_value_text')
        # episode text
        self.frame.create_text(195, 0, text='Episode No: {0}'.format(self.episodes), font="Verdana 10 bold",
                               fill='white', tag='episode_text')

        self.frame.create_line(28, 30, 470, 30, 470, 360, 30, 360, 30, 30, fill='white', width=5)
        self.frame.create_line(30, 140, 470, 140, fill='white', width=2)
        self.frame.create_line(30, 250, 470, 250, fill='white', width=2)
        self.frame.create_line(140, 30, 140, 360, fill='white', width=2)
        self.frame.create_line(250, 30, 250, 360, fill='white', width=2)
        self.frame.create_line(360, 30, 360, 360, fill='white', width=2)
        self.frame.create_line(370, 150, 460, 150, 460, 240, 370, 240, 370, 150, fill='white', width=2)
        self.agent_coords = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
        self.frame.update()
        time.sleep(30)

    def reset_agent_coords(self):
        self.frame.delete(self.agent_coords)
        self.agent_coords = self.frame.create_oval(70, 290, 100, 320, fill='cyan')
        self.frame.update()

    def update_state_value_text(self):
        state_value = self.agent.get_states_value()
        self.frame.delete('state_value_text')
        self.frame.delete('episode_text')

        for state, value in enumerate(state_value):
            if state in BLOCK_STATES + TERMINAL_STATES:
                continue

            coord = convert_state_to_coordinate(state=state)
            self.frame.create_text(coord[0] + 15, coord[1] + 15, text=round(value, 2),
                                   font="Verdana 10 bold", fill='white', tag='state_value_text')
            self.frame.create_text(230, 10, text='Episode No: {0}'.format(self.episodes), font="Verdana 10 bold",
                                   fill='white', tag='episode_text')
            self.frame.update()

    def run(self):
        while True:
            time.sleep(0.03)
            current_state_coords = self.frame.coords(self.agent_coords)
            current_state = convert_coordinate_to_state(coord=current_state_coords)
            next_state = self.agent.get_next_state(current_state=current_state)
            if next_state in BLOCK_STATES:
                next_state = current_state

            if next_state != current_state:
                reward = self.agent.get_reward(state=next_state)
                self.agent.train(current_state=current_state, reward=reward, next_state=next_state)

            next_state_coords = convert_state_to_coordinate(state=next_state)
            self.frame.move(self.agent_coords, next_state_coords[0] - current_state_coords[0], next_state_coords[1] -
                            current_state_coords[1])
            self.frame.update()

            if next_state in TERMINAL_STATES:
                time.sleep(0.5)
                self.reset_agent_coords()
                self.episodes += 1
                print('{0} Episodes Completed'.format(self.episodes))

            self.update_state_value_text()
            self.agent.update_epsilon()

        tk.mainloop()

if __name__ == '__main__':
    GridWorld().run()
