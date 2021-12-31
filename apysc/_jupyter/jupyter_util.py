"""
The module that is implemented each Jupyter interface and definition.

Mainly the following interfaces are defined:

- display_on_jupyter
    Save the overall HTML and display it on the Jupyter.
- display_on_colaboratory
    Save the overall HTML and display it on the Google Colaboratory.
"""

import os
import shutil
from datetime import datetime
from random import randint

_TMP_ROOT_DIR_PATH: str = './'


def _save_overall_html(*, html_file_name: str, minify: bool) -> None:
    """
    Save the overall HTML file.

    Parameters
    ----------
    html_file_name : str, default 'index.html'
        The output HTML file name.
    minify : bool, default True
        Boolean value whether minify a HTML or not.
    """
    import apysc as ap
    timestamp: float = datetime.now().timestamp()
    random_int: int = randint(10000, 100000)
    dest_dir_path: str = (
        f'{_TMP_ROOT_DIR_PATH}tmp_apysc_jupyter_{timestamp}{random_int}/')
    ap.save_overall_html(
        dest_dir_path=dest_dir_path,
        html_file_name=html_file_name,
        minify=minify,
        skip_js_lib_exporting=True,
        embed_js_libs=True,
        verbose=0)
    src_file_path: str = os.path.join(dest_dir_path, html_file_name)
    shutil.copy(src_file_path, html_file_name)
    shutil.rmtree(dest_dir_path, ignore_errors=True)


def display_on_jupyter(
        html_file_name: str,
        *,
        minify: bool = True) -> None:
    """
    Save the overall HTML and display it on the Jupyter.

    Notes
    -----
    Currently not supported the Jupyter on the VS Code.

    Parameters
    ----------
    html_file_name : str, default 'index.html'
        The output HTML file name.
    minify : bool, default True
        Boolean value whether minify a HTML or not.
        False setting is useful when debugging.

    Notes
    -----
    This interface requires the Jupyter library (e.g., `notebook` package).

    References
    ----------
    - display_on_jupyter interface document
        - https://simon-ritchie.github.io/apysc/display_on_jupyter.html
    """
    from IPython.display import IFrame
    from IPython.display import display

    import apysc as ap

    stage: ap.Stage = ap.get_stage()
    _save_overall_html(
        html_file_name=html_file_name,
        minify=minify)
    display(
        IFrame(src=f'./{html_file_name}',
               width=stage._width._value, height=stage._height._value))


def display_on_colaboratory(
        html_file_name: str, *,
        minify: bool = True) -> None:
    """
    Save the overall HTML and display it on the Google Colaboratory.

    Parameters
    ----------
    html_file_name : str, default 'index.html'
        The output HTML file name.
    minify : bool, default True
        Boolean value whether minify a HTML or not.
        False setting is useful when debugging.

    References
    ----------
    display_on_colaboratory interface document
        https://simon-ritchie.github.io/apysc/display_on_colaboratory.html
    """
    from IPython.display import HTML
    from IPython.display import display

    from apysc._file import file_util
    _save_overall_html(
        html_file_name=html_file_name,
        minify=minify)
    html_str: str = file_util.read_txt(file_path=html_file_name)
    display(HTML(html_str))
