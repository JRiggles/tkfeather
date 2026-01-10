"""tkfeather - Feather icons for tkinter"""
__all__ = ['tkfeather']
__author__ = 'John Riggles <jriggles@icloud.com>'
__copyright__ = '2024-26 John Riggles [sudo_whoami]'
__license__ = 'MIT'

from .tkfeather import Feather  # noqa


if __name__ == "__main__":
    from .showcase import showcase
    showcase()
