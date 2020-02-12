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
            self.rect.move_ip(self.movepos)
            self.movepos = [0, 0]

    def overturn(self):
        self.headup = not self.headup
        if self.headup:
            self.image = self.imgh
        else:
            self.image = Card.imgb

    def isclick(self, pos):
        return self.rect.collidepoint(pos)

    def move(self, rel):
        self.movepos[0] += rel[0]
        self.movepos[1] += rel[1]


class CardHeap():
    def __init__(self, rect):
        self.items = pygame.sprite.Group()
        self.count = 0
        self.area = rect

    def add(self, card):
        print('-----------------------------', card.rect, self.area.topleft)
        card.rect.move_ip(
            self.area.topleft[0] - card.rect.topleft[0], self.area.topleft[1] - card.rect.topleft[1])
        print('-----------------------------', card.rect)
        self.items.add(card)
        self.count += 1

    def remove(self, card):
        self.items.remove(card)
        self.count -= 1

    def clear(self, screen, background):
        self.items.clear(screen, background)

    def update(self):
        self.items.update()

    def draw(self, screen):
        self.items.draw(screen)

    def isclick(self, pos):
        for card in reversed(self.items.sprites()):
            if card.isclick(pos):
                return True, card
        return False, 0

    def setarea(self, rect):
        self.area = rect
        for card in self.items.sprites():
            card.rect.move_ip(rect.topleft)


allcardheaps = [CardHeap(pygame.Rect((50, 100), (100, 200))), CardHeap(
    pygame.Rect((120, 200), (200, 300))), CardHeap(pygame.Rect((30, 30), (100, 100)))]

CH = dynamic({'player0': 0, 'player1': 1, 'table': 2})


def cardinit():
    Card.imgb, no_use = load_img('back.jpg')

    # Initialise cardheaps
    ch = allcardheaps[CH.player0]
    ch.add(Card(0, 'criminal'))
    ch.add(Card(2, 'looker'))
    ch.add(Card(3, 'detective'))
    ch.add(Card(6, 'criminal'))

    ch = allcardheaps[CH.player1]
    ch.add(Card(1, 'person'))
    ch.add(Card(4, 'suspect'))
    ch.add(Card(5, 'person'))


def moveCH2CH(ch_remove, ch_add, card):
    ch_remove.remove(card)
    ch_add.add(card)


def moveCH2T(ch_remove, card):
    ch_remove.remove(card)
    allcardheaps[CH.table].add(card)
