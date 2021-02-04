"""Files' common utilities implementation.
"""

import shutil
import os


def empty_directory(directory_path: str) -> None:
    """
    Empty specified directory.

    Parameters
    ----------
    directory_path : str
        Directory path to empty. This folder itself will not be
        removed.
    """
    if os.path.isdir(directory_path):
        shutil.rmtree(directory_path, ignore_errors=True)
    os.makedirs(directory_path, exist_ok=True)


def read_txt(file_path: str) -> str:
    """
    Read specified file's text.

    Parameters
    ----------
    file_path : str
        File path to read.

    Returns
    -------
    txt : str
        Target file's text.
    """
    with open(file_path, 'r') as f:
        txt: str = f.read()
    return txt


def save_plain_txt(txt: str, file_path: str) -> None:
    """
    Save plain text string to file.

    Parameters
    ----------
    txt : str
        Plain text string to save.
    file_path : str
        Destination file path.
    """
    with open(file_path, 'w') as f:
        f.write(txt)
