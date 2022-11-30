from tkinter import *
import check
import scoreboard as sb

next_player = "X"


button = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = Tk()
string = StringVar()


def reset_button_click():
    global root, string, next_player
    root.destroy()
    root = Tk()
    string = StringVar()
    next_player = "X"
    game_start()


def button_click(num):
    global next_player

    if button[num]['text'] == "-":
        if next_player == "X":
            button[num]['text'] = "X"
            next_player = "O"
        else:
            button[num]['text'] = "O"
            next_player = "X"
    state = check.check(button)
    if state != "nincs":
        win_window(state)

    string.set(next_player + " következik")


def win_window(state):
    root.destroy()
    root2 = Tk()
    root2.title("Győzelem")
    root2.geometry('400x200')
    root2.eval('tk::PlaceWindow . center')
    root2_label = Label(text=state, font=("Arial", 16), fg="Red")

    if state == "X nyert":
        sb.set_win("X")
    elif state == "O nyert":
        sb.set_win("O")
    elif state == "Döntetlen":
        sb.set_win("Döntetlen")
    else:
        print("Hibás state a winnél.")

    wins = sb.get_wins()
    string2 = "Eddig X nyert {x_win} alkalommal. \nEddig O nyert {o_win} alkalommal.\
     \nDöntetlen lett {draw} alkalommal.".format(x_win=wins[0], o_win=wins[1], draw=wins[2])
    root2_label2 = Label(text=string2, font=("Arial", 16))
    root2_label.pack()
    root2_label2.pack()
    root2.mainloop()


def game_start():

    root.geometry("200x200")
    root.eval('tk::PlaceWindow . center')
    root.title('Tic-Tac-Toe')
    root.resizable(0, 0)

    string.set(next_player + " következik")
    label = Label(textvariable=string)
    label.grid(row=0, column=1)

    button[1] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(1))
    button[1].grid(row=1, column=0)

    button[2] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(2))
    button[2].grid(row=1, column=1)

    button[3] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(3))
    button[3].grid(row=1, column=2)

    button[4] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(4))
    button[4].grid(row=2, column=0)

    button[5] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(5))
    button[5].grid(row=2, column=1)

    button[6] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(6))
    button[6].grid(row=2, column=2)

    button[7] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(7))
    button[7].grid(row=3, column=0)

    button[8] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(8))
    button[8].grid(row=3, column=1)

    button[9] = Button(root, text="-", font=("Arial", 16), command=lambda: button_click(9))
    button[9].grid(row=3, column=2)

    reset_button = Button(root, text="Reset", font=("Arial", 16), command=reset_button_click)
    reset_button.grid(row=4, column=2)

    root.mainloop()


game_start()
