import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *


def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except:
        print('Cannot load image:', fullname)

    return image, image.get_rect()


class Card(pygame.sprite.Sprite):
    def __init__(self, id, lable, headname):
        super(Card, self).__init__()
        self.image, self.rect = load_png(headname)

        self.id = id
        self.lable = lable
        self.headup = True
        self.catch = False
        self.movepos = [0, 0]

    def update(self):
        if self.movepos[0] != 0 or self.movepos[1] != 0:
            self.rect = self.rect.move(self.movepos)
            self.movepos = [0, 0]

    def overturn(self):
        headup = not headup

    def iscatch(self, pos):
        self.catch = self.rect.collidepoint(pos)
        return self.catch

    def move(self, rel):
        self.movepos[0] += rel[0]
        self.movepos[1] += rel[1]


class CardHeap():
    def __init__(self):
        self.items = pygame.sprite.Group()
        self.count = 0

    def add(self, card):
        self.items.add(card)
        count += 1


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Basic Pong')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # Initialise cards
    a0 = Card(0, 'criminal', 'criminal.jpg')
    a1 = Card(1, 'person', 'person.jpg')

    a1.move((100, 100))
    a1.update()

    # Initialise sprites
    b = pygame.sprite.OrderedUpdates()
    b.add(a0)
    b.add(a1)

    # Initialise clock
    clock = pygame.time.Clock()

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONDOWN:
                print('-----------------down', event)
                if(a0.iscatch(event.pos)):
                    print("------------------------------------")
            elif event.type == MOUSEMOTION:
                if(a0.catch):
                    a0.move(event.rel)
                    print(event.rel)

            elif event.type == MOUSEBUTTONUP:
                print('-------------------up', event)
                a0.catch = False

        b.clear(screen, background)
        b.update()
        b.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
