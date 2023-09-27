from PIL import Image, ImageOps
import os, sys



def main():


    check_file_names()
    fit_images()

def check_file_names():

    valid_formats = [".jpeg", ".jpg", ".png"]

    #Check for valid number of command line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-lin arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-lin arguments.")

    name1, ext_1 = os.path.splitext(sys.argv[1])
    name2, ext_2 = os.path.splitext(sys.argv[2])

    if ext_1 not in valid_formats or ext_2 not in valid_formats:
        sys.exit("Invalid input")
    elif ext_1 != ext_2:
        sys.exit("Input and output have different extensions")
    #Check if the correct file format is entered.
    else:
        return True
    #If not a csv file, exit with a prompt.


def fit_images():

    try:
        shirt = Image.open("shirt.png")
        mask = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("No such file")

    resized_mask = ImageOps.fit(mask, shirt.size)

    resized_mask.paste(shirt, shirt)

    resized_mask.save(sys.argv[2])


if __name__ == "__main__":
    main()