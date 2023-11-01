from PIL import Image, ImageFilter
import sys
import os


def main():
    current = os.getcwd()  # get current working dir
    directory = sys.argv[2]  # gets the name of new directory from user using sys
    target_directory = sys.argv[1]
    create_directory(current, directory)
    convert_image(f'{current}\\{target_directory}', f'{current}\\{directory}')


def convert_image(source_path, destination_path):
    with Image.open(source_path) as img:
        img.save(destination_path, "PNG")


def create_directory(c, d):
    path = os.path.join(c, d)
    os.mkdir(path)  # uses os to create the new directory


if __name__ == '__main__':
    main()
