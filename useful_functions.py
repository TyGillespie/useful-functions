import ctypes
import os
import wx


class Console(object):
    @staticmethod
    def title(title: str):
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    @staticmethod
    def output(text: str):
        print(text, end="")

    @staticmethod
    def output_line(text: str):
        print(text)

    @staticmethod
    def clear():
        os.system("cls")

    @staticmethod
    def text_input(prompt: str = ""):
        return input(prompt)


class GUI(object):
    @staticmethod
    def alert(title: str, text: str):
        wx.MessageBox(text, title)

    @staticmethod
    def input_box(title: str, message: str):
        dlg = wx.TextEntryDialog(None, message, title)
        dlg.ShowModal()
        return dlg.GetValue()
        dlg.Destroy()


app = wx.App()
