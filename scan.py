from PIL import ImageGrab


def scan(board):
    screenshot = ImageGrab.grab()
    recent = []
    for square in board:
            (r,g,b) = screenshot.getpixel(xy=(square["coord"][0], square["coord"][1]))
            #highligted
            if (r == 185 and g == 202 and b == 67) or (r ==245 and g == 246 and b == 130):
                recent.append(square["pos"])
    return recent
