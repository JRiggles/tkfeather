import tkinter as tk
from idlelib.tooltip import Hovertip


def showcase() -> None:
    """tkfeather showcase example app"""
    from .tkfeather import Feather

    root = tk.Tk()
    root.config(background='whitesmoke')
    root.resizable(False, False)
    root.title('tkfeather showcase')
    app_icon = Feather('feather', size=16)
    root.iconphoto(True, app_icon.icon)  # type: ignore

    icons_dict = {
        name: Feather(name).icon for name in Feather.icons_available()
    }

    for index, (name, icon) in enumerate(icons_dict.items()):
        row, column = divmod(index, 16)
        label = tk.Label(
            root,
            background='whitesmoke',
            image=icon,  # type: ignore
        )
        Hovertip(
            label,
            text=name,
            hover_delay=333,
            foreground='whitesmoke',
            background='#16161b'
        )
        label.grid(row=row, column=column, ipadx=4, ipady=4, sticky='w')

    root.mainloop()


if __name__ == '__main__':  # example icon showcase app!
    showcase()
