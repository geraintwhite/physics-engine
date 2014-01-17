from graphics import *

def main():
    screen = Canvas()
    circle = Sprite(shapes.Circle(5),
                    position = (10, 5))
    screen.sprites.append(circle)
    print(screen)

if __name__ == '__main__':
    main()