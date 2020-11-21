# NOTE - THIS SHOULD BE IN "MU" PYTHON EDITOR - UNLESS EXPORTED
# IN MU - CLICK ON MODE - THEN PRESS "Pygame Zero"

import random

TITLE = "Flappy Bird"
WIDTH = 400
HEIGHT = 708


def update():

    # Moving Barry the bird
    Barry.speed += gravity
    Barry.y += 1

    # Moving the pipes
    Barry.y += Barry.speed
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed

    # Hitting pipes?
    if top_pipe.right < 0:
        offset = random.randint(200, HEIGHT -300)
        top_pipe.midleft = (WIDTH, offset)
        bottom_pipe.midleft = (WIDTH, offset + top_pipe.height + gap)
        top_pipe.pair_number += 1


    # Barry the bird off the screen?
    if Barry.y > HEIGHT or Barry.y < 0:
        reset()

    # If we hit the pipes
    if (Barry.colliderect(top_pipe) or Barry.colliderect(bottom_pipe)):
        hit_pipe()


# Animation
    if Barry.alive:
        if Barry.speed > 0:
            Barry.image = "bird1"
        else:
            Barry.image = "bird0"


    # Changing score
    if top_pipe.right < Barry.x:
        Barry.score = top_pipe.pair_number


def on_mouse_down():
    if Barry.alive:
        Barry.speed = -6.5


def reset():
    print("Back to the start...")
    Barry.speed = 1
    Barry.center = (75, 350)
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)
    top_pipe.pair_number = 1
    Barry.alive = True
    Barry.score = 0


def hit_pipe():
    print("You hit the pipe.")
    Barry.image = "birddead"
    Barry.alive = False


def draw():
    screen.blit("background", (0, 0))
    Barry.draw()
    top_pipe.draw()
    bottom_pipe.draw()

    screen.draw.text(
    str(Barry.score),
    color = "white",
    midtop = (20, 10),
    fontsize = 70,
    )

Barry = Actor("bird1", (75, 350))

Barry.speed = 1

# adding pipes
gap = 140
top_pipe = Actor("top", (300, 0))
bottom_pipe = Actor("bottom", (300, top_pipe.height + gap))

# flying forwards
scroll_speed = -1

reset()
gravity = 0.3
Barry.score = 0
