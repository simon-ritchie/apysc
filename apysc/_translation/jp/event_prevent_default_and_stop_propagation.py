"""This module is for the translation mapping data of the
following document:

Document file: event_prevent_default_and_stop_propagation.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Event class prevent_default and stop_propagation interfaces':
    '',

    'This page explains the `Event` class `prevent_default` and `stop_propagation` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `prevent_default` method interface appends the calling expression of the JavaScript `preventDefault` method. This interface prevents the browser default behavior of any event.\n\nThe `stop_propagation` method interface stops an event\'s propagation; for example, the triggered child event does not propagate to a parent event (it ignores the parent event).':  # noqa
    '',

    '## Basic usage of the prevent_default interface':
    '',

    'The `Event` instance and its subclass instance have the `prevent_default` method. The `prevent_default` method requires no arguments, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.prevent_default()\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'event_prevent_default_basic_usage/\')\n```':  # noqa
    '',

    '':
    '',

    '## Basic usage of the stop_propagation interface':
    '',

    'The `Event` instance and its subclass instance have the `stop_propagation` method. The `stop_propagation` method, like the `prevent_default` one, requires no arguments.\n\nThe following example binds the click event to the sprite and rectangle instances. The rectangle (child) click handler calls the `stop_propagation` method, so the sprite (parent) doesn\'t call the click handler:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_rectangle_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    e.stop_propagation()\n    ap.trace(\'The rectangle is clicked!\')\n\n\ndef on_sprite_click(\n        e: ap.MouseEvent[ap.Sprite], options: dict) -> None:\n    """\n    The handler that the sprite calls when clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    ap.trace(\'The sprite is clicked!\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.click(on_sprite_click)\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(on_rectangle_click)\n\nap.save_overall_html(\n    dest_dir_path=\'event_stop_propagation_basic_usage/\')\n```':  # noqa
    '',

    'If you click the following rectangle, the only message of `The rectangle is clicked!` is displayed browser console (please press the F12 key). Also, the sprite console message is not displayed.\n\n<iframe src="static/event_stop_propagation_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## prevent_default API':
    '',

    '<!-- Docstring: apysc._event.prevent_default_interface.PreventDefaultInterface.prevent_default -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `prevent_default(self) -> None`<hr>\n\n**[Interface summary]** Prevent event\'s default behavior.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     e.prevent_default()\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseup_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '',

    '':
    '',

    '## stop_propagation API':
    '',

    '<!-- Docstring: apysc._event.stop_propagation_interface.StopPropagationInterface.stop_propagation -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `stop_propagation(self) -> None`<hr>\n\n**[Interface summary]** Stop event propagation.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_click(e: ap.MouseEvent, options: dict) -> None:\n...     e.stop_propagation()\n...     ap.trace(\'Clicked!\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = sprite.click(on_click)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '',

}
