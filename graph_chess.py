import chess.pgn
import numpy as np
#import tensorflow as tf
import os
#import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from graph import *
#from sklearn.ensemble import RandomForestRegressor

import pickle

'''
with open('chessrf', 'rb') as f:
    clf = pickle.load(f)
'''


import tensorflow_decision_forests as tfdf

clf = tfdf.keras.RandomForestModel()
clf.compile(metrics=["accuracy"])

#model.fit(train_ds)



def winner(result, w):
    if '1/2' in result:
        return int(2)
    else:
        r = int(results[w])
        if r == 0:
            return int(r)
        else:
            return int(r) 
'''      
def convert_to_int(board):
        #l = [None] * 64
        ll = np.zeros(64*32).reshape(32,64)
        i = 0
        for sq in chess.scan_reversed(board.occupied_co[chess.WHITE]):  # Check if white
            #print(board.piece_type_at(sq))
            if board.piece_type_at(sq) != 0:
                ll[i][sq] = board.piece_type_at(sq)
                i += 1
        for sq in chess.scan_reversed(board.occupied_co[chess.BLACK]):  # Check if black
            if board.piece_type_at(sq) != 0:
                ll[i][sq] = -board.piece_type_at(sq)
                i += 1
        return np.array([0 if v is None else v for v in ll])
'''


def convert_to_int(board):
        l = [None] * 64
        for sq in chess.scan_reversed(board.occupied_co[chess.WHITE]):  # Check if white
            l[sq] = board.piece_type_at(sq)
        for sq in chess.scan_reversed(board.occupied_co[chess.BLACK]):  # Check if black
            l[sq] = -board.piece_type_at(sq)
        return [0 if v is None else v for v in l]








X = []
y = []
dict1 = dict()
e = 0
result = 1
for filename in os.listdir("files"): 
    
    pgn = open("files/" + filename)
    while e != -1:
        i = 0
        game = chess.pgn.read_game(pgn)
        
        if game.headers["White"][0:9] == 'Stockfish':
            w = 0
        else:
            w = 1
        board = game.board()
        # get reults of game (winner/loser)
        results = game.headers['Result'].split('-')
        result = winner(results, w)
        #make all the moves within the game append X and y data to lists
        for move in game.mainline_moves():
            board.push(move)
            b = convert_to_int(board)
            X.append(b)
            y.append(np.array([float(result)]))  
            i += 1
        
        e += 1
        
