from PIL import Image, ImageFilter
import sys
import os

#creates new directory
current = os.getcwd()
parent_director = f'{current}'
directory = sys.argv[2]
path = os.path.join(parent_director, directory)
os.mkdir(path)

