""" docker gave error at accessing some data (segmentation fault - core dropped).
But the error went away when we modified detectron2 script, so we are going to 
try a writer, to try it as a work around"""


def main(file = "writting_inside.py", printer):

    printer = "    print('line added correctly_2')"
    # read it
    with open(file, "r") as f:
        lines = f.readlines()
    # write all excepting the one we don't want:
    with open(file, "w") as f:
        for line in lines:
            if line.strip("\n") != printer:
                f.write(line)
    # write it again (not necessary usually):
    with open(file, "a") as f:
        f.write(printer)


if __name__ == "__main__":
    main()
