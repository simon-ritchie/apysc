"""This module is for the translation mapping data of the
following document:

Document file: mousedown_and_mouseup.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Mousedown and mouseup interfaces':
    '',

    'This page explains the `mousedown` and `mouseup` interfaces.':
    '',

    '## What interfaces are these?':
    '',

    'The `mousedown` interface binds the event handler that the interface calls when a user mouse downed on a `DisplayObject` instance. Conversely, the `mouseup` interface binds the event handler that the interface calls when a user mouse upped on a `DisplayObject` one.':  # noqa
    '',

    '## See also':
    '',

    'The following page describes the basic mouse event interfaces:\n\n- [Basic mouse event interfaces](mouse_event_basic.md)':  # noqa
    '',

    '## Basic usage of the mousedown and mouseup interfaces':
    '',

    'Each `DisplayObject` instance has the `mousedown` and `mouseup` method interfaces, and you can bind handlers by these.\n\nThe following example binds the mouse down handler and mouse upped one to the rectangle. The handler changes the rectangle color when the mouse downs and reverts to the original one when the mouse upped.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\ndef on_mouseup(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Bind each handler to the rectangle.\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(\n    dest_dir_path=\'mousedown_and_mouseup_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/mousedown_and_mouseup_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Unbind interfaces':
    '',

    'The `unbind_mousedown` and `unbind_mouseup` interfaces unbind each registered handler from the `DisplayObject`\\.\n\nThe following example unbinds handlers in the `on_mousedown` and `on_mouseup` functions so that the rectangle calls these handlers only once.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousedown(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mousedown(handler=on_mousedown)\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\ndef on_mouseup(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseup.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.unbind_mouseup(handler=on_mouseup)\n    rectangle.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle.mousedown(on_mousedown)\nrectangle.mouseup(on_mouseup)\n\nap.save_overall_html(\n    dest_dir_path=\'mousedown_and_mouseup_unbind_interfaces/\')\n```':  # noqa
    '',

    '<iframe src="static/mousedown_and_mouseup_unbind_interfaces/index.html" width="150" height="150"></iframe>\n\nThere are also existing the `unbind_mousedown_all` and `unbind_mouseup_all` interfaces. These interfaces unbind all the handlers from the target `DisplayObject` instance.':  # noqa
    '',

    '## mousedown API':
    '',

    '<!-- Docstring: apysc._event.mouse_down_interface.MouseDownInterface.mousedown -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `mousedown(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>\n\n**[Interface summary]** Add mouse down event listener setting.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Callable that would be called when mouse down on this instance.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler.\n\n<hr>\n\n**[Returns]**\n\n- `name`: str\n  - Handler\'s name.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## unbind_mousedown API':
    '',

    '<!-- Docstring: apysc._event.mouse_down_interface.MouseDownInterface.unbind_mousedown -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mousedown(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>\n\n**[Interface summary]** Unbind a specified handler\'s mouse down event.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Unbinding target Callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mousedown(on_mousedown)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '',

    '':
    '',

    '## unbind_mousedown_all API':
    '',

    '<!-- Docstring: apysc._event.mouse_down_interface.MouseDownInterface.unbind_mousedown_all -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mousedown_all(self) -> None`<hr>\n\n**[Interface summary]** Unbind all mouse down events.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mousedown_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '',

    '':
    '',

    '## mouseup API':
    '',

    '<!-- Docstring: apysc._event.mouse_up_interface.MouseUpInterface.mouseup -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `mouseup(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>\n\n**[Interface summary]** Add mouse up event listener setting.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Callable that would be called when mouse-up on this instance.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler\n\n<hr>\n\n**[Returns]**\n\n- `name`: str\n  - Handler\'s name.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## unbind_mouseup API':
    '',

    '<!-- Docstring: apysc._event.mouse_up_interface.MouseUpInterface.unbind_mouseup -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mouseup(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>\n\n**[Interface summary]** Unbind a specified handler\'s mouse-up event.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Unbinding target Callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseup(on_mouseup)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```':  # noqa
    '',

    '':
    '',

    '## unbind_mouseup_all API':
    '',

    '<!-- Docstring: apysc._event.mouse_up_interface.MouseUpInterface.unbind_mouseup_all -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mouseup_all(self) -> None`<hr>\n\n**[Interface summary]** Unbind all mouse up events.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseup(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseup_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseup(on_mouseup)\n```':  # noqa
    '',

}
