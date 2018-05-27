import os



class FileInteractions():

    def __init__(self):
        self.mirrors = []

    def readmirrors(self):
        with open('<Mirror file path>', 'r') as readfile:
            for line in readfile.readlines():
                self.mirrors.append(line.strip())
            return self.mirrors

    def appendmirrors(self, text):
        with open('<Mirror File Path>', 'a') as appendfile:
            text = text + "\n"
            appendfile.write(text)
