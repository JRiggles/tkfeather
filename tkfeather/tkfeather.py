"""
tkfeather
A tkinter wrapper for Feather Icons by Cole Bemis - https://feathericons.com

MIT License

Copyright (c) 2024-26 John Riggles [sudo_whoami]

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
"""
from functools import cached_property
from pathlib import Path

from PIL import Image, ImageTk


class Feather:
    """
    Import:
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
    >>> label = tk.Label(parent, image=feather.icon)
    >>> label.pack()

    If you don't maintain a reference to the image, it won't appear!
    >>> # this doesn't work - the label will have no image
    >>> label = tk.Label(parent, image=Feather('home').icon)
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

    @cached_property
    def icon(self) -> ImageTk.PhotoImage | None:
        """An `ImageTk.PhotoImage` object for the given Feather icon"""
        return self._icon_image

    @classmethod
    def icons_available(cls) -> list[str]:
        """Return a list containing the names of all available Feather Icons"""
        # NOTE: iterdir keeps including a nonexisting .DS_Store file, so glob
        # it is...
        return sorted([icon.stem for icon in cls._ICONS_DIR.glob('*.png')])
