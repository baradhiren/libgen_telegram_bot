import os



class FileInteractions():

    def __init__(self):
        self.mirrors = []

    def readmirrors(self):
        with open('B:\Projects\GitHub Projects\Book_Downloader_Telegram\libgenmirrors.txt', 'r') as readfile:
            for line in readfile.readlines():
                self.mirrors.append(line.strip())
            return self.mirrors

    def appendmirrors(self, text):
        with open('B:\Projects\GitHub Projects\Book_Downloader_Telegram\libgenmirrors.txt', 'a') as appendfile:
            text = text + "\n"
            appendfile.write(text)
