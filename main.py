#!/usr/bin/python3
import time

import chess
import chess.engine

from scan import scan
from chesscomboard import initialize, flip
from action import move

def main():
    engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-ubuntu-x86-64-avx2");
    
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
            player_move(board, chess, vizboard)
            opponent_move(board, chess, vizboard)
            print(board, "\n")
        elif player == 'b':
            opponent_move(board, chess, vizboard)
            player_move(board, chess, vizboard)
            print(board, "\n")
    print("game over")
    engine.quit()

def player_move(board, chess, vizboard):
    engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-ubuntu-x86-64-avx2");
    result = engine.play(board, chess.engine.Limit(time=1))
    move(str(result.move), vizboard)
    board.push(result.move)

def opponent_move(board, chess, vizboard):
    while True:
        if board.is_game_over():
            break
        time.sleep(1)
        inputArr = scan(vizboard)
        if len(inputArr) < 2:
            continue
        opponent_move = inputArr[0]+inputArr[1]
        if chess.Move.from_uci(opponent_move) not in board.legal_moves:
            opponent_move = inputArr[1]+inputArr[0]
        if chess.Move.from_uci(opponent_move) in board.legal_moves:
            break
    move = chess.Move.from_uci(opponent_move)
    board.push(move)
    
if __name__ == "__main__":
    main()
