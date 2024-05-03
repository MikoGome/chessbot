#!/usr/bin/python3
import time

import chess
import chess.engine

import subprocess

from scan import scan
from chesscomboard import initialize
from action import move

def main():
    engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-ubuntu-x86-64-avx2");
    
    board = chess.Board()
    vizboard = initialize()

    lastmove = []

    while not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=0.1))
        white_decision = result.move
        board.push(white_decision)
        print("White move: ", white_decision)
        move(str(white_decision), vizboard)
        print(board)
        while True:
            time.sleep(1)
            inputArr = scan(vizboard)
            if len(inputArr) > 1:
                break
        input = inputArr[0]+inputArr[1]
        if chess.Move.from_uci(input) not in board.legal_moves:
            input = inputArr[1]+inputArr[0]
        black_decision = chess.Move.from_uci(input)
        print("Black move: ", black_decision)
        board.push(black_decision)

    engine.quit()

if __name__ == "__main__":
    main()
