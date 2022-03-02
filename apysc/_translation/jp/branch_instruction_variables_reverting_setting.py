"""This module is for the translation mapping data of the
following document:

Document file: branch_instruction_variables_reverting_setting.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Each branch instruction class\'s scope variable reverting setting':
    '',

    'This page explains each branch instruction class (like the `If`\\, `Elif`\\, and `Else`) scope variables reverting setting.':  # noqa
    '',

    '## These interfaces execute With statement code':
    '',

    'These interfaces execute the code in each branch instruction regardless of the condition, and variables are updated.\n\nFor example, the following code of the condition is `False`\\, but the value of int is 20 on the Python:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\nassert int_1 == 20\n```':  # noqa
    '',

    'This condition is skipped in JavaScript (converted code) since the condition is not satisfied.':  # noqa
    '',

    '## Scope variables reverting setting':
    '',

    'The `If`, `Elif`, and `Else` classes have the arguments of the `locals_` and `globals_` (basically set the `locals()` and `globals` built-in functions return value). If these arguments are specified, the scope variables are reverted when ended each scope (e.g., `If` scope).\n\nThis interface is occasionally helpful when you don\'t want to update the variables in each branch instruction scope.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition, locals_=locals(), globals_=globals()):\n    int_1 += 10\nassert int_1 == 10\n```':  # noqa
    '',

    '':
    '',

    '## See also':
    '',

    '- [If class](if.md)\n- [Elif class](elif.md)\n- [Else class](else.md)':
    '',

}
