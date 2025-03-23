#!/usr/bin/python3
import time
import sys

import chess
import chess.engine

from scan import scan
from chesscomboard import initialize, flip
from action import move

def main():
    engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-ubuntu-x86-64-avx2")
    
    engine.configure({"Skill Level": 6})
    board = chess.Board()
    vizboard = initialize()

    player = ''
    while True:
        player = input("are you white or black?[w/b]")[0].lower()
        if player == 'w':
            break
        elif player == 'b':
            flip(vizboard)
            break

    while not board.is_game_over():
        if player == 'w':
            player_move(board, chess, vizboard, engine)
            opponent_move(board, chess, vizboard, player)
            print(board, "\n")
        elif player == 'b':
            opponent_move(board, chess, vizboard, player)
            player_move(board, chess, vizboard, engine)
            print(board, "\n")
    print("game over")
    engine.quit()
    sys.exit()

def player_move(board, chess, vizboard, engine):
    result = engine.play(board, chess.engine.Limit(time=1))
    move(str(result.move), vizboard)
    board.push(result.move)

def opponent_move(board, chess, vizboard, player):
    while True:
        if board.is_game_over():
            break
            
        inputArr = scan(vizboard)
        if len(inputArr) < 2:
            continue

        opponent_move = inputArr[0]+inputArr[1]
        if chess.Move.from_uci(opponent_move) not in board.legal_moves:
            opponent_move = inputArr[1]+inputArr[0]
        if chess.Move.from_uci(opponent_move) not in board.legal_moves:
            opponent_move = inputArr[0]+inputArr[1] + 'q'
        if chess.Move.from_uci(opponent_move) in board.legal_moves:
            move = chess.Move.from_uci(opponent_move)
            board.push(move)
            break
        time.sleep(1)
    
if __name__ == "__main__":
    main()
