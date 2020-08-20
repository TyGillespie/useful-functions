import ctypes
import os
import wx


class console_class(object):
    def __init__(self):
        pass

    def title(self, title):
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    def output(self, text):
        print(text)

    def output_line(self, text):
        print(text + "\n")

    def clear(self):
        os.system("cls")

    def text_input(self, prompt=""):
        return input(prompt)


class gui_class(object):
    def __init__(self):
        pass

    def alert(self, title, text):
        wx.MessageBox(text, title)


console = console_class()
gui = gui_class()
app = wx.App()
