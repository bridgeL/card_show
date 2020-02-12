import os
import pygame


class dynamic(dict):
    def __init__(self, d=None):
        if d is not None:
            for k, v in d.items():
                self[k] = v
        return super().__init__()

    def __key(self, key):
        return "" if key is None else key.lower()

    def __str__(self):
        import json
        return json.dumps(self)

    def __setattr__(self, key, value):
        self[self.__key(key)] = value

    def __getattr__(self, key):
        return self.get(self.__key(key))

    def __getitem__(self, key):
        return super().get(self.__key(key))

    def __setitem__(self, key, value):
        return super().__setitem__(self.__key(key), value)


def load_img(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    return image, image.get_rect()


class Card(pygame.sprite.Sprite):
    imgb = 0

    def __init__(self, id, lable):
        super(Card, self).__init__()
        self.imgh, self.rect = load_img(lable+'.jpg')
        self.image = self.imgh
        self.id = id
        self.lable = lable
        self.headup = True
        self.movepos = [0, 0]

    def update(self):
        if self.movepos[0] != 0 or self.movepos[1] != 0:
            self.rect = self.rect.move(self.movepos)
            self.movepos = [0, 0]

    def overturn(self):
        self.headup = not self.headup
        if self.headup:
            self.image = self.imgh
        else:
            self.image = self.imgb

    def isclick(self, pos):
        return self.rect.collidepoint(pos)

    def move(self, rel):
        self.movepos[0] += rel[0]
        self.movepos[1] += rel[1]


class CardHeap():
    null_card = 0

    def __init__(self):
        self.items = pygame.sprite.Group()
        self.count = 0

    def add(self, card):
        self.items.add(card)
        self.count += 1

    def isclick(self, pos):
        for card in reversed(self.items.sprites()):
            if card.isclick(pos):
                return True, card
        return False, CardHeap.null_card


allcardheaps = [CardHeap(), CardHeap(), CardHeap()]
CH = dynamic({'player0': 0, 'player1': 1, 'table': 2})


def cardinit():
    CardHeap.null_card = pygame.sprite.Sprite()
    Card.imgb, no_use = load_img('back.jpg')

    # Initialise cardheaps
    cardheap = allcardheaps[CH.player0]
    cardheap.add(Card(0, 'criminal'))
    cardheap.add(Card(2, 'looker'))
    cardheap.add(Card(3, 'detective'))
    cardheap.add(Card(6, 'criminal'))

    for card in cardheap.items.sprites():
        card.move((0, 100))
        card.update()

    cardheap = allcardheaps[CH.player1]
    cardheap.add(Card(1, 'person'))
    cardheap.add(Card(4, 'suspect'))
    cardheap.add(Card(5, 'person'))

    for card in cardheap.items.sprites():
        card.move((100, 200))
        card.update()
