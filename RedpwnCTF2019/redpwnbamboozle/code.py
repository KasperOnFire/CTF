from PIL import Image
import numpy as np
from webcolors import rgb_to_hex

data_file = "data2d.txt"

w, h = 600, 800
data1d = []
data2d = np.zeros((h*w, 3), dtype=np.uint8)
data3d = np.zeros((h, w, 3), dtype=np.uint8)

with open(data_file, "r") as in_file:
    data_in = list(in_file.readlines())

for in_list in data_in[0].strip().split(', '):
    new_list = list(in_list[1:-1].split(" "))
    data1d.append(new_list)

colors = set()

for entry in data1d:
    entry = list(map(int, entry))
    colors.add(rgb_to_hex((entry[0], entry[1], entry[2])))

print(colors)
print(len(colors))

np2d = np.array(data1d).reshape(480000, 3)
data3d = np2d.astype("uint8")
data3d = data3d.reshape(h, w, 3)

img = Image.fromarray(data3d, "RGB")
img.save("bamboozle.png")
