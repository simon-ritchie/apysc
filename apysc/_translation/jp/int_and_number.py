"""This module is for the translation mapping data of the
following document:

Document file: int_and_number.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Int and Number':
    '',

    'This page explains the `Int` and `Number` classes.\n\nBefore reading on, maybe it is helpful to read the following page:\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## Int class':
    '',

    'The `Int` class is the apysc integer type. It can accept numeric values at the constructor, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nassert int_1 == 10\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(int_1)\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(int_1)\nint_2 += 15\nassert int_2 == 25\n```':  # noqa
    '',

    'If you specify a float value to the constructor argument, then the `Int` class floor a value:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10.5)\nassert int_1 == 10\n```':  # noqa
    '',

    '':
    '',

    '## Number class':
    '',

    'The ``Number`` class is the apysc float type. It can accept numeric values at the constructor, same as `Int`:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nassert number_1 == 10.5\n\nnumber_2: ap.Number = ap.Number(number_1)\nnumber_2 += 10.5\nassert number_2 == 21\n```':  # noqa
    '',

    '':
    '',

    '## Note for the Float class alias':
    '',

    'The `Float` class is the alias of the `Number` class. It behaves the same as the `Number` class. Maybe a Python developer is familiar with its name rather than the `Number`\\. On the other hand, the `Number` is more common in JavaScript than the `Number`\\.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nassert ap.Number == ap.Float\nassert ap.Number(10.5) == ap.Float(10.5)\n```':  # noqa
    '',

    '':
    '',

    '## Int and Number classes basic interfaces':
    '',

    'The `Int` and `Number` classes have the same interfaces. For more details, please see:\n\n- [Int and Number classes basic arithmetic operations](int_and_number_arithmetic_operations.md)\n- [Int and Number classes basic comparison operations](int_and_number_comparison_operations.md)\n- [Funcdamental data classes common value interface](fundamental_data_classes_value_interface.md)':  # noqa
    '',

    '## Int class constructor API':
    '',

    '<!-- Docstring: apysc._type.int.Int.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, value:Union[int, float, apysc._type.number_value_interface.NumberValueInterface]) -> None`<hr>\n\n**[Interface summary]** Integer class for apysc library.<hr>\n\n**[Parameters]**\n\n- `value`: int or float or Int or Number\n  - Initial integer value. If the `float` or `Number` value is specified, this class casts it to an integer.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> int_val\nInt(10)\n\n>>> int_val == 10\nBoolean(True)\n\n>>> int_val == ap.Int(10)\nBoolean(True)\n\n>>> int_val >= 10\nBoolean(True)\n\n>>> int_val += 10\n>>> int_val\nInt(20)\n\n>>> int_val = ap.Int(10.5)\n>>> int_val\nInt(10)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)\n- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)':  # noqa
    '',

    '## Number class constructor API':
    '',

    '<!-- Docstring: apysc._type.number.Number.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, value:Union[int, float, apysc._type.number_value_interface.NumberValueInterface]) -> None`<hr>\n\n**[Interface summary]** Floating point number class for apysc library.<hr>\n\n**[Parameters]**\n\n- `value`: int or float or Int or Number\n  - Initial floating point number value. This class casts it to float if you specify int or Int value.\n\n<hr>\n\n**[Notes]**\n\nThe `Float` class is the alias of the Number, and it behaves the same as the Number class.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> number: ap.Number = ap.Number(10.5)\n>>> number\nNumber(10.5)\n\n>>> number == 10.5\nBoolean(True)\n\n>>> number == ap.Number(10.5)\nBoolean(True)\n\n>>> number >= 10.5\nBoolean(True)\n\n>>> number += 10.3\n>>> number\nNumber(20.8)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Int and Number common arithmetic operations document](https://simon-ritchie.github.io/apysc/int_and_number_arithmetic_operations.html)\n- [Int and Number common comparison operations document](https://simon-ritchie.github.io/apysc/int_and_number_comparison_operations.html)':  # noqa
    '',

    '## value property API':
    '',

    '<!-- Docstring: apysc._type.number_value_interface.NumberValueInterface.value -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current number value.<hr>\n\n**[Returns]**\n\n- `value`: int or float\n  - Current number value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> int_val.value\n10\n\n>>> int_val.value = 20\n>>> int_val.value\n20\n\n>>> int_val.value = ap.Int(30)\n>>> int_val.value\n30\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)':  # noqa
    '',

}
