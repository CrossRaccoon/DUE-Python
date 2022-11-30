
score = [0, 1, 2]


def get_wins():
    global score
    f = open("win.txt", "r")
    currentline = f.readline().split(";")
    score[0] = currentline[0]
    score[1] = currentline[1]
    score[2] = currentline[2]
    f.close()
    return score


def set_win(symbol):
    global score
    f = open("win.txt", "r")
    currentline = f.readline().split(";")
    score[0] = currentline[0]
    score[1] = currentline[1]
    score[2] = currentline[2]

    if symbol == "X":
        score[0] = int(score[0]) + 1
    elif symbol == "O":
        score[1] = int(score[1]) + 1
    elif symbol == "Döntetlen":
        score[2] = int(score[2]) + 1
    else:
        print("Hibás symbol a scoreboardban.")
    f.close()
    f = open("win.txt", "w")
    line = "{a};{b};{c}".format(a=score[0], b=score[1], c=score[2])
    f.write(line)
    f.close()

