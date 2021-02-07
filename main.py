# Chicago - the game of three dice!

from game_object import Die, Player, Game
import random

def right_answer(answer_list):
    correct_answer = False
    while correct_answer is False:
        answer = input("\t> ")
        if answer in answer_list:
            correct_answer = True
        else:
            print("Unerwartete Eingabe. Bitte wähle aus " + str(answer_list))
    return answer

def next_step():
    rolls_left = chicago.max_rolls - chicago.roll
    print("\tDu kannst noch " + str(rolls_left) + " Mal würfeln. Was willst du tun? a-halten oder b-würfeln")
    answer_loc = right_answer(["a", "b", "würfeln", "halten"])
    return answer_loc


def roll_again(roll_1, roll_2, roll_3):
    roll_result = [roll_1, roll_2, roll_3]

    print("\tDeine Würfel zeigen:")
    print("\t" + str(roll_result))
    print("\tWelche der Würfel möchtest du neu werfen?")
    print("\ta) Würfel 1")
    print("\tb) Würfel 2")
    print("\tc) Würfel 3")
    print("\td) Würfel 1 und 2")
    print("\te) Würfel 1 und 3")
    print("\tf) Würfel 2 und 3")
    print("\tg) alle")

    answer = right_answer(["a", "b", "c", "d", "e", "f", "1", "2", "3", "1 und 2", "1 und 3", "2 und 3", "g", "alle"])
    if answer.lower() in ["a", "1"]:
        roll_1 = wuerfel_1.roll()
    elif answer.lower() in ["b", "2"]:
        roll_2 = wuerfel_2.roll()
    elif answer.lower() in ["c", "3"]:
        roll_3 = wuerfel_3.roll()
    elif answer.lower() in ["d", "1 und 2"]:
        roll_1 = wuerfel_1.roll()
        roll_2 = wuerfel_2.roll()
    elif answer.lower() in ["e", "1 und 3"]:
        roll_1 = wuerfel_1.roll()
        roll_3 = wuerfel_3.roll()
    elif answer.lower() in ["f", "2 und 3"]:
        roll_2 = wuerfel_2.roll()
        roll_3 = wuerfel_3.roll()
    elif answer.lower() in ["g", "alle"]:
        roll_1 = wuerfel_1.roll()
        roll_2 = wuerfel_2.roll()
        roll_3 = wuerfel_3.roll()
    else:
        raise Exception


    roll_result = [roll_1, roll_2, roll_3]  # liste
    print("\tDeine Würfel zeigen:")
    print("\t" + str(roll_result))
    return roll_result

def update(winner):
    winner.points += 1
    chicago.active_player = winner
    print("\t" + str(winner.name) + " gewinnt. Spielstand:")
    print("\t" + str(player_1.name) + " " + str(player_1.points) + ":" + str(player_2.points) + " " + str(player_2.name))

def finish_turn(player):
    print("\t" + str(player.name) + "'s Ergebis ist " + str(player.last_result) + " / " + chicago.count_ruling)
    print("\t--------------------")
    chicago.max_rolls = chicago.roll
    chicago.roll = 1
    chicago.change_active_player(player_1, player_2, player)

#----------Init----------------------------------------------------------------------------------------

wuerfel_1 = Die(color="green", nr_sides=6, material="wood")
wuerfel_2 = Die(color="red", nr_sides=6, material="wood")
wuerfel_3 = Die(color="red", nr_sides=6, material="wood")

chicago = Game()

player_1 = Player(name="Basti")
player_2 = Player(name="Addi-Yo")
chicago.active_player = player_1

# print(player_1.points)
# player_1.points = 5
# print(player_1.points)
# player_1.points = player_1.points+1
# print(player_1.points)
# player_1.points += 1
# print(player_1.points)
#----------Initiate the Game-------------------------------------------------------------------------------

