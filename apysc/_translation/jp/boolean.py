"""This module is for the translation mapping data of the
following document:

Document file: boolean.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Boolean':
    '',

    'This page explains the `Boolean` class.\n\nBefore reading on, maybe it is helpful to read the following page:\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the Boolean class?':
    '',

    'The `Boolean` class is the apysc boolean class. It can accept `bool` or `Boolean` values at the constructor, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n\nbool_3: ap.Boolean = ap.Boolean(bool_1)\nassert bool_3\n```':  # noqa
    '',

    '':
    '',

    '## Note for the Bool class alias':
    '',

    'The `Bool` class is the alias of the `Boolean` class. And it behaves the same as the `Boolean` class.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nassert ap.Boolean == ap.Bool\nassert ap.Boolean(True) == ap.Bool(True)\n```':  # noqa
    '',

    '':
    '',

    '## Boolean comparison':
    '',

    'The `Boolean` comparison interface behaves like the Python built-in `bool` value.\n\nYou can compare it with the equal comparison operator (`=`), and the `Boolean`\\, `bool`\\, `int`\\, `Int` types are acceptable, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 == True  # noqa\nassert bool_1 == ap.Boolean(True)\nassert bool_1 == 1\nassert bool_1 == ap.Int(1)\n```':  # noqa
    '',

    'Also, the not equal comparison operator (`!=`) is supported, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 != False  # noqa\nassert bool_1 != ap.Boolean(False)\nassert bool_1 != 0\nassert bool_1 != ap.Int(0)\n```':  # noqa
    '',

    'You can skip the comparison operator, as follows:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n```':  # noqa
    '',

    '':
    '',

    '## Reverse a Boolean value':
    '',

    'The `not_` property returns the reversed `Boolean` value:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nbool_2: ap.Boolean = bool_1.not_\nassert not bool_2\n\nbool_3: ap.Boolean = bool_2.not_\nassert bool_3\n```':  # noqa
    '',

    '':
    '',

    '## Boolean class constructor API':
    '',

    '<!-- Docstring: apysc._type.boolean.Boolean.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, value:Union[int, apysc._type.int.Int, _ForwardRef(\'Boolean\')]) -> None`<hr>\n\n**[Interface summary]** Boolean class for apysc library.<hr>\n\n**[Parameters]**\n\n- `value`: Boolean or Int or bool or int\n  - Initial boolean value. 0 or 1 are acceptable for an integer value.\n\n<hr>\n\n**[Notes]**\n\nThe Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> bool_val_1: ap.Boolean = ap.Boolean(True)\n>>> bool_val_1\nBoolean(True)\n\n>>> bool_val_2: ap.Bool = ap.Bool(True)\n>>> bool_val_2\nBoolean(True)\n```':  # noqa
    '',

    '':
    '',

    '## value property API':
    '',

    '<!-- Docstring: apysc._type.boolean.Boolean.value -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current boolean value.<hr>\n\n**[Returns]**\n\n- `value`: bool\n  - Current boolean value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.value = False\n>>> bool_val.value\nFalse\n\n>>> bool_val.value = ap.Boolean(True)\n>>> bool_val.value\nTrue\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)':  # noqa
    '',

    '## not_ property API':
    '',

    '<!-- Docstring: apysc._type.boolean.Boolean.not_ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a not condition Boolean value.<hr>\n\n**[Returns]**\n\n- `result`: Boolean\n  - Not condition Boolean value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.not_\nBoolean(False)\n\n>>> bool_val.value = False\n>>> bool_val.not_\nBoolean(True)\n```':  # noqa
    '',

}
