"""This module is for the translation mapping data of the
following document:

Document file: int_and_number_arithmetic_operations.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Int and Number basic arithmetic operations':
    '',

    'This page explains basic arithmetic operations of the `Int` and `Number` classes, like addition, multiplication, or incremental addition.':  # noqa
    '',

    '## Common behaviors':
    '',

    'You can calculate the `Int` and `Number` values with the Python built-in values, such as `int` or `float`\\, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 + 20\nassert int_1 == 30\n```':  # noqa
    '',

    'Also, arithmetic operations with the same types (e.g., `Int` and `Int`) are supported:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 + int_2\nassert int_1 == 30\n```':  # noqa
    '',

    'Arithmetic operations are not supported if the left value is the Python built-in value. For instance, the following code raises an exception:':  # noqa
    '',

    '```py\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\n\n# This will raise the error!\nint_1 = 20 + int_1\n```':  # noqa
    '',

    '':
    '',

    '```\nTypeError: unsupported operand type(s) for +: \'int\' and \'Int\'\n```':  # noqa
    '',

    '':
    '',

    '## Addition':
    '',

    'You can add values with the `+` operator.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 + 20\nassert int_1 == 30\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 + int_2\nassert int_1 == 30\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10) + ap.Int(20)\nassert int_1 == 30\n```':  # noqa
    '',

    'Also, you can use the `+=` operator.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_1 += 20\nassert int_1 == 30\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 += int_2\nassert int_1 == 30\n```':  # noqa
    '',

    '':
    '',

    '## Subtraction':
    '',

    'You can subtract values with the `-` operator.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(30)\nint_1 = int_1 - 10\nassert int_1 == 20\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(30)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 - int_2\nassert int_1 == 10\n```':  # noqa
    '',

    'Also, you can use the `-=` operator.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(50)\nint_1 -= 30\nassert int_1 == 20\n```':  # noqa
    '',

    '':
    '',

    '## Multiplication':
    '',

    'You can multiply values with the `*` operator.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 * 3\nassert int_1 == 30\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(5)\nint_1 = int_1 * int_2\nassert int_1 == 50\n```':  # noqa
    '',

    'Also, you can use the `*=` operator.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_1 *= 3\nassert int_1 == 30\n```':  # noqa
    '',

    '':
    '',

    '## Division':
    '',

    'You can divide values with the `/` operator. A return value becomes a `Number` value, not an `Int`\\.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = int_1 / 4\nassert number_1 == 2.5\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(4)\nnumber_1: ap.Number = int_1 / int_2\nassert number_1 == 2.5\n```':  # noqa
    '',

    'Also, you can use the `/=` operator.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10)\nnumber_1 /= 4\nassert number_1 == 2.5\n```':  # noqa
    '',

    '':
    '',

    '## Floor division':
    '',

    'You can divide and floor values with the `//` operator. A return value becomes an `Int` value, not a `Number`\\.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 // 4\nassert int_1 == 2\n```':  # noqa
    '',

    '':
    '',

    '## Modulo':
    '',

    'You can use the modulo operation with the `%` operator.':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: int = int_1 % 3\nassert int_2 == 1\n```':  # noqa
    '',

    '':
    '',

    '```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nnumber_2: ap.Number = number_1 % 3\nassert number_2 == 1.5\n```':  # noqa
    '',

}
