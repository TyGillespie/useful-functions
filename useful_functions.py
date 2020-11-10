import ctypes
import os
import wx


class Console(object):
    @staticmethod
    def title(title):
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    @staticmethod
    def output(text):
        print(text, end="")

    @staticmethod
    def output_line(text):
        print(text)

    @staticmethod
    def clear():
        os.system("cls")

    @staticmethod
    def text_input(self, prompt=""):
        return input(prompt)


class GUI(object):
    @staticmethod
    def alert(self, title, text):
        wx.MessageBox(text, title)
    @staticmethod
    def input_box(title, message):
        dlg=wx.TextEntryDialog(None, message, title)
        dlg.ShowModal()
        return dlg.GetValue()
        dlg.Destroy()
    

app = wx.App()
