import graphics as g
import time


def main():

    FPS = 30

    screen = g.Canvas(size=(40, 40))

    ball = g.Sprite(
        g.shapes.Circle(5),
        position = (14, 10)
    )

    screen.sprites.append(ball)

    r = 0.7
    yv = 0
    xv = 0
    with g.NonBlockingInput() as nbi:
        while True:

            edge = ball.onEdge(screen)

            if 2 in edge:
                xv *= 0.95
                if yv < 0:
                    yv *= -r
            if 0 in edge:
                xv *= 0.95
                if yv > 0:
                    yv *= -r
                elif abs(yv) < r:
                    yv = 0
            else:
                yv += .1
            if any(x in edge for x in (1, 3)):
                yv *= 0.95
                if abs(xv) < r:
                    xv = 0
                else:
                    xv *= -r

            xv *= 0.95

            ch = nbi.char()

            if ch == '.':
                if not 3 in edge:
                    xv += 2
            if ch == ',':
                if not 1 in edge:
                    xv -= 2
            if ch == ' ':
                yv -= 2

            ball.position[0] += xv
            ball.position[1] += yv

            print(screen)

            time.sleep(1 / FPS)

if __name__ == '__main__':
    main()
