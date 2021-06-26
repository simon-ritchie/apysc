"""
The module that is implemented each Jupyter interface and definition.
"""

from apysc._display.stage import Stage


def display_on_jupyter(
        stage: Stage,
        html_file_name: str,
        dest_dir_path: str = './',
        minify: bool = True) -> None:
    """
    Save the overall HTML and display it on the Jupyter.

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

    from apysc import save_overall_html
    save_overall_html(
        dest_dir_path=dest_dir_path,
        html_file_name=html_file_name,
        minify=minify,
        skip_js_lib_exporting=True,
        embed_js_libs=True)
    display(
        IFrame(src=f'./{html_file_name}',
               width=stage._width._value, height=stage._height._value))
