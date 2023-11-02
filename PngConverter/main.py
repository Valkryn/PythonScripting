from PIL import Image
import sys
import os


def main():
    output_folder = sys.argv[2]  # gets the name of new directory from user using sys
    image_folder = sys.argv[1]
    create_directory(output_folder)
    all_img = os.listdir(f'{os.getcwd()}\\{image_folder}')
    convert_image(all_img, image_folder, output_folder)


def create_directory(d):
    if not os.path.exists(d): #if not - if the file DOES NOT EXIST ; create it.
        os.mkdir(d)  # uses os to create the new directory


def convert_image(img_list, image_folder, output_folder):
    for img_name in img_list:
        img = Image.open(f'{os.getcwd()}\\{image_folder}\\{img_name}')
        clean_name = os.path.splitext(img_name)[0] #splits the name of the from the format [0]=name [1]=format
        img.save(f'{os.getcwd()}\\{output_folder}\\{clean_name}.png', 'png')



if __name__ == '__main__':
    main()
