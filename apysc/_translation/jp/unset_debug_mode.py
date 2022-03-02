"""This module is for the translation mapping data of the
following document:

Document file: unset_debug_mode.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# unset_debug_mode interface':
    '',

    'This page explains the `unset_debug_mode` function interface.':
    '',

    '## What interface is this?':
    '',

    'The `unset_debug_mode` function interface unsets the debug mode setting. It stops the debug information appending.\n\nThe debug mode exports lots of information. Sometimes it becomes cumbersome. In that case, stopping the debug mode is helpful when it is no longer needed.':  # noqa
    '',

    '## Notes':
    '',

    'If the exporting interface (e.g., `ap.save_overall_html`) `minify` option is enabled, it removes debug mode information. So it is required to set the `minify=False` when you use the `unset_debug_mode` interface.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `unset_debug_mode` interface requires no arguments.\n\nThe following example appends the debug information only at the `int_1` instantiation and incremental addition of 10.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\'#333\',\n    stage_elem_id=\'stage\')\nsprite: ap.Sprite = ap.Sprite()\nap.set_debug_mode()\nint_1: ap.Int = ap.Int(10)\nint_1 += 10\nap.unset_debug_mode()\nint_2: ap.Int = ap.Int(20)\nint_2 += 20\n\nap.save_overall_html(\n    minify=False, dest_dir_path=\'unset_debug_mode_basic_usage/\')\n```':  # noqa
    '',

    'The exported HTML includes the debug information at the first integer position. It doesn\'t include the sprite and second integer positions, as follows:':  # noqa
    '',

    '```js\n...\n  var sp_1 = stage.nested();\n  var g_1 = stage.nested();\n  arr_2.push(g_1);\n  var i_12 = -1;\n  i_12 = arr_2.indexOf(g_1);\n  var b_3 = false;\n  var i_13 = -1;\n...\n  //////////////////////////////////////////////////////////////////////\n  // [__init__ 12] started.\n  // module name: apysc._type.int\n  // class: Int\n  // arguments and variables:\n  //    value = 10\n  //    self = 0()\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 14] started.\n    // module name: apysc._type.number_value_interface\n    // class: NumberValueInterface\n    // arguments and variables:\n    //    type_name = \'i\'\n    //    value = 10\n    //    self = 0(i_16)\n    // [__init__ 14] ended.\n    // module name: apysc._type.number_value_interface\n    // class: NumberValueInterface\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [to_int_from_float 14] started.\n    // module name: apysc._converter.cast\n    // arguments and variables:\n    //    int_or_float = 10\n    // [to_int_from_float 14] ended.\n    // module name: apysc._converter.cast\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [append_constructor_expression 14] started.\n    // module name: apysc._type.number_value_interface\n    // class: NumberValueInterface\n    // arguments and variables:\n    //    self = 10(i_16)\n      var i_16 = 10;\n    // [append_constructor_expression 14] ended.\n    // module name: apysc._type.number_value_interface\n    // class: NumberValueInterface\n    //////////////////////////////////////////////////////////////////////\n...\n  var i_18 = 20;\n  var i_19 = cpy(i_18);\n  var i_19 = i_18 + 20;\n  i_18 = i_19;\n...\n```':  # noqa
    '',

    '':
    '',

    '## See also':
    '',

    '- [Set debug mode interface](set_debug_mode.md)':
    '',

    '## unset_debug_mode API':
    '',

    '<!-- Docstring: apysc._html.debug_mode.unset_debug_mode -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unset_debug_mode() -> None`<hr>\n\n**[Interface summary]** Unset the debug mode for the HTML and JavaScript debugging.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> ap.set_debug_mode()\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.unset_debug_mode()\n```':  # noqa
    '',

}
