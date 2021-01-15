import copy
import random
from collections import Counter


class Hat:

    def __init__(self, **kwargs):
        contents = []
        for key, value in kwargs.items():
            for x in range(value):
                contents += key.split()
        self.contents = contents

    def draw(self, draw_number):
        draw_list = []
        contents = self.contents
        if draw_number >= len(contents):
            return contents
        for i in range(draw_number):
            choice = random.choice(contents)
            contents.remove(choice)
            draw_list.append(choice)
        self.contents = contents
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_list = []

    for key, value in expected_balls.items():
        for x in range(value):
            expected_list += key.split()
    m = 0
    for n in range(num_experiments):
        trial = copy.deepcopy(hat)
        draw = trial.draw(num_balls_drawn)
        result = list((Counter(expected_list) - Counter(draw)).elements())
        if not result:
            m += 1
    probability = m / num_experiments
    return probability
