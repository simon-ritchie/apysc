"""This module is for the translation mapping data of the
following document:

Document file: string_addition_and_multiplication.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# String class addition and multiplication operations':
    '',

    'This page explains the `String` class addition and multiplication operations.':  # noqa
    '',

    '## Addition':
    '',

    'The `String` class addition operation (`+`) returns the concatenated `String` value:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nstring_2: ap.String = string_1 + \' World!\'\nassert string_2 == \'Hello World!\'\nassert isinstance(string_2, ap.String)\n```':  # noqa
    '',

    'Also, the `+=` operator is supported:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nstring_1 += \' World!\'\nassert string_1 == \'Hello World!\'\n```':  # noqa
    '',

    'A `String` value + Python built-in `str` operation is supported. Similarly, a `String` value + `String` value operation is also supported:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nstring_2: ap.String = ap.String(\' World!\')\nstring_3: ap.String = string_1 + string_2\nassert string_3 == \'Hello World!\'\n```':  # noqa
    '',

    'But a Python built-in `str` + `String` value is not supported; for instance, the following code raises an error:':  # noqa
    '',

    '```py\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\' World!\')\nstring_2: ap.String = \'Hello\' + string_1\n```':  # noqa
    '',

    '':
    '',

    '```\nTypeError: must be str, not String\n```':
    '',

    '':
    '',

    '## Multiplication':
    '',

    'The `String` class multiplication operation (`*`) returns the repeated `String` value, same behaviors as the Python built-in `str` value:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nstring_2: ap.String = string_1 * 3\nassert string_2 == \'HelloHelloHello\'\n```':  # noqa
    '',

    'The `int` or `Int` values are acceptable at the operation\'s right-side value:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String(\'Hello\')\nint_1: ap.Int = ap.Int(3)\nstring_2: ap.String = string_1 * int_1\nassert string_2 == \'HelloHelloHello\'\n```':  # noqa
    '',

}
