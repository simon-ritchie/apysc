"""This module is for the translation mapping data of the
following document:

Document file: stage.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Stage':
    '',

    'This page explains the `Stage` class.':
    '',

    '## What is the Stage?':
    '',

    'The `Stage` is the apysc overall drawing area (like a viewport, canvas, or something else) and contains all elements.\n\nYou must create the `Stage` at the first of the apysc project (this runs cleaning up internal data and files).':  # noqa
    '',

    '## Create stage':
    '',

    'Creating stage is simple, like this:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage()\n```':  # noqa
    '',

    '':
    '',

    '## Stage background color setting':
    '',

    '`Stage` class has a `background_color` option, which changes the stage\'s background color.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'stage_background_color/\')\n```':  # noqa
    '',

    'This will create HTML with black background stage, as follows:\n\n<iframe src="static/stage_background_color/index.html" width="300" height="185"></iframe>':  # noqa
    '',

    '## Stage size setting':
    '',

    'Stage class has options to set stage width and stage height (arguments of `stage_width` and `stage_height`). These settings change stage sizes.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=500, stage_height=50,\n    background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nap.save_overall_html(\n    dest_dir_path=\'stage_size/\')\n```':  # noqa
    '',

    'The Previous script will create a horizontal stage, as follows:\n\n<iframe src="static/stage_size/index.html" width="500", height="50"></iframe>':  # noqa
    '',

    '## Stage element id setting':
    '',

    'Stage element id (HTML id) can be set by `stage_elem_id` argument. If you don\'t specify this, the apysc sets any unique id (based on created timestamp, like `stage_12345...`).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    background_color=\'#333\',\n    stage_elem_id=\'line_chart_1\')\n```':  # noqa
    '',

    'This option is useful when using the apysc project multiple times (for an easily identifiable ID) or version control.':  # noqa
    '',

    '## Stage class constructor API':
    '',

    '<!-- Docstring: apysc._display.stage.Stage.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, *, stage_width:int=300, stage_height:int=185, background_color:str=\'#ffffff\', add_to:str=\'body\', stage_elem_id:Union[str, NoneType]=None) -> None`<hr>\n\n**[Interface summary]** Create Stage (overall viewport) instance.<hr>\n\n**[Parameters]**\n\n- `stage_width`: int, default 300\n  - Stage width.\n- `stage_height`: int, default 185\n  - Stage height\n- `background_color`: str, default \'#ffffff\'\n  - Hexadecimal background color string.\n- `add_to`: str, default \'body\'\n  - Specification of element to add stage. Unique tag (e.g., \'body\') or ID selector (e.g., \'#any-unique-elem\') is acceptable.\n- `stage_elem_id`: str or None, optional\n  - ID attribute set to stage html element (e.g., \'line-graph\'). If None is set, random integer will be applied.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500, stage_height=300,\n...     background_color=\'#333\', stage_elem_id=\'sales_chart\')\n```':  # noqa
    '',

    '':
    '',

    '## stage_elem_id property API':
    '',

    '<!-- Docstring: apysc._display.stage.Stage.stage_elem_id -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get stage\'s html element id.<hr>\n\n**[Returns]**\n\n- `stage_elem_id`: str\n  - Stage\'s html element id (not including class or id symbol). e.g., \'line-graph\'\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage(\n...     stage_width=500, stage_height=300,\n...     background_color=\'#333\', stage_elem_id=\'sales_chart\')\n>>> stage.stage_elem_id\n\'sales_chart\'\n```':  # noqa
    '',

    '':
    '',

    '## add_child API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.add_child -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `add_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>\n\n**[Interface summary]** Add display object child to this instance.<hr>\n\n**[Parameters]**\n\n- `child`: DisplayObject\n  - Child instance to add.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite_1: ap.Sprite = ap.Sprite()\n>>> sprite_1.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite_2: ap.Sprite = ap.Sprite()\n>>> sprite_2.add_child(rectangle)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [add_child and remove_child interfaces document](https://simon-ritchie.github.io/apysc/add_child_and_remove_child.html)':  # noqa
    '',

    '## remove_child API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.remove_child -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `remove_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>\n\n**[Interface summary]** Remove display object child from this instance.<hr>\n\n**[Parameters]**\n\n- `child`: DisplayObject\n  - Child instance to remove.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite.graphics.remove_child(rectangle)\n>>> print(rectangle.parent)\nNone\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [add_child and remove_child interfaces document](https://simon-ritchie.github.io/apysc/add_child_and_remove_child.html)':  # noqa
    '',

    '## contains API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.contains -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `contains(self, child:apysc._display.display_object.DisplayObject) -> apysc._type.boolean.Boolean`<hr>\n\n**[Interface summary]** Get a boolean whether this instance contains a specified child.<hr>\n\n**[Parameters]**\n\n- `child`: DisplayObject\n  - Child instance to check.\n\n<hr>\n\n**[Returns]**\n\n- `result`: Boolean\n  - If this instance contains a specified child, this method returns True.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> sprite.graphics.contains(rectangle)\nBoolean(True)\n\n>>> rectangle.remove_from_parent()\n>>> sprite.graphics.contains(rectangle)\nBoolean(False)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [contains interface document](https://simon-ritchie.github.io/apysc/contains.html)':  # noqa
    '',

    '## num_children property API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.num_children -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current children\'s number.<hr>\n\n**[Returns]**\n\n- `num_children`: int\n  - Current children number.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50)\n>>> sprite.graphics.num_children\nInt(2)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [num_children interface document](https://simon-ritchie.github.io/apysc/num_children.html)':  # noqa
    '',

    '## get_child_at API':
    '',

    '<!-- Docstring: apysc._display.child_interface.ChildInterface.get_child_at -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `get_child_at(self, index:Union[int, apysc._type.int.Int]) -> apysc._display.display_object.DisplayObject`<hr>\n\n**[Interface summary]** Get child at a specified index.<hr>\n\n**[Parameters]**\n\n- `index`: int or Int\n  - Child\'s index (start from 0).\n\n<hr>\n\n**[Returns]**\n\n- `child`: DisplayObject\n  - Target index child instance.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\', alpha=0.5)\n>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=150, y=50, width=50, height=50)\n>>> child_at_index_1: ap.DisplayObject = (\n...     sprite.graphics.get_child_at(1))\n>>> child_at_index_1 == rectangle_2\nTrue\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [get_child_at interface document](https://simon-ritchie.github.io/apysc/get_child_at.html)':  # noqa
    '',

}
