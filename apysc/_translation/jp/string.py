"""This module is for the translation mapping data of the
following document:

Document file: string.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# String':
    '',

    'This page explains the `String` class.\n\nBefore reading on, maybe it is helpful to read the following page:\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the String class?':
    '',

    'The `String` class is the apysc string class. It can accept `str` or `String` values at the constructor, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nassert string_1 == \'Hello\'\n\nstring_2: ap.String = ap.String(string_1)\nassert string_2 == \'Hello\'\n```':  # noqa
    '',

    '':
    '',

    '## String class interfaces':
    '',

    'For more details about the `String` class each interface, please see the following:\n\n- [String class comparison operations](string_comparison_operations.md)\n- [String class addition and multiplication operations](string_addition_and_multiplication.md)':  # noqa
    '',

    '## String class constructor API':
    '',

    '<!-- Docstring: apysc._type.string.String.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, value:Union[str, _ForwardRef(\'String\')]) -> None`<hr>\n\n**[Interface summary]** String class for apysc library.<hr>\n\n**[Parameters]**\n\n- `value`: String or str\n  - Initial string value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> string: ap.String = ap.String(\'Hello\')\n>>> string\nString(\'Hello\')\n\n>>> string += \' World!\'\n>>> string\nString(\'Hello World!\')\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [String class comparison operations document](https://simon-ritchie.github.io/apysc/string_comparison_operations.html)\n- [String class addition and multiplication operations document](https://simon-ritchie.github.io/apysc/string_addition_and_multiplication.html)':  # noqa
    '',

    '## value property API':
    '',

    '<!-- Docstring: apysc._type.string.String.value -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current string value.<hr>\n\n**[Returns]**\n\n- `value`: str\n  - Current string value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> string: ap.String = ap.String(\'Hello\')\n>>> string.value = \'World!\'\n>>> string.value\n\'World!\'\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)':  # noqa
    '',

}
