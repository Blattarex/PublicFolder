import sys, pygame
from pygame.locals import *



class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white, white, white, white]

        #read trivia data from file
        f = open(filename, "r")
        trivia_data = f.readlines()
        f.close()

        #count and clean trivia data
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1

    def show_question(self):
        print_text(font1, 210, 5, "TRIVIA GAME")
        print_text(font2, 190, 500-20, "Press Keys (1-4) To Answer", purple)
        print_text(font2, 530, 5, "Score", purple)
        print_text(font2, 550, 25, str(self.score), purple)

        self.correct = int(self.data[self.current+5])

        #display question
        question = self.current #6 + 1
        print_text(font1, 5, 80, "QUESTION" + str(question))
        print_text(font2, 20, 120, self.data[self.current], yellow)

        #respond to correct answer
        if self.scored:
            self.colors = [white, white, white, white]
            self.colors[self.correct-1] = green
            print_text(font1, 230, 380, "CORRECT!", green)
            print_text(font2, 170, 420, "Press Enterr for Next Question", green)
        elif self.failed:
            self.colors = [white, white, white, white]
            self.colors[self.wronganswer - 1] = red
            self.colors[self.correct-1] = green
            print_text(font2, 220, 380, "INCORRECT!", red)
            print_text(font2, 170, 420, "Press enter for next question", red)

    print_text(font1,5, 170, "ANSWERS") 
    print_text(font2,20, 210, "1 - " + self.data[self.current+1], self.colors[0])
    print_text(font2,20, 240, "2 - " + self.data[self.current+2], self.colors[1])
    print_text(font2,20, 270, "3 - " + self.data[self.current+3], self.colors[2])
    print_text(font2,20, 300, "4 - " + self.data[self.current+4], self.colors[3]) 

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white, white, white, white]
            self.current += 6
            if self.current >= self.total:
                self.current = 0

def print_text(font, x, y, text, color =(255,255,255), shadow=True):
     if shadow:
         imgText = font.render(text,True,(0,0,0))
         screen.blit(imgText, (x-2,y-2))
     imgText = font.render(text, True, color)
     screen.blit(imgText,(x,y)


