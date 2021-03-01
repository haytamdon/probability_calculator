import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for arg in kwargs:
            self.contents.extend(((arg + ' ') * kwargs[arg]).split(" ")[:kwargs[arg]])

        if not kwargs:
            self.contents.append(self.getSillyColorSelectionFromNothing())

    def getSillyColorSelectionFromNothing(self):
        return ["yellow", "blue", "red", "green", "orange", "black", "pink", "striped"][random.randint(0, 7)]

    def draw(self, num):
        drawn = []
        rints = []
        for i in range(num if num < (len(self.contents)) else len(self.contents)):
            rint = random.randint(0, len(self.contents) - 1)
            drawn.append(self.contents.pop(rint))
            rints.append(rint)
        return drawn

    def resetBalls(self, balls):
        self.contents.clear()
        self.contents.extend(balls)

    def getNumBalls(self):
        return len(self.contents)


def isGreater(d1, d2):
    for key in d1:
        if d2.get(key, 0) < d1[key]:
            return False

    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    foundit = 0
    orig = copy.deepcopy(hat.contents)
    for i in range(num_experiments):
        if hat.getNumBalls() < num_balls_drawn:
            hat.resetBalls(orig)
        drawn = hat.draw(num_balls_drawn)
        d = {}
        for ball in drawn:
            d[ball] = d.get(ball, 0) + 1
        if isGreater(expected_balls, d):
            foundit += 1
    return foundit / num_experiments

hat = Hat(blue=4, red=2, green=6)
probability = experiment(hat=hat, expected_balls={"blue": 2,"red": 1}, num_balls_drawn=4, num_experiments=3000)
print("Probability:", probability)