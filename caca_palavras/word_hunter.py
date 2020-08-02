#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alex
#
# Created:     02/08/2020
# Copyright:   (c) alex 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
from random import randint
from copy import deepcopy
import unicodedata

SIZE_X = 80
SIZE_Y = 40

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4


def main():
    with open("word2.txt") as f:
        words = [w.strip().upper() for w in f.readlines() if w.strip() != ""]

        # remove accents
        words = [unicodedata.normalize('NFD', w).encode('ascii', 'ignore').decode('UTF-8') for w in words]

    table = [[' '] * SIZE_X for _ in range(SIZE_Y)]
    for word in words:
        count = 0
        fitted = False
        while not fitted:
            fitted = True

            while True:
                startX = randint(0, SIZE_X-1)
                startY = randint(0, SIZE_Y-1)
                if table[startY][startX] == ' ':
                    break

            direction = randint(1, 4)
            if direction == LEFT:
                if startX < len(word) - 1:
                    direction = RIGHT
            elif direction == RIGHT:
                if SIZE_X - startX < len(word):
                    direction = LEFT
            elif direction == UP:
                if startY < len(word) - 1:
                    direction = DOWN
            else:
                if SIZE_Y - startY < len(word):
                    direction = UP

            count = count + 1
            if count > 50000:
                print (word, "failed")
                break

            cursorX = startX
            cursorY = startY
            for character in word:
                #print(cursorX, cursorY, word)
                if table[cursorY][cursorX] != " " and table[cursorY][cursorX] != character:
                    fitted = False
                    break

                if direction == LEFT:
                    cursorX -= 1
                elif direction == RIGHT:
                    cursorX += 1
                elif direction == UP:
                    cursorY -= 1
                else: # DOWN
                    cursorY += 1

                if cursorX < 0 or cursorX >= SIZE_X or cursorY < 0 or cursorY >= SIZE_Y:
                    fitted = False
                    break

            if fitted:
                if direction == LEFT:
                    table[startY][startX - len(word):startX] = [w for w in word][::-1]
                    if len(table[startY]) > SIZE_X:
                        print(1)
                elif direction == RIGHT:
                    table[startY][startX:startX + len(word)] = [w for w in word]
                    if len(table[startY]) > SIZE_X:
                        print(1)
                elif direction == UP:
                    for i, c in enumerate(word):
                        table[startY - i][startX] = c
                else: # DOWN
                    for i, c in enumerate(word):
                        table[startY + i][startX] = c

    for y, line in enumerate(table):
        for x, c in enumerate(line):
            if c == ' ':
                table[y][x] = chr(randint(ord('A'), ord('Z')))


    # draw table
    with open ("game.txt", "w") as f:
        for line in table:
            for c in line:
                #print(c, end="")
                f.write(c)
            #print("")
            f.write("\n")
    print("Done")


if __name__ == '__main__':
    main()
