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
        :param action: Method
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
        self._create_button()

    def _create_button(self):
        """
        creating button
        :return:
        """
        button = tkinter.Button(self.root, text=self.text, image=self.icon,
                                command=lambda: self.action(self.action_args), bg='white', font=('Helvetica', 14),
                                compound='left')
        button.grid(row=self.row, column=self.colum, sticky='we', padx=10, pady=10, ipadx=10)
        return button


class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)

        self.root.title("Launcher")
        self.root.configure(bg='white')

        self._load_items()
        self._create_widgets()

    def _convert_image(self, path: str, x_size: int = 32, y_size: int = 32):
        """
        Convert Image
        :param path: Path to icon
        :param x_size: size x
        :param y_size: size y
        :return: converted image
        """
        tmp_icon = Image.open(path)
        tmp_icon = tmp_icon.resize((x_size, y_size), Image.LANCZOS)
        return ImageTk.PhotoImage(tmp_icon)

    def _load_items(self):
        self.notepad_icon_tk = self._convert_image(r'images/notepad.png')
        self.calc_icon_tk = self._convert_image(r'images/calculator.png')
        self.stackoverflow_icon_tk = self._convert_image(r'images/stackoverflow.png')
        self.youtube_icon_tk = self._convert_image(r'images/youtube.png', 64)
        self.github_icon_tk = self._convert_image(r'images/github.png')
        self.python_icon_tk = self._convert_image(r'images/python.png')
        self.photoshop_icon_tk = self._convert_image(r'images/photoshop.png')
        self.settings_icon_tk = self._convert_image(r'images/settings.png')
        self.exit_icon_tk = self._convert_image(r'images/exit.png')
        self.explorer_icon_tk = self._convert_image(r'images/explorer.png')
        self.icon_icon_tk = self._convert_image(r'images/icon.png')
        self.paint_icon_tk = self._convert_image(r'images/paint.png')
        self.size_icon_tk = self._convert_image(r'images/size.png')
        self.code_pepega_club_icon = self._convert_image(r'images/logo.png')
        self.uploadsystems_icon = self._convert_image(r'images/uploadsystems.png')
        self.transmission_icon=self._convert_image(r'images/Transmission_icon.png')
        self.nextcloud_icon = self._convert_image(r'images/nextcloud.png',48)

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
        self.mainframe.configure(bg='white')
        self.mainframe.grid(row=0, padx=10, pady=10)

        self.apps_label = tkinter.Label(self.mainframe, text="Приложения", bg='white', fg='black',
                                        font=('Helvetica', 18))
        self.apps_label.grid(row=0, column=0, columnspan=2, sticky="we")

        self.notepad_button = Button(self.mainframe, text="Notepad", icon=self.notepad_icon_tk,
                                     action=self._run_program,
                                     action_args='notepad.exe', row=1, colum=0)
        self.paint_button = Button(self.mainframe, text="Paint", icon=self.paint_icon_tk, action=self._run_program,
                                   action_args="mspaint.exe", row=1, colum=1)
        self.calc_button = Button(self.mainframe, text="Calculator", icon=self.calc_icon_tk,
                                  action=self._run_program,
                                  action_args='calc.exe', row=2, colum=0)
        self.browser_button = Button(self.mainframe, text="Browser", icon=self.explorer_icon_tk,
                                     action=self._run_browser,
                                     action_args='https://google.com', row=2, colum=1)

        self.browser_label = tkinter.Label(self.mainframe, text="Сайты", bg='white', fg='black',
                                           font=('Helvetica', 18))
        self.browser_label.grid(row=3, column=0, columnspan=2, sticky="we")

        self.github_button = Button(self.mainframe, text="GitHub", icon=self.github_icon_tk, action=self._run_browser,
                                    action_args="https://github.com", row=4, colum=0)
        self.python_button = Button(self.mainframe, text="Python", icon=self.python_icon_tk, action=self._run_browser,
                                    action_args="https://python.org", row=4, colum=1)
        self.stackoverflow_button = Button(self.mainframe, text="StackOverFlow", icon=self.stackoverflow_icon_tk,
                                           action=self._run_browser,
                                           action_args="https://stackoverflow.com", row=5, colum=0)
        self.youtube_button = Button(self.mainframe, text="Youtube", icon=self.youtube_icon_tk,
                                     action=self._run_browser,
                                     action_args="https://youtube.com", row=5, colum=1)
        self.pepega_button = Button(self.mainframe, text="Pepega.club", icon=self.code_pepega_club_icon, row=6, colum=0,
                                    action=self._run_browser, action_args="https://code.pepega.club")
        self.nextcloud_button = Button(self.mainframe, text="NextCloud", icon=self.nextcloud_icon, row=6, colum=1,
                                    action=self._run_browser, action_args="https://nextcloud.nexy.one")
        self.transmission_button = Button(self.mainframe, text="Transmission", icon=self.transmission_icon, row=7, colum=0,
                                    action=self._run_browser, action_args="https://transmission.dontmover.ru")
        self.zipline_button = Button(self.mainframe, text="ZipLine", icon=self.uploadsystems_icon, row=7, colum=1,
                                    action=self._run_browser, action_args="https://i.nexy.one")


if __name__ == '__main__':
    root = tkinter.Tk()
    a = LauncherApp(root)
    root.mainloop()
