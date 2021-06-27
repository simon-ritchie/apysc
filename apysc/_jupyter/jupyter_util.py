"""
The module that is implemented each Jupyter interface and definition.
"""

import os


def display_on_jupyter(
        html_file_name: str,
        dest_dir_path: str = './',
        minify: bool = True) -> None:
    """
    Save the overall HTML and display it on the Jupyter.

    Parameters
    ----------
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
    from IPython.display import HTML
    from IPython.display import display

    from apysc._file import file_util
    from apysc import save_overall_html
    save_overall_html(
        dest_dir_path=dest_dir_path,
        html_file_name=html_file_name,
        minify=minify,
        skip_js_lib_exporting=True,
        embed_js_libs=True,
        verbose=0)
    file_path: str = os.path.join(dest_dir_path, html_file_name)
    html_str: str = file_util.read_txt(file_path=file_path)
    display(HTML(html_str))
