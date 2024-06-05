"""
tkfeather
A tkinter wrapper for Feather Icons by Cole Bemis - https://feathericons.com

MIT License

Copyright (c) 2024 John Riggles [sudo_whoami]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Requires PIL >= 9.2.0
"""
from pathlib import Path
from PIL import Image, ImageTk


class Feather:
    """
    Import:
    >>> import tkfeather

    Or better yet:
    >>> from tkfeather import Feather

    Initialization:
    >>> Feather(name: str, size: int [optional])

    ### Args
    - `name: str` - The name of the Feather icon
    - `size: int [optional]` - The size of the icon image in pixels, square
    (default: 24)

    Note: Sizes smaller than 24px are allowed but aren't recommended as the
    icon will become blurred

    The minimum allowed `size` is 1, and the maximum allowed `size` is 1024

    Passing a `size` value  outside the range of 1 to 1024 will raise a
    `ValueError`

    ### Properties
    - `Feather.icon` - an `ImageTk.PhotoImage` object for the given Feather
    icon

    ### Class Methods
    - `Feather.icons_available()` - returns a list with the names of all
    available Feather Icons

    Trying to use an icon that doesn't exist will raise a `FileNotFoundError`

    ### Usage:
    You must maintain a reference to the Feather instance in a variable in
    order to keep the image from being garbage-collected:
    >>> # this works
    >>> feather = Feather('home')
    >>> label = tk.Label(root, image=feather.icon)
    >>> label.pack()

    If you don't maintain a reference to the image, it won't appear!
    >>> # this doesn't work - the label will have no image
    >>> label = tk.Label(root, image=Feather('home').icon)
    >>> label.pack()
    """

    _ICONS_DIR = Path(__file__).parent / 'icons'

    def __init__(self, name: str, size: int = 24) -> None:
        self._icon_name = name
        self._size = size
        self._icon_path = (
            self._ICONS_DIR.joinpath(self._icon_name).with_suffix('.png')
        )
        self._icon_image = None

        if self._icon_path.exists():
            # cast to int to allow for other numeric arg types
            self._size = int(self._size)
            if self._size < 1 or self._size > 1024:
                raise ValueError('"size" must be between 1 and 1024')
            else:
                with Image.open(self._icon_path) as img:
                    img = img.resize(  # feather icons are square
                        size=(self._size, self._size),
                        resample=Image.Resampling.LANCZOS,
                    )
                self._icon_image = ImageTk.PhotoImage(img)
        else:
            raise FileNotFoundError(
                'The image file for the icon '
                f'"{self._icon_name}" was not found'
            )

    @property
    def icon(self) -> ImageTk.PhotoImage | None:
        """An `ImageTk.PhotoImage` object for the given Feather icon"""
        return self._icon_image

    @classmethod
    def icons_available(cls) -> list[str]:
        """Return a list containing the names of all available Feather Icons"""
        # NOTE: iterdir keeps including a nonexisting .DS_Store file, so glob
        # it is...
        return sorted([icon.stem for icon in cls._ICONS_DIR.glob('*.png')])


# if __name__ == '__main__':  # example icon showcase app!
#     import tkinter as tk

#     root = tk.Tk()
#     root.config(background='whitesmoke')
#     root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())
#     root.resizable(False, False)
#     root.title('tkinter Feather Icons Showcase - Hover icons to see names')
#     app_icon = Feather('feather', size=16)
#     root.iconphoto(True, app_icon.icon)

#     icons_dict = {
#         name: Feather(name).icon for name in Feather.icons_available()
#     }

#     for index, (name, icon) in enumerate(icons_dict.items()):
#         row, column = divmod(index, 41)
#         label = tk.Label(
#             root,
#             background='whitesmoke',
#             # compound='left',
#             foreground='#111111',
#             image=icon,
#             # text=name,
#         )
#         # BUG: Hovertip text not showing up on Mac OS
#         # see https://github.com/python/cpython/issues/120083
#         label.grid(row=row, column=column, ipadx=4, ipady=4, sticky='w')

#     root.mainloop()
