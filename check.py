# buttons:
# 1 2 3
# 4 5 6
# 7 8 9

string = "nincs"


def check(button):
    global string
    if (button[1]['text'] == "X" and button[2]['text'] == "X" and button[3]['text'] == "X") or \
            (button[1]['text'] == "X" and button[4]['text'] == "X" and button[7]['text'] == "X") or \
            (button[1]['text'] == "X" and button[5]['text'] == "X" and button[9]['text'] == "X") or \
            (button[2]['text'] == "X" and button[5]['text'] == "X" and button[8]['text'] == "X") or \
            (button[4]['text'] == "X" and button[5]['text'] == "X" and button[6]['text'] == "X") or \
            (button[7]['text'] == "X" and button[8]['text'] == "X" and button[9]['text'] == "X") or \
            (button[7]['text'] == "X" and button[5]['text'] == "X" and button[3]['text'] == "X"):
                string = "X nyert"
    elif (button[1]['text'] == "O" and button[2]['text'] == "O" and button[3]['text'] == "O") or \
            (button[1]['text'] == "O" and button[4]['text'] == "O" and button[7]['text'] == "O") or \
            (button[1]['text'] == "O" and button[5]['text'] == "O" and button[9]['text'] == "O") or \
            (button[2]['text'] == "O" and button[5]['text'] == "O" and button[8]['text'] == "O") or \
            (button[4]['text'] == "O" and button[5]['text'] == "O" and button[6]['text'] == "O") or \
            (button[7]['text'] == "O" and button[8]['text'] == "O" and button[9]['text'] == "O") or \
            (button[7]['text'] == "O" and button[5]['text'] == "O" and button[3]['text'] == "O"):
                string = "O nyert"
    return string
