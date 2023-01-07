"""
This file takes an image as input and divides into square pieces.
Then combines all the pieces randomly.
"""

import numpy as np
import cv2
import my_image

class _create_puzzle:
    def __init__(self, puzzled_image_out, image_input, piece_size):
        self.puzzled_image_out = puzzled_image_out
        self.image_input = image_input
        self.piece_size = piece_size

        self.run()

    def run(self):
        image = cv2.imread(self.image_input)
        pieces, rows, columns = my_image.flatten_image(image, self.piece_size)

        # Shuffle pieces randomly
        np.random.shuffle(pieces)

        # Assemble all the pieces to create a puzzle
        puzzle = my_image.assemble_image(pieces, rows, columns)

        # Save puzzle image
        cv2.imwrite(self.puzzled_image_out, puzzle)
        print("Puzzle created with {} pieces\n".format(len(pieces)))

