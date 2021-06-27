"""
The module that is implemented each Jupyter interface and definition.

Mainly the following interfaces are defined:

- display_on_jupyter
    Save the overall HTML and display it on the Jupyter.
- display_on_colaboratory
    Save the overall HTML and display it on the Google Colaboratory.
"""

import os

from apysc._display.stage import Stage


def _save_overall_html(
        html_file_name: str, dest_dir_path: str,
        minify: bool) -> None:
    """
    Save the overall HTML file.

    Parameters
    ----------
    html_file_name : str, default 'index.html'
        The output HTML file name.
    dest_dir_path : str
        Destination directory path to save HTML.
    minify : bool, default True
        Boolean value whether minify a HTML or not.
    """
    from apysc import save_overall_html
    save_overall_html(
        dest_dir_path=dest_dir_path,
        html_file_name=html_file_name,
        minify=minify,
        skip_js_lib_exporting=True,
        embed_js_libs=True,
        verbose=0)


def display_on_jupyter(
        stage: Stage,
        html_file_name: str,
        dest_dir_path: str = './',
        minify: bool = True) -> None:
    """
    Save the overall HTML and display it on the Jupyter.

    Notes
    -----
    Currently not supported the Jupyter on the VS Code.

    Parameters
    ----------
    stage : Stage
        Target stage instance.
    html_file_name : str, default 'index.html'
        The output HTML file name.
    dest_dir_path : str
        Destination directory path to save HTML.
    minify : bool, default True
        Boolean value whether minify a HTML or not.
        False setting is useful when debugging.

    Notes
    -----
    This interface requires the Jupyter library (e.g., `notebook` package).
    """
    from IPython.display import IFrame
    from IPython.display import display

    _save_overall_html(
        html_file_name=html_file_name, dest_dir_path=dest_dir_path,
        minify=minify)
    display(
        IFrame(src=f'./{html_file_name}',
               width=stage._width._value, height=stage._height._value))


def display_on_colaboratory(
        html_file_name: str,
        dest_dir_path: str = './',
        minify: bool = True) -> None:
    """
    Save the overall HTML and display it on the Google Colaboratory.

    Parameters
    ----------
    html_file_name : str, default 'index.html'
        The output HTML file name.
    dest_dir_path : str
        Destination directory path to save HTML.
    minify : bool, default True
        Boolean value whether minify a HTML or not.
        False setting is useful when debugging.
    """
    from IPython.display import HTML
    from IPython.display import display

    from apysc._file import file_util
    _save_overall_html(
        html_file_name=html_file_name, dest_dir_path=dest_dir_path,
        minify=minify)
    file_path: str = os.path.join(dest_dir_path, html_file_name)
    html_str: str = file_util.read_txt(file_path=file_path)
    display(HTML(html_str))
