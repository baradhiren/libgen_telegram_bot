import os


class FileInteractions:

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        self.abs_path = script_dir + "/libgenmirrors.txt"
        self.mirrors = []

    def readmirrors(self):
        with open(self.abs_path, 'r') as readfile:
            for line in readfile.readlines():
                self.mirrors.append(line.strip())
            return self.mirrors

    def appendmirrors(self, text):
        with open(abs_path, 'a') as appendfile:
            text = text + "\n"
            appendfile.write(text)
