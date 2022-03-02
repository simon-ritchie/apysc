"""This module is for the translation mapping data of the
following document:

Document file: display_on_colaboratory.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# display_on_colaboratory interface':
    '',

    'This page will explain the `display_on_colaboratory` function interface.':  # noqa
    '',

    '## What interface is this?':
    '',

    'The `display_on_colaboratory` interface displays the apysc HTML on the Google Colaboratory.':  # noqa
    '',

    '## Requirements':
    '',

    'You need to install apysc on the Google Colaboratory before going on. A `!` symbol and pip command on the Google Colaboratory installs this library:':  # noqa
    '',

    '```\n!pip install apysc\n```':
    '',

    '':
    '',

    '## Basic usage':
    '',

    'You can use the `display_on_colaboratory` interface to display an output HTML instead of the `save_overall_html` function.\n\nThis interface requires the `html_file_name` argument to be unique if you need to output multiple HTML. Otherwise, it overwrites the HTML file:':  # noqa
    '',

    '```py\nimport apysc as ap\n\nap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\')\nsprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\n\nsprite.graphics.begin_fill(color=\'#f0a\')\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.display_on_colaboratory(html_file_name=\'jupyter_test_1.html\')\n```':  # noqa
    '',

    '![](_static/colaboratory_interface.png)':
    '',

    '## display_on_colaboratory API':
    '',

    '<!-- Docstring: apysc._jupyter.jupyter_util.display_on_colaboratory -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `display_on_colaboratory(html_file_name:str, *, minify:bool=True) -> None`<hr>\n\n**[Interface summary]** Save the overall HTML and display it on Google Colaboratory.<hr>\n\n**[Parameters]**\n\n- `html_file_name`: str, default \'index.html\'\n  - The output HTML file name.\n- `minify`: bool, default True\n  - Boolean value whether minify a HTML or not. False setting is useful when debugging.':  # noqa
    '',

}
