"""This module is for the translation mapping data of the
following document:

Document file: display_on_jupyter.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# display_on_jupyter interface':
    '',

    'This page explains the `display_on_jupyter` function interface.':
    '',

    '## What interface is this?':
    '',

    'The `display_on_jupyter` interface displays the apysc HTML on the Jupyter.':  # noqa
    '',

    '## Requirements':
    '',

    'This interface requires the Jupyter library. Therefore, if you haven\'t installed Jupyter, you need to install it before going on (e.g., `pip install notebook`).\n\nFor more information, please see:\n\n- [Installing the Jupyter Software](https://jupyter.org/install)\n\nAlso, this interface uses the `IPython.display.IFrame` interface. If you encountered that interface error, please update the Jupyter version.':  # noqa
    '',

    '## Notes':
    '',

    '- Jupyter on the VS Code is not supported currently (since the VS code restriction).\n- Jupyter notebook and JupyterLab are supported.':  # noqa
    '',

    '## Basic usage':
    '',

    'You can use the `display_on_jupyter` interface to display an output HTML instead of the `save_overall_html` function.\n\nThis interface requires the `html_file_name` argument to be unique if you need to output multiple HTML. Otherwise, this interface overwrites the HTML file:':  # noqa
    '',

    '```py\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\')\nsprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color=\'#f0a\')\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.display_on_jupyter(html_file_name=\'jupyter_sample_1.html\')\n```':  # noqa
    '',

    '![](_static/jupyter_notebook_interface.png)\n\nAlso, this interface can use on the JupyterLab:\n\n![](_static/jupyterlab_interface.png)':  # noqa
    '',

    '## display_on_jupyter API':
    '',

    '<!-- Docstring: apysc._jupyter.jupyter_util.display_on_jupyter -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `display_on_jupyter(html_file_name:str, *, minify:bool=True) -> None`<hr>\n\n**[Interface summary]** Save the overall HTML and display it on the Jupyter.<hr>\n\n**[Parameters]**\n\n- `html_file_name`: str, default \'index.html\'\n  - The output HTML file name.\n- `minify`: bool, default True\n  - Boolean value whether minify a HTML or not. False setting is useful when debugging.\n\n<hr>\n\n**[Notes]**\n\nCurrently, this interface does not support Jupyter on the VS Code. This interface requires the Jupyter library (e.g., `notebook` package).':  # noqa
    '',

}
