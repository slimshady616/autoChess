

from chess_game import ChessGame
from stockfish import Stockfish
import time


def main():
    try:
        chess_game = ChessGame()
        s=Stockfish(r"C:\Users\saran\stockfish\stockfish-windows-x86-64.exe")
        chess_game.login("616spidey", "gtexejpg$S17")
        chess_game.start_1min()
        color=chess_game.my_color()
        if color=="white":
            chess_game.start_move()
            s.set_position(['e2e4'])
        else:
            if chess_game.black_move():
                opp_move=chess_game.get_opp_move()
                s.set_position([opp_move[2:]+opp_move[:2]])
                best_move=s.get_best_move()
                chess_game.make_move(best_move)
                s.make_moves_from_current_position([best_move])
            
        counter=0
        while True:
            if chess_game.not_your_move():
                continue
            counter=counter+1
            print("move : ",counter)
            opp_move=chess_game.get_opp_move()
            try:
                s.make_moves_from_current_position([opp_move])
            except:
                s.make_moves_from_current_position([opp_move[2:]+opp_move[:2]])
            best_move=s.get_best_move()
            print(best_move)
            chess_game.make_move(best_move)
            if len(best_move)==5:
                print("promotion")
                chess_game.promotion(best_move[4])
            print('made')
            s.make_moves_from_current_position([best_move])
        input("enter : ")
        
    except:
        input("except : ")



"""
from chess_game import ChessGame
from stockfish import Stockfish
import time

def main():
    try:
        chess_game = ChessGame()
        chess_game.login("slimshady616", "gtexejpg$S17")
        chess_game.start_game_with_bot()
        chess_game.start_move()
        s.set_position(['e2e4'])
        counter=0
        while True:
            if chess_game.not_your_move():
                continue
            counter=counter+1
            print("move : ",counter)
            opp_move=chess_game.get_opp_move()
            try:
                s.make_moves_from_current_position([opp_move])
            except:
                s.make_moves_from_current_position([opp_move[2:]+opp_move[:2]])
            best_move=s.get_best_move()
            print(best_move)
            chess_game.make_move(best_move)
            if len(best_move)==5:
                print("promotion")
                chess_game.promotion(best_move[4])
            print('made')
            s.make_moves_from_current_position([best_move])
        input("enter : ")
        
    except Exception as e:
        print(e)
        input("except : ")

"""


if __name__ == "__main__":
    main()


