import subprocess
import tkinter
import webbrowser

from PIL import Image, ImageTk


class Button:
    def __init__(self, root, text, icon, action, action_args, row, colum):
        """

        :param root: window
        :param text: Button text
        :param icon: Button icon
        :param action: Methon
        :param action_args: link to site or application
        :param row: row
        :param colum: colum
        """
        self.root = root
        self.text = text
        self.icon = icon
        self.action = action
        self.action_args = action_args
        self.row = row
        self.colum = colum

    def _create_button(self):
        """
        creating button
        :return:
        """
        button = tkinter.Button(self.root, text=self.text, image=self.icon,
                                command=lambda: self.action(self.action_args), bg='white', font=('Helvetica', 14),
                                compound='left')
        button.grid(row=self.row, column=self.colum, sticky='we', padx=10, pady=10, ipadx=10)


class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)

        self.root.title("Launcher")
        self.root.configure(bg='white')

        self._load_items()

    def _convert_image(self, path: str, x_size: int = 32, y_size: int = 32):
        """
        Convert Image
        :param path: Path to icon
        :param x_size: size x
        :param y_size: size y
        :return: converted image
        """
        tmp_icon = Image.open(path)
        tmp_icon.resize((x_size, y_size), Image.LANCZOS)
        return ImageTk.PhotoImage(tmp_icon)

    def _load_items(self):
        self.notepad_icon_tk = self._convert_image(r'images/notepad.png')
        self.calc_icon_tk = self._convert_image(r'images/calculator.png')
        self.stackoverflow_icon_tk = self._convert_image(r'images/stackoverflow.png')
        self.youtube_icon_tk = self._convert_image(r'images/youtube.png')
        self.github_icon_tk = self._convert_image(r'images/github.png')
        self.python_icon_tk = self._convert_image(r'images/python.png')
        self.photoshop_icon_tk = self._convert_image(r'images/photoshop.png')
        self.settings_icon_tk = self._convert_image(r'images/settings.png')
        self.exit_icon_tk = self._convert_image(r'images/exit.png')
        self.explorer_icon_tk = self._convert_image(r'images/explorer.png')
        self.icon_icon_tk = self._convert_image(r'images/icon.png')
        self.paint_icon_tk = self._convert_image(r'images/paint.png')
        self.size_icon_tk = self._convert_image(r'images/size.png')

    def _run_program(self, path: str):
        subprocess.Popen(path)

    def _run_browser(self, url: str):
        webbrowser.open(url)

    def _create_widgets(self):
        """
        Creating UI
        :return:
        """
        self.mainframe = tkinter.Frame(self.root)


if __name__ == '__main__':
    root = tkinter.Tk()
