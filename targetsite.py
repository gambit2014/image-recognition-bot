import time
import webbrowser
import cv2 as cv
import pyautogui as pg

# website
webbrowser.open("https://human-benchmark.org/aim-trainer")
time.sleep(5)

# images
target = cv.imread("victim.png")  # VICTIM
start_button_image = "startvictim.png"  # TART
try_again_image = "victimtryagain.png"  # AGAIN


def click_image(image_path, confidence=0.7):
    while True:
        try:
            pos = pg.locateOnScreen(image_path, confidence=confidence)
            if pos is not None:
                pg.moveTo(pos[0] + pos[2] // 2, pos[1] + pos[3] // 2)
                pg.click()
                break
        except TypeError:
            pass


def hit_target(target_image, num_hits):
    for _ in range(num_hits):
        try:
            pos = pg.locateOnScreen(target_image, confidence=0.6)
            if pos is not None:
                pg.moveTo(pos[0] + pos[2] // 2, pos[1] + pos[3] // 2)
                pg.click()
        except TypeError:
            pass


# Click 'Start' button
click_image(start_button_image)

# LUPA
for _ in range(6):
    # Hit target 30 times
    hit_target("victim.png", 30)

    # Click 'Try Again' button
    click_image(try_again_image)
