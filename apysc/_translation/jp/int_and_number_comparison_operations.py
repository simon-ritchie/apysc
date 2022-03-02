"""This module is for the translation mapping data of the
following document:

Document file: int_and_number_comparison_operations.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Int and Number basic comparison operations':
    '',

    'This page explains basic comparison operations of the `Int` and `Number` classes, like the `>=`\\, `<`\\.':  # noqa
    '',

    '## Common behaviors':
    '',

    'Each comparison operation returns a `Boolean` value, not a Python built-in `bool` value:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == 10\nassert isinstance(result, ap.Boolean)\n```':  # noqa
    '',

    'You can compare the `Int` or `Number` values with the Python built-in values, like the `int` or `float`:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(20)\nresult: ap.Boolean = int_1 == 20\nassert result\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nresult: ap.Boolean = number_1 == 10.5\nassert result\n```':  # noqa
    '',

    'Also, the comparison between the `Int` and `Int`\\, `Number` and `Number`\\, `Int` and `Number` are supported:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == int_2\nassert result\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nnumber_2: ap.Number = ap.Number(10.5)\nresult: ap.Boolean = number_1 == number_2\nassert result\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = ap.Number(10)\nresult: ap.Boolean = int_1 == number_1\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Equal comparison operator':
    '',

    'You can use the `==` operator for the equal comparison:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == 10\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Not equal comparison operator':
    '',

    'You can use the `!=` operator for the not equal comparison:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 != 15\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Less than comparison operator':
    '',

    'You can use the `<` operator for the less than comparison:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 < 11\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Less than or equal comparison operator':
    '',

    'You can use the `<=` operator for the less than or equal comparison:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 <= 10\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Greater than comparison operator':
    '',

    'You can use the `>` operator for the greater than comparison:':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 > 9\nassert result\n```':  # noqa
    '',

    '':
    '',

    '## Greater than or equal comparison operator':
    '',

    'You can use the `>=` operator for the greater than or equal comparison:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 >= 10\nassert result\n```':  # noqa
    '',

}
