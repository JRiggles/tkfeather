# tkfeather <img src="assets/tkfeather-white.svg" width=48>

<img src="screenshots/showcase.png" alt="an application window showing the available icons in tkfeather" />

#### tkinter support for [feather icons](https://feathericons.com)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/tkfeather?period=total&units=ABBREVIATION&left_color=BLACK&right_color=RED&left_text=downloads)](https://pepy.tech/projects/simple-color-palette)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/tkfeather?period=monthly&units=ABBREVIATION&left_color=BLACK&right_color=BRIGHTGREEN&left_text=downloads%2Fmonth)](https://pepy.tech/projects/simple-color-palette)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/tkfeather?period=weekly&units=ABBREVIATION&left_color=BLACK&right_color=BLUE&left_text=downloads%2Fweek)](https://pepy.tech/projects/simple-color-palette)

## Latest Changes
Current version: 1.0.1
- Fixes for and improvements to the example showcase
- Minor performace improvements

## Usage

### Installation
tkfeather can be installed with pip
```shell
pip install tkfeather
```

### Import

Import tkfeather like so
```python
from tkfeather import Feather
````

Once you've imported the `Feather` class, you can instantiate it as many times as you need
```python
Feather(name: str, size: int [optional])
```

### Parameters
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
> tkfeather v1.0.1 supports all of the icons available in Feather Icons v4.29.0

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

## Showcase

To see an example application showcasing all of the available icons, you can run the `tkfeather.showcase` like so:

```shell
python3 -m tkfeather.showcase
```

## Packaged Dependencies

- PNG Icons
- Pillow >= 9.2.0

## Acknowledgements

Based on **Feather Icons** originally created by Cole Bemis, used under the MIT License

- https://feathericons.com
- https://github.com/feathericons/feather
