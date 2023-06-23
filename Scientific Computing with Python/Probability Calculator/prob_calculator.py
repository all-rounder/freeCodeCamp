import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        self.contents_copy = []
        for key, val in balls.items():
            print(key, val)
            for _ in range(val):
                self.contents.append(key)
        print("init:", self.contents)

    def draw(self, num):
        self.contents_copy = self.contents.copy()
        drawn_balls = []
        length = len(self.contents)

        if num >= length:
            return self.contents

        for i in range(num):
            position = (random.randint(1, length - i))
            drawn_balls.append(self.contents[position - 1])
            # print(i + 1, "time draw:", position, "is", self.contents[position - 1])
            del self.contents[position - 1]
            # print("after draw:", self.contents)

        print("drawn_balls:", drawn_balls)
        return drawn_balls

    def reset(self):
        self.contents = self.contents_copy


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    success = 0
    for i in range(num_experiments):
        print(i + 1, "time draw" + "-" * 30)
        drawn_balls = hat.draw(num_balls_drawn)
        hat.reset()
        if match_balls(expected_balls, drawn_balls):
            success += 1

    probability = success / num_experiments
    print("probability", probability)
    return probability


def match_balls(expected_balls, drawn_balls):
    sorted_drawn_balls = {}
    for i in drawn_balls:
        if i not in sorted_drawn_balls:
            sorted_drawn_balls[i] = 1
        else:
            sorted_drawn_balls[i] += 1
    print("sorted_drawn_balls:", sorted_drawn_balls)

    length = len(expected_balls)
    match_times = 0
    for key, value in expected_balls.items():
        if key in sorted_drawn_balls and value <= sorted_drawn_balls[key]:
            match_times += 1
    if match_times == length:
        print("match_balls: True")
        return True
    else:
        print("match_balls: False")
        return False


# hat = Hat(blue=3, red=2, green=6)
# hat.draw(4)
# check_balls(expected_balls={"blue": 2, "green": 1}, drawn_balls=hat.draw(4))
# probability = experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
