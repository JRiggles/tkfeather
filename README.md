# tkfeather <img src="tkfeather-white.svg" width=48>

#### tkinter support for [feather icons](https://feathericons.com)
[![Downloads](https://static.pepy.tech/badge/tkfeather)](https://pepy.tech/project/tkfeather)
[![Downloads](https://static.pepy.tech/badge/tkfeather/month)](https://pepy.tech/project/tkfeather)
[![Downloads](https://static.pepy.tech/badge/tkfeather/week)](https://pepy.tech/project/tkfeather)

## Latest Changes
Current version: 1.0.0
- Initial release

## Usage

### Installation
tkfeather can be installed with pip
```
pip install tkfeather
```

### Import

Import tkfeather like so
```
from tkfeather import Feather
````

Once you've imported the `Feather` class, you can instantiate it as many times as you need
```
Feather(name: str, size: int [optional])
```

### Args
- `name: str` - The name of the Feather icon
- `size: int [optional]` - The size of the icon image in pixels, square
(default: 24)

> [!WARNING]
> Sizes smaller than 24px are allowed but aren't recommended as the
icon will become blurred
>
> The minimum allowed `size` is 1, and the maximum allowed `size` is 1024

### Properties
- `Feather.icon` - an `ImageTk.PhotoImage` object for the given Feather
icon

### Class Methods
- `Feather.icons_available()` returns a list with the names of all
available Feather Icons

> [!TIP]
> tkfeather v1.0.0 supports all of the icons available in Feather Icons v4.29.0

### Exceptions
- Passing a `size` value  outside the range of 1 to 1024 will raise a
`ValueError`
- Trying to use an icon that doesn't exist will raise a `FileNotFoundError`

### Example
You must maintain a reference to the Feather instance in a variable in
order to keep the image from being garbage-collected:

```python
# this works
feather = Feather('home')
label = tk.Label(parent, image=feather.icon)
label.pack()
```

If you don't maintain a reference to the image, it won't appear!

```python
# this doesn't work - the label will have no image
label = tk.Label(parent, image=Feather('home').icon)
label.pack()
```

### Packaged Dependencies

- PNG Icons
- Pillow >= 9.2.0

##

### Acknowledgements

Based on **Feather Icons** originally created by Cole Bemis

- https://feathericons.com
- https://github.com/feathericons/feather

Under MIT License
