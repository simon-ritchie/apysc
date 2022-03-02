"""This module is for the translation mapping data of the
following document:

Document file: dblclick.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Double click interface':
    '',

    'This page explains the `dblclick` (double-click) interface.':
    '',

    '## What interface is this?':
    '',

    'The `dblclick` interface binds the double-click event to any `DisplayObject` instance (e.g., `Sprite`\\, `Rectangle`\\, and so on). If you double-click on that instance, this interface calls the registered handler function.':  # noqa
    '',

    '## See also':
    '',

    'The following page describes the basic mouse event interfaces.\n\n- [Basic mouse event interfaces](mouse_event_basic.md)':  # noqa
    '',

    '## Basic usage of the dblclick interface':
    '',

    'Each `DisplayObject` instance has the `dblclick` method, and you can bind handlers by that.\n\nThe following example binds the double-click event handler to the rectangle. If you double-click on that instance, the rectangle color changes from cyan to magenta.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when double-clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.dblclick(on_double_click)\n\nap.save_overall_html(\n    dest_dir_path=\'./dblclick_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/dblclick_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Basic usage of the unbind_dblclick interfaces':
    '',

    'The `unbind_dblclick` interface can remove the single binded double-click event from a `DisplayObject` instance. The `unbind_dblclick_all` interface removes all double-click events.\n\nThe following example removes the double click event by the `unbind_dblclick` method. If you double-click the rectangle, nothing happens.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when double-clicked.\n\n    Parameters\n    ----------\n    e : ap.MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.dblclick(on_double_click)\nrectangle.unbind_dblclick(on_double_click)\n\nap.save_overall_html(\n    dest_dir_path=\'./unbind_dblclick_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/unbind_dblclick_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## dblclick API':
    '',

    '<!-- Docstring: apysc._event.double_click_interface.DoubleClickInterface.dblclick -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `dblclick(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>\n\n**[Interface summary]** Add a double-click event listener setting.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Callable that would be called when double-clicking this instance.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler.\n\n<hr>\n\n**[Returns]**\n\n- `name`: str\n  - Handler\'s name.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## unbind_dblclick API':
    '',

    '<!-- Docstring: apysc._event.double_click_interface.DoubleClickInterface.unbind_dblclick -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_dblclick(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>\n\n**[Interface summary]** Unbind a specified handler\'s double click event.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Unbinding target Callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_dblclick(on_double_click)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```':  # noqa
    '',

    '':
    '',

    '## unbind_dblclick_all API':
    '',

    '<!-- Docstring: apysc._event.double_click_interface.DoubleClickInterface.unbind_dblclick_all -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_dblclick_all(self) -> None`<hr>\n\n**[Interface summary]** Unbind all double click events.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_double_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_dblclick_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.dblclick(on_double_click)\n```':  # noqa
    '',

}
