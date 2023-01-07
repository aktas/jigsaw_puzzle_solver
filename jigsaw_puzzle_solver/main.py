from genetic_algorithm import GeneticAlgorithm
import cv2
import create_puzzle
import time
import argparse
import sys

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Image path')
ap.add_argument('-W', '--width', required=True, help='Piece\'s width')
ap.add_argument('-H', '--height', required=True, help='Piece\'s height')
args = vars(ap.parse_args())

image_input = args['image']
puzzled_image_out = "images/output_puzzle/puzzeled_out.jpg"
width = int(args['width'])
height = int(args['height'])
piece_size = [height, width]

create_puzzle._create_puzzle(puzzled_image_out, image_input, piece_size)

start_time = time.perf_counter()

image = cv2.imread(puzzled_image_out)
h, w, c = image.shape

# Change generation and population number here
GENERATIONS = 30
POPULATION = int(w/width) * int(h/height)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Puzzled image output.
solution = GeneticAlgorithm(image, piece_size, POPULATION, GENERATIONS).start_evolution().to_image()

# Saving the output.
image_output = "images/output_solution/solution.jpg"
cv2.imwrite(image_output, solution)
print("Saved to '{}'".format(image_output))


finish_time = time.perf_counter()

print((finish_time - start_time) / 60.0)