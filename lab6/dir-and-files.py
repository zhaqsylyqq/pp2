import os
import string


# --------------------------------------------1
def inf_about_path():
    path = r"C:\Users\Jahs\work\pp2\repository\pp2"
    print("Directories:")
    print(
        [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    )
    print("Files:")
    print(
        [
            name
            for name in os.listdir(path)
            if not os.path.isdir(os.path.join(path, name))
        ]
    )
    print("Directories and files :")
    print([name for name in os.listdir(path)])


# --------------------------------------------2
def check_for_access():
    path = r"C:\Users\Jahs\work\pp2\repository\pp2"
    print("Exist:", os.access(path, os.F_OK))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))


# --------------------------------------------3
def check_path_exist():
    print("Test a path exists or not:")
    path = r"g:\testpath\a.txt"
    print(os.path.exists(path))
    print("Filename:")
    print(os.path.basename(path))
    print("Dir:")
    print(os.path.dirname(path))


# --------------------------------------------4
def readlinecount():
    with open(r"myfile.txt", "r") as file:
        lines = len(file.readlines())
        print("Total Number of lines:", lines)


# --------------------------------------------5
def writinglist():
    list = ["meow", "brac", "ex3"]
    file = open("some.txt", "w")
    file.writelines(list)
    file.close()


# --------------------------------------------6
def generate26lett():
    if not os.path.exists("letters"):
        os.makedirs("letters")
    for letter in string.ascii_uppercase:
        with open(letter + ".txt", "w") as f:
            f.writelines(letter)


# --------------------------------------------7
def append_of_files():
    with open("first.txt", "r") as firstfile, open("second.txt", "a") as secondfile:
        for line in firstfile:
            secondfile.write(line)


# --------------------------------------------8
def del_file():
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")
