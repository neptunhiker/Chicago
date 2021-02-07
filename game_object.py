import random

class Die:

    def __init__(self, color, nr_sides, material):
        self.color = color
        self.nr_sides = nr_sides
        self.material = material
        self.last_roll = None

    def roll(self):
        self.last_roll = random.randint(1, self.nr_sides)
        return self.last_roll

class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.last_result = None

    def calc_last_result(self, wuerfel_1, wuerfel_2, wuerfel_3, game):

        if game.count_ruling in ["h", "t"]:
            self.last_result = wuerfel_1 + wuerfel_2 + wuerfel_3
        elif game.count_ruling == "160":
            die_list = [wuerfel_1, wuerfel_2, wuerfel_3]
            converted_die_list = []
            for die in die_list:
                if die == 1:
                    die = 100
                elif die == 6:
                    die = 60
                else:
                    pass
                converted_die_list.append(die)
            self.last_result = sum(converted_die_list)
        else:
            raise Exception

class Game:

    def __init__(self):
        self.count_ruling = None
        self.round = 1
        self.turn = 1
        self.roll = 1
        self.max_rolls = 3
        self.nr_players = 2
        self.active_player = None
        self.go_on = True

    def change_active_player(self, p_1, p_2, cur_player):
        if cur_player == p_1:
            self.active_player = p_2
        elif cur_player == p_2:
            self.active_player = p_1
        else:
            raise Exception
        return self.active_player

    def reset(self):
        self.count_ruling = None
        self.turn = 1
        self.roll = 1
        self.max_rolls = 3









