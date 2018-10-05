from tkinter import *

import random
import sys
import os


def generateRandomNum(llim, ulim):
    return random.randrange(llim, ulim)


def submitGuess():
    global i
    global winFlag
    global hoc_lim
    global score
    global scorePoints
    global randomNumber
    global root

    guess = int(entryBox.get())

    print(guess)
    hoc = abs(guess - randomNumber)

    if guess == randomNumber:
        print("Bravo!")
        root.configure(background='green')
        # messagebox.showinfo("Status", "BRAVO! You won!")
        winFlag = 1
    elif hoc < hoc_lim:
        print("Hot")
        root.configure(background='red')
        # messagebox.showinfo("Status", "Hot")
    elif hoc >= hoc_lim:
        root.configure(background='blue')
        print("Cold")

    score = int(scorePoints / i)
    i = i + 1

    if score == 0:
        print("Sorry You ran out of guesses!")
        print("The number was %d" % (randomNumber))
        return

    if winFlag == 1:
        print("Congractulations! Your Score: %d" % score)
        try:

            highScoreFile = open("HighScore.txt", "r+")
            highScore = int(highScoreFile.read())

        except:

            highScoreFile = open("HighScore.txt", "w")
            highScoreFile.write(str(score))
            print("Error in opening or reading file")
            sys.exit()

        print("High Score: ", highScore)
        highScoreFile.close()


# For commandline arguments
a = sys.argv
a = list(map(int, a[1:]))

if len(a) != 4:
    print("error: invalid arguments")
    print("usage: python3 filename.py lower_limit upper_limit difficulty(5-range) score_pool")
    print("exiting...")
    sys.exit()


i = 1
guess = 0
hoc_lim = 0
scorePoints = 0
score = 0
winFlag = 0

root = Tk()

randomNumber = generateRandomNum(a[0], a[1])

label = Label(root, text="Guess").grid(row=0, sticky=W)
entryBox = Entry(root)
entryBox.grid(row=0, column=1)
submit = Button(root, text="Submit", command=submitGuess).grid(
    row=1, columnspan=2)

root.mainloop()
