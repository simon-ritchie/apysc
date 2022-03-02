"""This module is for the translation mapping data of the
following document:

Document file: quick_start.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Quick start guide':
    '',

    'This page explains the first step of the apysc library journey.':
    '',

    '## Installing':
    '',

    'To use apysc library Python 3.6 or the later version is required.\n\nYou can use the pip command to install apysc.':  # noqa
    '',

    '```\n$ pip install apysc\n```':
    '',

    '':
    '',

    '## Create stage and export HTML':
    '',

    '`Stage` instance is apysc\'s space for displaying each graphics. You can set arguments of `stage_width` for width setting, `stage_height` for height setting, and `background_color` for background.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage = ap.Stage(stage_width=300, stage_height=180, background_color=\'#333\')\n```':  # noqa
    '',

    'Then you can export each HTML and js file by the `save_overall_html` function (in this case, that code displays only the black background stage).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=300, stage_height=180, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nap.save_overall_html(\n    dest_dir_path=\'quick_start_stage_creation/\')\n```':  # noqa
    '',

    'This code will create each HTML and js files to `dest_dir_path`. You can confirm an exported result by opening `index.html` (`quick_start_stage_creation/index.html`), as follows:\n\n<iframe src="static/quick_start_stage_creation/index.html" width="300" height="180"></iframe>':  # noqa
    '',

    '## Add sprite container and vector graphics':
    '',

    'The `Sprite` class is the container object of each display object, and it can make vector graphics with the `graphics` property.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=250, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\n\n# Draw polyline vector graphics.\nsprite.graphics.line_style(color=\'#fff\', thickness=3)\nsprite.graphics.move_to(x=50, y=50)\nsprite.graphics.line_to(x=100, y=50)\nsprite.graphics.line_to(x=50, y=100)\nsprite.graphics.line_to(x=100, y=100)\n\n# Draw rectangle vector graphic.\nsprite.graphics.begin_fill(color=\'#0af\')\nsprite.graphics.draw_rect(x=150, y=50, width=50, height=50)\n\nap.save_overall_html(\n    dest_dir_path=\'quick_start_sprite_graphics/\')\n```':  # noqa
    '',

    '<iframe src="static/quick_start_sprite_graphics/index.html" width="250" height="150"></iframe>\n\nPlease see each interface documentation page for more details of `Sprite` and `Graphics`\\.':  # noqa
    '',

    '## See also':
    '',

    '- [Sprite class](sprite.md)\n- [Draw interfaces abstract](draw_interfaces_abstract.md)':  # noqa
    '',

}
