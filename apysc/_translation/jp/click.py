"""This module is for the translation mapping data of the
following document:

Document file: click.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Click interface':
    '',

    'This page explains the `click` interface.':
    '',

    '## What interface is this?':
    '',

    'The `click` interface binds the click event to any `DisplayObject` instance (e.g., `Sprite`\\, `Rectangle`\\, and so on). These interfaces call the registered handler function if you mouse down on that instance and mouse up.\n\nConversely, the `unbind_click` interface unbinds the click event from the `DisplayObject` instance.':  # noqa
    '',

    '## See also':
    '',

    'The following page describes basic mouse event interfaces.\n\n- [Basic mouse event interfaces](mouse_event_basic.md)':  # noqa
    '',

    '## Basic usage of the click interface':
    '',

    'Each `DisplayObject` instance has the `click` method, and you can bind handlers by that.\n\nThe following example binds the click event handler to the rectangle.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'click_basic_usage_of_the_click_interface/\')\n```':  # noqa
    '',

    'If you click the following rectangle, the rectangle color becomes the magenta color.\n\n<iframe src="static/click_basic_usage_of_the_click_interface/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Basic usage of the unbind_click interface':
    '',

    'The `unbind_click` interface can remove the binded click event from a `DisplayObject` instance.\n\nThe following example removes the click event by the `unbind_click` method, and nothing happens if you click the rectangle.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\nrectangle.unbind_click(handler=on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'click_basic_usage_of_the_unbind_click_interface/\')\n```':  # noqa
    '',

    '<iframe src="static/click_basic_usage_of_the_unbind_click_interface/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Unbind all the click event handlers':
    '',

    '`unbind_click_all` interface can unbind all the click event handlers from the `DisplayObject` instance.\n\nThe following example removes all the click events by the `unbind_click_all` method (if you click the rectangle, nothing happens).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_click(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.fill_color = ap.String(\'#f0a\')\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.click(handler=on_click)\nrectangle.unbind_click_all()\n\nap.save_overall_html(\n    dest_dir_path=\'click_unbind_all_the_click_event_handlers/\')\n```':  # noqa
    '',

    '<iframe src="static/click_unbind_all_the_click_event_handlers/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## click API':
    '',

    '<!-- Docstring: apysc._event.click_interface.ClickInterface.click -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `click(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>\n\n**[Interface summary]** Add a click event listener setting.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - A callable would be called when clicking this instance.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler.\n\n<hr>\n\n**[Returns]**\n\n- `name`: str\n  - Handler\'s name.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.x += 10\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## unbind_click API':
    '',

    '<!-- Docstring: apysc._event.click_interface.ClickInterface.unbind_click -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_click(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>\n\n**[Interface summary]** Unbind specified handler\'s click event.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Unbinding target Callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_click(on_click)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '',

    '':
    '',

    '## unbind_click_all API':
    '',

    '<!-- Docstring: apysc._event.click_interface.ClickInterface.unbind_click_all -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_click_all(self) -> None`<hr>\n\n**[Interface summary]** Unbind all click events.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n...     rectangle.unbind_click_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '',

}
