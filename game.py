from graphics import *
import time

def main():
    FPS = 30

    screen = Canvas(size = (40, 40))

    ball = Sprite(
        shapes.Circle(5),
        position = (14, 10)
    )

    screen.sprites.append(ball)

    r = .7
    yv = 0
    with NonBlockingInput() as nbi:
        while True:

            edge = ball.edge(screen):

            if 2 in edge:
                if yv < 0:
                    yv *= -r

            if 0 in edge:
                if yv > 0:
                    yv *= -r
                elif abs(yv) < r:
                    yv = 0
            else:
                yv += .1

            ball.position[1] += yv

            ch = nbi.char()

            if ch == '.':
                if not 3 in ball.edge(screen):
                    ball.move(3)
            if ch == ',':
                if not 1 in ball.edge(screen):
                    ball.move(1)
            if ch == ' ':
                v -= 2

            print(screen)

            time.sleep(1/FPS)

if __name__ == '__main__':
    main()
