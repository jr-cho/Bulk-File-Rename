import os
from path import path
import random

p = path
i = 0
chars = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890<>/?.,_"
)

for r in range(10):
    rand = ""
    for l in range(9999):
        rand += random.choice(chars)

if os.path.exists(p):
    if os.path.isdir(p):
        os.chdir(p)

        for t in range(5):
            i += 1
            file_path = f"text{i}.txt"
            with open(file_path, "w") as file:
                file.write(rand)

        print("Text written to the files.")
    else:
        print("The specified path is not a directory.")
else:
    print("The specified directory does not exist.")
