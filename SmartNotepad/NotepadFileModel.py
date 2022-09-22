import string
from tkinter import filedialog
from typing import Text
import os


class File_Model:
    def __init__(self):
        self.url = ""
        self.offset = 6
        self.key = string.ascii_letters+''.join([str(x) for x in range(0, 10)])

    def encrypt(self, plaintext):
        result = ''

        for ch in plaintext:
            try:
                ind = (self.key.index(ch) + self.offset) % 62
                result += self.key[ind]
            except ValueError:
                result += ch

        return result

    def decrypt(self, ciphertext):
        result = ''

        for ch in ciphertext:
            try:
                ind = (self.key.index(ch) - self.offset) % 62
                result += self.key[ind]
            except ValueError:
                result += ch

        return result

    def open_file(self):
        self.url = filedialog.askopenfile(title='select text file only', filetypes=[
            ("Text Documents", "*.*")])
        if self.url == None:
            return
        self.url = self.url.name

    def new_file(self):
        self.url = ""

    def save_as(self, msg):
        encrypt_text = self.encrypt(msg)
        self.url = filedialog.asksaveasfile(
            mode='w', defaultextension=".ntxt", filetypes=[("All Files", "*.*"),
                                                           ("Text Documents", "*.*")])
        if self.url is None:
            return
        self.url.write(encrypt_text)
        filepath = self.url.name
        self.url.close()
        self.url = filepath

    def save_file(self, msg):
        if self.url == '':
            self.url = filedialog.asksaveasfilename(title="Select file name", defaultextension=".ntxt", filetypes=[("All Files", "*.*"),
                                                                                                                   ("Text Documents", "*.*")])
        if self.url == ():
            return
        file_name, file_extenstion = os.path.splitext(self.url)
        print(file_extenstion == '.ntxt')
        if file_extenstion == '.ntxt':
            msg = self.encrypt(msg)
        with open(self.url, "w", encoding="utf-8") as fw:
            fw.write(msg)

    def read_file(self, url):
        if url != '':
            self.url = url
        else:
            self.open_file()

        if self.url is None:
            return
        base = os.path.basename(self.url)
        file_name, file_extenstion = os.path.splitext(self.url)
        fr = open(self.url, 'r')
        contents = fr.read()
        if file_extenstion == '.ntxt':
            contents = self.decrypt(contents)
        fr.close()
        return contents, base
