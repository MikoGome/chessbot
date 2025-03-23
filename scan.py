from PIL import ImageGrab


def scan(board, tolerance=5):
    screenshot = ImageGrab.grab()
    recent = []
    for square in board:
            (r,g,b) = screenshot.getpixel(xy=(square["coord"][0], square["coord"][1]))
            #highlighted
            if ( 185-tolerance < r < 185+tolerance and 202-tolerance < g < 202+tolerance and 67-tolerance < b < 67+tolerance) or (245-tolerance <r < 245+tolerance and 246-tolerance < g < 246+tolerance and 130 - tolerance < b < 130+tolerance):
                recent.append(square["pos"])
    return recent
