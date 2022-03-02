"""This module is for the translation mapping data of the
following document:

Document file: else.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Else':
    '',

    'This page explains the `Else` class.\n\nBefore reading on, maybe it is helpful to read the following page (the apysc uses the `Else` class for the same reason of each apysc data type):\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the Else class?':
    '',

    'The `Else` class is the apysc branch instruction class. It behaves like the Python built-in `else` keyword.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `Else` requires using the `with` statement. The `Else` class statement is only acceptable to implement right after the `If` or `Elif` classes statement.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\nwith ap.Else():\n    int_1 += 20\n```':  # noqa
    '',

    '':
    '',

    '## Notes':
    '',

    'if you insert the code between the `If` (or `Elif`) and `Else` statements, it raises an exception:':  # noqa
    '',

    '```py\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\n# If there is a code implementation between the `If` and `Else`, then\n# exceptions will be raised.\nint_2: ap.Int = ap.Int(20)\nwith ap.Else():\n    int_1 += 20\n```':  # noqa
    '',

    '':
    '',

    '```\nValueError: Else interface can only use right after If or Elif interfaces.\n```':  # noqa
    '',

    '':
    '',

    '## See also':
    '',

    '- [If class](if.md)\n- [Elif class](elif.md)\n- [Each branch instruction class\'s scope variables reverting setting](branch_instruction_variables_reverting_setting.md)':  # noqa
    '',

    '## Else constructor API':
    '',

    '<!-- Docstring: apysc._branch._else.Else.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, *, locals_:Union[Dict[str, Any], NoneType]=None, globals_:Union[Dict[str, Any], NoneType]=None) -> None`<hr>\n\n**[Interface summary]** A class to append else branch instruction expression.<hr>\n\n**[Parameters]**\n\n- `locals_`: dict or None, default None\n  - Current scope\'s local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of an `Else` scope. This setting is useful when you don\'t want to update each variable by implementing the `Else` scope.\n- `globals_`: dict or None, default None\n  - Current scope\'s global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.\n\n<hr>\n\n**[Notes]**\n\n ・You can only use this class immediately after the `If` or `Elif` statement.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> with ap.If(int_val >= 11):\n...     ap.trace(\'Value is greater than equal 11.\')\n>>> with ap.Else():\n...     ap.trace(\'Value is less than 11.\')\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Each branch instruction class\'s scope variables reverting setting](https://simon-ritchie.github.io/apysc/branch_instruction_variables_reverting_setting.html)':  # noqa
    '',

}