print("\n@-@-@-@-@-@-@--Chicago--@-@-@-@-@-@-@ \n")
print("Lasst die Spiele beginnen \n")
#----------Initial Roll------------------------------------------------------------------------------------
while chicago.go_on:
    while chicago.turn < chicago.nr_players+1:
        if chicago.turn == 1:
            print ("---------- \nRunde " + str(chicago.round) + "\n")

        wuerfel_1.roll()
        wuerfel_2.roll()
        wuerfel_3.roll()

        print("\t" + str(chicago.active_player.name) + " ist am Zug und hat " + str(wuerfel_1.last_roll) + ", " + str(wuerfel_2.last_roll) + ", " + str(wuerfel_3.last_roll) + " gewürfelt.")

        #----------Decision Type------------------------------------------------------------------------------------

        if chicago.turn == 1:
            print("\tWähle: h-hoch, t-tief oder 160")
            chicago.count_ruling = right_answer(["h", "t", "160"])

        chicago.active_player.calc_last_result(wuerfel_1.last_roll, wuerfel_2.last_roll, wuerfel_3.last_roll, chicago)
        #----------roll phase----------------------------------------------------------------------------------------
        temp_player = chicago.active_player
        while chicago.active_player == temp_player:
            if chicago.roll == chicago.max_rolls:
                finish_turn(chicago.active_player)
            else:
                print("\tDu hast " + str(chicago.active_player.last_result) + " / " + chicago.count_ruling + ".")
                answer = next_step()

                if answer == "a":
                    finish_turn(chicago.active_player)
                elif answer == "b":
                    roll_result = roll_again(wuerfel_1.last_roll, wuerfel_2.last_roll, wuerfel_3.last_roll)
                    chicago.active_player.calc_last_result(wuerfel_1.last_roll, wuerfel_2.last_roll, wuerfel_3.last_roll, chicago)
                    chicago.roll += 1
                    if chicago.roll == chicago.max_rolls:
                        finish_turn(chicago.active_player)
                else:
                    raise Exception

        chicago.turn += 1

    #----------Determine Winner-----------------------------------------------------------------------------------

    if chicago.count_ruling in ["h", "160"]:
        if player_1.last_result >= player_2.last_result:
            update(player_1)
        else:
            update(player_2)
    elif chicago.count_ruling in ["t"]:
        if player_1.last_result <= player_2.last_result:
            update(player_1)
        else:
            update(player_2)
    else:
        raise Exception

    chicago.reset()
    chicago.round += 1

    print("\nNoch eine Runde? ja/nein")
    go_on=right_answer(["ja", "nein", "j", "n"])

    if go_on in ["ja", "j"]:
        pass
    elif go_on in ["nein", "n"]:
        chicago.go_on = False
        final = random.randint(1, 4)
        if final == 1:
            print("Sehr vernünftig. Glückspiel ist nur etwas für schwache Charaktere. Zurück an die Arbeit!\n")
        elif final == 2:
            print("Ohhhh schade. Es hat gerade angefangen richtig Spaß zu machen!\n")
        elif final == 3:
            print("Kann da einer nicht verlieren?!\n")
        elif final == 4:
            print("Wir hoffen Sie bald wieder bei Chicago begrüßen zu dürfen!\n")

        print("Endstand:\t" + str(player_1.name) + " " + str(player_1.points) + ":" + str(player_2.points) + " " + str(player_2.name))
        if player_1.points > player_2.points:
            print("Herzichen Glückunsch " + str(player_1.name) + ", du gewinnst. Mehr Glück beim nächsten Mal " + str(player_2.name) + "!")
        elif player_1.points < player_2.points:
            print("Herzichen Glückunsch " + str(player_2.name) + ", du gewinnst. Mehr Glück beim nächsten Mal " + str(player_1.name) + "!")
        elif player_1.points == player_2.points:
            print("Unendschieden! Endstand ist Spaß:Spaß!")
    else:
        raise Exception


