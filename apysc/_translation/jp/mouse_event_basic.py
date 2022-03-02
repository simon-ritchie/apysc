"""This module is for the translation mapping data of the
following document:

Document file: mouse_event_basic.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Basic mouse event interfaces':
    '',

    'This page explains the basic mouse event interfaces, like the `this` attribute.':  # noqa
    '',

    '## Basic binding usage':
    '',

    'Each mouse event binding interface accepts `handler` and `options` arguments. The `handler` argument is each interface\'s callable object when event dispatching.\n\nThe `options` argument is an optional parameter dictionary to be passed to the handler. You can skip this argument.\n\nFor instance, you can set the `click` event as follows:':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    # Change the clicked rectangle color to the passed color.\n    rectangle: ap.Rectangle = e.this\n    color: ap.String = ap.String(options[\'color\'])\n    rectangle.fill_color = color\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {\'color\': \'#f0a\'}\nrectangle.click(\n    handler=on_rectangle_click, options=options)\n\nap.save_overall_html(\n    dest_dir_path=\'mouse_event_basic_basic_binding_usage/\')\n```':  # noqa
    '',

    'If you click the rectangle, the handler changes the rectangle color to the specified options color.\n\n<iframe src="static/mouse_event_basic_basic_binding_usage/index.html" width="150" height="150"></iframe>\n\nThere are many mouse events binding interfaces, such as the `click`\\, `mousedown`\\, `mouseup`\\, `mouseover`\\, `mouseout`\\, and `mousemove` that the `DisplayObject` instance has.':  # noqa
    '',

    '## Basic unbinding usage':
    '',

    'Each `DisplayObject` instance has the `unbind_<event_name>` interfaces, for example, `unbind_click` or `unbind_mousedown` or something else.\n\nThese interfaces can unbind the single handler setting (remove binding setting).\n\nFor example, the following code unbinds the click event, so the interface doesn\'t call the handler function.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef on_rectangle_click(e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    # Change the clicked rectangle color to the passed color.\n    rectangle: ap.Rectangle = e.this\n    color: ap.String = ap.String(options[\'color\'])\n    rectangle.fill_color = color\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {\'color\': \'#f0a\'}\nrectangle.click(\n    handler=on_rectangle_click, options=options)\n\nrectangle.unbind_click(handler=on_rectangle_click)\n\nap.save_overall_html(\n    dest_dir_path=\'mouse_event_basic_basic_unbinding_usage/\')\n```':  # noqa
    '',

    'When you click the following rectangle, nothing happens.\n\n<iframe src="static/mouse_event_basic_basic_unbinding_usage/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Unbind all event handlers':
    '',

    'Sometimes, it is helpful to unbind specific all the events at once. For example, each event interface has the `unbind_<event_name>_all` method (e.g., `unbind_click_all`). It can unbind all event handlers from that instance.\n\nThe following code calls the `unbind_click_all` method and removes all handler settings.':  # noqa
    '',

    '```py\n# runnable\nfrom typing_extensions import TypedDict\n\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\nclass _ColorOptions(TypedDict):\n    color: str\n\n\ndef change_color_on_rectangle_click(\n        e: ap.MouseEvent, options: _ColorOptions) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    color: ap.String = ap.String(options[\'color\'])\n    rectangle.fill_color = color\n\n\ndef change_x_on_rectangle_click(\n        e: ap.MouseEvent, options: dict) -> None:\n    """\n    The handler that the rectangle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle: ap.Rectangle = e.this\n    rectangle.x += 50\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\noptions: _ColorOptions = {\'color\': \'#f0a\'}\nrectangle.click(\n    handler=change_color_on_rectangle_click, options=options)\nrectangle.click(handler=change_x_on_rectangle_click)\n\nrectangle.unbind_click_all()\n\nap.save_overall_html(\n    dest_dir_path=\'mouse_event_basic_unbind_all_event_handlers/\')\n```':  # noqa
    '',

    'Nothing happens when clicking the rectangle (no color change and no x-coordinate change).\n\n<iframe src="static/mouse_event_basic_unbind_all_event_handlers/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## Handler argument names and types':
    '',

    'Handler function (or method) first argument requires the type of the `MouseEvent`\\.\n\nAlso, a second argument name is required to be `options`\\. This argument type becomes `dict`\\. If you skip options argument specification at binding the event, then this argument becomes a blank dictionary (`{}`).':  # noqa
    '',

    '## MouseEvent this attribute':
    '',

    'The `MouseEvent` instance has the `this` attribute, which becomes an event target instance. So, if you bind the click event to the rectangle instance, the `this` attribute becomes that rectangle instance.':  # noqa
    '',

    '## MouseEvent generic type settings':
    '',

    'Suppose you know that you only use one of the handlers by an instance of a particular type. In that case, you can set generic type settings to the `MouseEvent` type annotation (e.g., `MouseEvent[Rectangle]`).\n\nThis setting is helpful to determine the `this` attribute type, and the type-checking library, such as the `mypy` or `Pylance`\\, checks the instance type.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_rectangle_mousedown(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousedown.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    rectangle = e.this\n    rectangle.x += 50\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.mousedown(handler=on_rectangle_mousedown)\n```':  # noqa
    '',

    '':
    '',

    '## MouseEvent stage_x and stage_y attributes':
    '',

    'MouseEvent instance has the `stage_x` and `stage_y` attributes. These attributes are absolute coordinates from the upper-left position of the stage.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_mousemove(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    ap.trace(\'stage_x:\', e.stage_x, \'stage_y:\', e.stage_y)\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=100, width=50, height=50)\nrectangle.mousemove(handler=on_mousemove)\n\nap.save_overall_html(\n    dest_dir_path=\'mouse_event_basic_stage_x_and_stage_y\')\n```':  # noqa
    '',

    'If you open the DevTools console on Chrome (press F12) and move the mouse cursor on the following rectangle, you can check the `stage_x` and `stage_y` coordinates. The previous code positions the rectangle at `(50, 100)`, so the `stage_x` becomes the range of 50 to 100, and `stage_y` becomes 100 to 150.\n\n<iframe src="static/mouse_event_basic_stage_x_and_stage_y/index.html" width="150" height="200"></iframe>':  # noqa
    '',

    '## MouseEvent local_x and local_y attributes':
    '',

    'MouseEvent instance also has `local_x` and `local_y` attributes. These attributes are the local coordinates from the event registered instance position.\n\nThe following example shows that local_x and local_y become the coordinates in the rectangle area. Both of the `local_x` and `local_y` become a range of 0 to 50 because the rectangle size is 50-pixel.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=150,\n    stage_height=150,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\n\n\ndef on_mousemove(\n        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the rectangle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments.\n    """\n    ap.trace(\'local_x:\', e.local_x, \'local_y:\', e.local_y)\n\n\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(\n    x=50, y=50, width=50, height=50)\nrectangle.mousemove(handler=on_mousemove)\n\nap.save_overall_html(\n    dest_dir_path=\'mouse_event_basic_local_x_and_local_y\')\n```':  # noqa
    '',

    'Please check on Chrome DevTools (press F12) and move the mouse cursor on the following rectangle.\n\n<iframe src="static/mouse_event_basic_local_x_and_local_y/index.html" width="150" height="150"></iframe>':  # noqa
    '',

    '## See also':
    '',

    '- [Click interface](click.md)\n- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)\n- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)\n- [Mousemove interface](mousemove.md)':  # noqa
    '',

    '## stage_x property API':
    '',

    '<!-- Docstring: apysc._event.mouse_event.MouseEvent.stage_x -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get the x-coordinate of the stage reference.<hr>\n\n**[Returns]**\n\n- `x`: Int\n  - x-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '',

    '':
    '',

    '## stage_y property API':
    '',

    '<!-- Docstring: apysc._event.mouse_event.MouseEvent.stage_y -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get the y-coordinate of the stage reference.<hr>\n\n**[Returns]**\n\n- `y`: Int\n  - y-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_y: ap.Int = e.stage_y\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '',

    '':
    '',

    '## local_x property API':
    '',

    '<!-- Docstring: apysc._event.mouse_event.MouseEvent.local_x -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a local x-coordinate event listening instance. For example, this value becomes x-coordinate from Sprite\'s left-end position by clicking a Sprite instance.<hr>\n\n**[Returns]**\n\n- `x`: Int\n  - x-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     local_x: ap.Int = e.local_x\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '',

    '':
    '',

    '## local_y property API':
    '',

    '<!-- Docstring: apysc._event.mouse_event.MouseEvent.local_y -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get the local y-coordinate of the event listening instance. For example, this value becomes y-coordinate from Sprite\'s top-end position by clicking a Sprite instance.<hr>\n\n**[Returns]**\n\n- `y`: Int\n  - y-coordinate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousedown(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     local_y: ap.Int = e.local_y\n...     # Do something here with the coordinate.\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousedown(on_mousedown)\n```':  # noqa
    '',

    '':
    '',

    '# this property API':
    '',

    '<!-- Docstring: apysc._event.event.Event.this -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get an instance of listening to this event.<hr>\n\n**[Returns]**\n\n- `this`: VariableNameInterface\n  - Instance that listening this event.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_custom_event(\n...         e: ap.Event[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.fill_color = ap.String(\'#f0a\')\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> e: ap.Event = ap.Event(this=rectangle)\n>>> _ = rectangle.bind_custom_event(\n...     custom_event_type=\'my_custom_event\',\n...     handler=on_custom_event, e=e)\n>>> # Do something here and then trigger the custom event\n>>> rectangle.trigger_custom_event(\n...     custom_event_type=\'my_custom_event\')\n```':  # noqa
    '',

}
