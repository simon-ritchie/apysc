"""This module is for the translation mapping data of the
following document:

Document file: set_debug_mode.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# set_debug_mode interface':
    '',

    'This page explains the `set_debug_mode` function interface.':
    '',

    '## What interface is this?':
    '',

    'The `set_debug_mode` function interface sets the debug mode setting. This setting appends the debug information (Python function or method calls and arguments information) to the exported HTML.':  # noqa
    '',

    '## Notes':
    '',

    'The debug mode setting appends lots of information to the HTML. As a result, the exporting time becomes long, and the HTML file size becomes large.\n\nAlso, this setting ignores the `minify` setting.':  # noqa
    '',

    '## Basic usage':
    '',

    'After the stage instantiation, you can set the debug mode by the `set_debug_mode` function. This function requires the stage instance since the stage instance resets the settings at first, including the debug mode.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nap.set_debug_mode()\nsprite: ap.Sprite = ap.Sprite()\nint_1: ap.Int = ap.Int(10)\n\nap.save_overall_html(\n    dest_dir_path=\'set_debug_mode_basic_usage/\')\n```':  # noqa
    '',

    'This setting appends the information (Python\'s function and method callings, its module and class names, and argument information) as the JavaScript comment to the exported HTML, like the following:':  # noqa
    '',

    '```js\n...\n  //////////////////////////////////////////////////////////////////////\n  // [__init__ 1] started.\n  // module name: apysc._display.sprite\n  // class: Sprite\n  // arguments and variables:\n  //    variable_name = None\n  //    self = Sprite(\'\')()\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 2] started.\n    // module name: apysc._type.array\n    // class: Array\n    // arguments and variables:\n    //    value = []\n    //    self = []()\n      //////////////////////////////////////////////////////////////////////\n      // [_append_constructor_expression 2] started.\n      // module name: apysc._type.array\n      // class: Array\n      // arguments and variables:\n      //    self = [](arr_2)\n        var arr_2 = [];\n      // [_append_constructor_expression 2] ended.\n      // module name: apysc._type.array\n      // class: Array\n      //////////////////////////////////////////////////////////////////////\n    // [__init__ 2] ended.\n    // module name: apysc._type.array\n    // class: Array\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 1] started.\n    // module name: apysc._display.display_object\n    // class: DisplayObject\n    // arguments and variables:\n    //    variable_name = \'sp_1\'\n    //    self = Sprite(\'\')()\n    // [__init__ 1] ended.\n    // module name: apysc._display.display_object\n    // class: DisplayObject\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [_append_constructor_expression 1] started.\n    // module name: apysc._display.sprite\n    // class: Sprite\n    // arguments and variables:\n    //    self = Sprite(\'sp_1\')(sp_1)\n      var sp_1 = stage.nested();\n    // [_append_constructor_expression 1] ended.\n    // module name: apysc._display.sprite\n    // class: Sprite\n    //////////////////////////////////////////////////////////////////////\n...\n```':  # noqa
    '',

    '':
    '',

    '## See also':
    '',

    '- [Unset debug mode interface](unset_debug_mode.md)':
    '',

    '## set_debug_mode API':
    '',

    '<!-- Docstring: apysc._html.debug_mode.set_debug_mode -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `set_debug_mode() -> None`<hr>\n\n**[Interface summary]** Set the debug mode for the HTML and JavaScript debugging. If calling this function, this interface applies the following setting: <br> ・Disabling HTML minify setting. <br> ・Changing to append per each interface JavaScript divider string.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> ap.set_debug_mode()\n>>> int_val: ap.Int = ap.Int(10)\n```':  # noqa
    '',

}
