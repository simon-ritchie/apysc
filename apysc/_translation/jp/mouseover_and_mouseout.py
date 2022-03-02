"""This module is for the translation mapping data of the
following document:

Document file: mouseover_and_mouseout.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Mouseover and mouseout interfaces':
    '',

    'This page explains the `mouseover` and `mouseout` interfaces.':
    '',

    '## What interfaces are these?':
    '',

    'The `mouseover` interface binds the event handler. Moreover, this interface calls the handler when a mouse cursor is over on a `DisplayObject` instance. Conversely, the `mouseout` interface also binds and calls the handler when a cursor is out from the `DisplayObject` one.':  # noqa
    '',

    '## See also':
    '',

    'The following page describes the basic mouse event interfaces.\n\n- [Basic mouse event interfaces](mouse_event_basic.md)':  # noqa
    '',

    '## Basic usage of the mouseover and mouseout interfaces':
    '',

    'Each `DisplayObject` instance has the `mouseover` and `mouseout` interfaces, and you can bind handlers by these.\n\nThe following example binds the mouse over and handler and mouse out one to the rectangle. The rectangle color changes when your cursor is over the rectangle. Also, it reverts to the original one when your cursor is outed from the rectangle.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mouseover(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseover.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Change the rectangle fill color to magenta.\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\ndef on_mouseout(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseout.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n\n    # Revert the rectangle fill color.\n    rectangle.fill_color = ap.String(\'#0af\')\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\n# Bind the mouse over and mouse out event handlers to the rectangle.\nrectangle.mouseover(on_mouseover)\nrectangle.mouseout(on_mouseout)\n\nap.save_overall_html(\n    dest_dir_path=\'mouseover_and_mouseout_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/mouseover_and_mouseout_basic_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Unbind Interfaces':
    '',

    'The `unbind_mouseover` and `unbind_mouseout` interfaces unbind each registered handler from the `DisplayObject`\\.\n\nThe following example unbind handlers in the `on_mouseover` and `on_mouseout` functions so that the interface calls these handlers only once.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mouseover(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseover.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n    # Unbind the mouseover handler.\n    rectangle.unbind_mouseover(handler=on_mouseover)\n\n\ndef on_mouseout(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mouseout.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#0af\')\n\n    rectangle.unbind_mouseout(handler=on_mouseout)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\n\nsprite.graphics.begin_fill(color=\'#0af\')\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\n\nrectangle.mouseover(on_mouseover)\nrectangle.mouseout(on_mouseout)\n\nap.save_overall_html(\n    dest_dir_path=\'mouseover_and_mouseout_unbind_interfaces/\')\n```':  # noqa
    '',

    '<iframe src="static/mouseover_and_mouseout_unbind_interfaces/index.html" width="150" height="150"></iframe>\n\nThere are also existing the `unbind_mouseover_all` and `unbind_mouseover_all` interfaces. These interfaces unbind all the handlers from the target `DisplayObject` instance.':  # noqa
    '',

    '## mouseover API':
    '',

    '<!-- Docstring: apysc._event.mouse_over_interface.MouseOverInterface.mouseover -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `mouseover(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>\n\n**[Interface summary]** Add mouse over event listener setting.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Callable that would be called when mouse over on this instance.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler.\n\n<hr>\n\n**[Returns]**\n\n- `name`: str\n  - Handler\'s name.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseover(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseout(on_mouseover)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options\' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## unbind_mouseover API':
    '',

    '<!-- Docstring: apysc._event.mouse_over_interface.MouseOverInterface.unbind_mouseover -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mouseover(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>\n\n**[Interface summary]** Unbind a specified handler\'s mouseover event.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Unbinding target Callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseover(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseover(on_mouseover)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseout(on_mouseover)\n```':  # noqa
    '',

    '':
    '',

    '## unbind_mouseover_all API':
    '',

    '<!-- Docstring: apysc._event.mouse_over_interface.MouseOverInterface.unbind_mouseover_all -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mouseover_all(self) -> None`<hr>\n\n**[Interface summary]** Unbind all mouseover events.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseover(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseover_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseout(on_mouseover)\n```':  # noqa
    '',

    '':
    '',

    '## mouseout API':
    '',

    '<!-- Docstring: apysc._event.mouse_out_interface.MouseOutInterface.mouseout -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `mouseout(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>\n\n**[Interface summary]** Add mouse out event listener setting.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Callable that would be called when mouse out on this instance.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler.\n\n<hr>\n\n**[Returns]**\n\n- `name`: str\n  - Handler\'s name.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseout(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseout(on_mouseout)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## unbind_mouseout API':
    '',

    '<!-- Docstring: apysc._event.mouse_out_interface.MouseOutInterface.unbind_mouseout -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mouseout(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>\n\n**[Interface summary]** Unbind a specified handler\'s mouse-out event.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Unbinding target Callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseout(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseout(on_mouseout)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseout(on_mouseout)\n```':  # noqa
    '',

    '':
    '',

    '## unbind_mouseout_all API':
    '',

    '<!-- Docstring: apysc._event.mouse_out_interface.MouseOutInterface.unbind_mouseout_all -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mouseout_all(self) -> None`<hr>\n\n**[Interface summary]** Unbind all mouse out events.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mouseout(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_mouseout_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mouseout(on_mouseout)\n```':  # noqa
    '',

}
