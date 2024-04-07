'''
This file contains the Piece class which represents a Tetris piece.
'''
class Piece:
    def __init__(self):
        self.x = 4
        self.y = 0
        self.shape = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    def rotate(self):
        '''
        Rotates the piece clockwise.
        '''
        rotated_shape = [[0] * 4 for _ in range(4)]
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                rotated_shape[col][3 - row] = self.shape[row][col]
        return rotated_shape