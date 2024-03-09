import random
import os
from PIL import Image
import numpy as np


class AvatarGenerator:
    def __init__(self, path=".\\avatars"):
        self.width = 528
        self.height = 560
        self.chanels = 4
        self.pic = np.full([self.height, self.width, self.chanels, 256], 0)
        print("Train:")
        for filename in os.listdir(path):
            img = Image.open(path + "\\" + filename)
            print(filename)
            arr = np.array(img)
            for y in range(self.height):
                for x in range(self.width):
                    for c in range(self.chanels):
                        self.pic[y][x][c][arr[y][x][c]] += 1

    def generate(self, filename, mle=False):
        pixel = [i for i in range(256)]
        res = np.empty([self.height, self.width, self.chanels])
        if mle:
            self.pic += 1
        for y in range(self.height):
            for x in range(self.width):
                for c in range(self.chanels):
                    res[y][x][c] = random.choices(pixel, weights=self.pic[y][x][c])[0]
        im = Image.fromarray(res.astype(np.uint8))
        im.save(f".\\imgs\\{filename}.png")
