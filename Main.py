import os
import sys
from tkinter import *
from tkinter import ttk
from WordGuessing import Word, WordsPacks

# declare the window
window = Tk()


class Main:
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    def __init__(self, n_guess, word_pack):
        self.n_guess = n_guess
        self.word_pack = word_pack
        self.wrong_guess = []

        # set window title
        window.title("Hangman Game")
        # set window width and height
        # window.geometry('800x600')
        # set window background color
        # window.configure(bg='lightgray')
        frm = ttk.Frame(window)
        frm.grid()
        self.frm = frm

        words = Word(n_guess, word_pack)
        word, length = words.generate_word()
        self.word = word.upper()
        self.length = length
        print(word)
        for i in range(length):
            ttk.Label(frm, text="_", width=10, padding=10, font=32).grid(column=i, row=0)
        ttk.Label(frm, text=f"Length: {length}", font=40, foreground='darkblue', padding=5).grid(column=0, row=1)
        ttk.Label(frm, text=f"Guess Left: {n_guess}", font=40, foreground='darkblue', padding=5).grid(
            column=length // 2, row=1)
        ttk.Label(frm, text=f"Wrong Guess: {self.wrong_guess}", font=40, foreground='darkblue', padding=5).grid(
            column=(length - 1), row=1)

        # k = 0
        # row = 2
        # j = 0
        # for letter in self.alphabet:
        #     if k == length:
        #         row += 1
        #         k = 0
        #     nLetter = letter
        #     ttk.Button(frm, text=letter, width=5, padding=10, command=lambda: self.get_letter(nLetter)).grid(column=k, row=row)
        #     k += 1
        #     j += 1
        # УРОДСТВО!

        ttk.Button(frm, text=self.alphabet[0], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[0])).grid(column=0, row=2)
        ttk.Button(frm, text=self.alphabet[1], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[1])).grid(column=1, row=2)
        ttk.Button(frm, text=self.alphabet[2], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[2])).grid(column=2, row=2)
        ttk.Button(frm, text=self.alphabet[3], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[3])).grid(column=3, row=2)
        ttk.Button(frm, text=self.alphabet[4], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[4])).grid(column=4, row=2)
        ttk.Button(frm, text=self.alphabet[5], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[5])).grid(column=5, row=2)
        ttk.Button(frm, text=self.alphabet[6], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[6])).grid(column=0, row=3)
        ttk.Button(frm, text=self.alphabet[7], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[7])).grid(column=1, row=3)
        ttk.Button(frm, text=self.alphabet[8], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[8])).grid(column=2, row=3)
        ttk.Button(frm, text=self.alphabet[9], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[9])).grid(column=3, row=3)
        ttk.Button(frm, text=self.alphabet[10], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[10])).grid(column=4, row=3)
        ttk.Button(frm, text=self.alphabet[11], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[11])).grid(column=5, row=3)
        ttk.Button(frm, text=self.alphabet[12], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[12])).grid(column=0, row=4)
        ttk.Button(frm, text=self.alphabet[13], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[13])).grid(column=1, row=4)
        ttk.Button(frm, text=self.alphabet[14], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[14])).grid(column=2, row=4)
        ttk.Button(frm, text=self.alphabet[15], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[15])).grid(column=3, row=4)
        ttk.Button(frm, text=self.alphabet[16], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[16])).grid(column=4, row=4)
        ttk.Button(frm, text=self.alphabet[17], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[17])).grid(column=5, row=4)
        ttk.Button(frm, text=self.alphabet[18], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[18])).grid(column=0, row=5)
        ttk.Button(frm, text=self.alphabet[19], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[19])).grid(column=1, row=5)
        ttk.Button(frm, text=self.alphabet[20], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[20])).grid(column=2, row=5)
        ttk.Button(frm, text=self.alphabet[21], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[21])).grid(column=3, row=5)
        ttk.Button(frm, text=self.alphabet[22], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[22])).grid(column=4, row=5)
        ttk.Button(frm, text=self.alphabet[23], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[23])).grid(column=5, row=5)
        ttk.Button(frm, text=self.alphabet[24], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[24])).grid(column=0, row=6)
        ttk.Button(frm, text=self.alphabet[25], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[25])).grid(column=1, row=6)
        ttk.Button(frm, text=self.alphabet[26], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[26])).grid(column=2, row=6)
        ttk.Button(frm, text=self.alphabet[27], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[27])).grid(column=3, row=6)
        ttk.Button(frm, text=self.alphabet[28], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[28])).grid(column=4, row=6)
        ttk.Button(frm, text=self.alphabet[29], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[29])).grid(column=5, row=6)
        ttk.Button(frm, text=self.alphabet[30], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[30])).grid(column=0, row=7)
        ttk.Button(frm, text=self.alphabet[31], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[31])).grid(column=1, row=7)
        ttk.Button(frm, text=self.alphabet[32], width=5, padding=10,
                   command=lambda: self.get_letter(self.alphabet[32])).grid(column=2, row=7)

        ttk.Button(frm, text="Restart", command=self.restart_program).grid(column=4, row=10)

        if self.n_guess <= 0:
            print("You died! The word was:", word)
            window.quit()

        while True:
            window.mainloop()

    def get_letter(self, letter):
        positions = []
        word = self.word
        if letter in word:
            i = 0
            for let in word:
                if let == letter:
                    positions.append(i)
                i += 1
            for n in range(len(positions)):
                ttk.Label(self.frm, text=letter, width=10, padding=10, font=32).grid(column=positions[n], row=0)

        else:
            if letter not in self.wrong_guess:
                self.wrong_guess.append(letter)
                ttk.Label(self.frm, text=f"Wrong Guess: {self.wrong_guess}", font=40, foreground='darkblue', padding=5).grid(
                    column=(self.length - 1), row=1)
                self.n_guess -= 1
                ttk.Label(self.frm, text=f"Guess Left: {self.n_guess}", font=40, foreground='darkblue', padding=5).grid(
                    column=self.length // 2, row=1)
                if self.n_guess == 0:
                    print("You died! The word was:", word)
                    window.destroy()

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)


main = Main(5, WordsPacks.countries_pack)
