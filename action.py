import subprocess
import time

def move(move, board):
    begin = move[0:2]
    end = move[2:4]
    init = convert(begin, board)
    final = convert(end, board)
    subprocess.call(["xdotool", "mousemove", str(init[0]), str(init[1])])
    subprocess.call(["xdotool", "click", "1"])
    time.sleep(1)
    subprocess.call(["xdotool", "mousemove", str(final[0]), str(final[1])])
    subprocess.call(["xdotool", "click", "1"])
    subprocess.call(["xdotool", "mousemove", "10", "10"])

def convert(coord, board):
    for square in board:
      if coord == square["pos"]:
        return square["coord"]