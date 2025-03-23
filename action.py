import subprocess
import time
import keyboard

def move(move, board):
    begin = move[0:2]
    end = move[2:4]
    init = convert(begin, board)
    final = convert(end, board)
    padding = 30
    keyboard.wait('q')
    subprocess.call(["xdotool", "mousemove", str(init[0]-padding), str(init[1]+padding)])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(0.1)
    subprocess.call(["xdotool", "mousemove", str(final[0]-padding), str(final[1]+padding)])
    subprocess.call(["xdotool", "click", "1"])
    subprocess.call(["xdotool", "mousemove", "500", "10"])
    if len(move) > 4:
        subprocess.call(["xdotool", "mousemove", str(final[0]-padding), str(final[1]+padding)])
        subprocess.call(["xdotool", "click", "1"])
        subprocess.call(["xdotool", "mousemove", "500", "10"])

def convert(coord, board):
    for square in board:
      if coord == square["pos"]:
          return square["coord"]
