import pygame
from pygame.locals import *
from card import *


MG = dynamic({'no_action': 0, 'click_l': 1, 'click_r': 2, 'move': 3})


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Basic Pong')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # card initialise
    cardinit()

    # Initialise mouse_gesture
    mouse_gesture = MG.no_action
    mouse_click_pos = (0, 0)
    card_click = 0
    cardheap_click = 0

    # Initialise clock
    clock = pygame.time.Clock()

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    print('-===============', pygame.Rect((50, 100), (100, 200)))

    # Event loop
    while True:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONDOWN:
                for ch in reversed(allcardheaps):
                    card_find, card_click = ch.isclick(event.pos)
                    if card_find:
                        cardheap_click = ch
                        mouse_click_pos = event.pos
                        if event.button == 1:
                            mouse_gesture = MG.click_l
                            break
                        elif event.button == 3:
                            mouse_gesture = MG.click_r
                            break

            elif event.type == MOUSEMOTION:
                if mouse_gesture == MG.click_l:
                    if abs(event.pos[0] - mouse_click_pos[0]) > 10:
                        mouse_gesture = MG.move
                        card_click.move([event.pos[0] - mouse_click_pos[0], 0])
                elif mouse_gesture == MG.move:
                    card_click.move([event.rel[0], 0])

            elif event.type == MOUSEBUTTONUP:
                if mouse_gesture == MG.click_l and event.button == 1:
                    card_click.overturn()
                elif mouse_gesture == MG.click_r and event.button == 3:
                    moveCH2T(cardheap_click, card_click)

                mouse_gesture = MG.no_action
                card_click = 0

        for ch in allcardheaps:
            ch.clear(screen, background)

        for ch in allcardheaps:
            ch.update()

        for ch in allcardheaps:
            ch.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
