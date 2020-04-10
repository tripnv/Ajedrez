#first the picture should be resized so every time it is cut up, the same pixel # apply 
#most of the pictures are 900p, for our first try it should be resized to 800p (%8==0)
import cv2
import numpy as np
import os 

def read_in(picture_name):
    path = os.getcwd()
    board = cv2.imread(path + picture_name)
    return board 

def slicing(board):
    board = cv2.resize(board, (800,800))
    grid = np.empty((8,8))
    
    for i in range(8):
        for j in range(8):
            image = board[i*100:(i+1)*100,j*100:(j+1)*100]
            """if picture is not empty:
                grid[i][j] = identify_piece()        when sliced and identified the according letter will be added.
            else:
                grid[i][j]= 0"""
    return grid


def main():
    if __name__ == "__main__":
        board = read_in("file")
        id_board = slicing(board)