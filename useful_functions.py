import ctypes
import os
import wx


class Console(object):
    @staticmethod
    def title(title: str):
        """Sets the console title."""
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    @staticmethod
    def output(text: str):
        """Prints a string of text without a line break at the end."""
        print(text, end="")

    @staticmethod
    def output_line(text: str):
        """Prints a line of text to the console with a line break at the end."""
        print(text)

    @staticmethod
    def clear():
        """Clear the console of all text."""
        os.system("cls")

    @staticmethod
    def text_input(prompt: str = ""):
        """Prompts the user for input."""
        text = input(prompt)
        return text


class GUI(object):
    @staticmethod
    def alert(title: str, text: str):
        """Shows a basic Modal Dialog with an OK button."""
        wx.MessageBox(text, title)

    @staticmethod
    def input_box(title: str, message: str):
        """Shows an input box with OK and Cancel buttons."""
        dlg = wx.TextEntryDialog(None, message, title)
        dlg.ShowModal()
        return dlg.GetValue()
        dlg.Destroy()


app = wx.App()
