"""This module is for the translation mapping data of the
following document:

Document file: assert_true_and_false.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# assert_true and assert_false interfaces':
    '',

    'This page explains the `assert_true` and `assert_false` function interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `assert_true` function interface asserts a specified `Boolean` value is true. Conversely, the `assert_false` function interface asserts a specified `Boolean` value is false.':  # noqa
    '',

    '## See also':
    '',

    '- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)':  # noqa
    '',

    '## Basic usage':
    '',

    'The `assert_true` and `assert_false` interfaces requires `value` argument. The `type_strict` and `msg` arguments are optional (default value of the `type_strict` argument is `True`).\n\nIf the `type_strict` argument is `True`, the assertion will use the JavaScript strict comparison operator (`===`). For instance, if the `value` is `Int(1)` and the `type_strict` is `True`, an assertion will fail (because of the comparison between the `Boolean` and `Int`). Conversely, if the `type_strict` is `False`, `Int(1)` will pass the `assert_true` assertion.\n\nThese interfaces display an assertion result on the browser console.\n\nThe following assertion example (`assert_true` and value is the `Boolean(True)`) passes:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nbool_1: ap.Boolean = ap.Boolean(True)\nap.assert_true(bool_1, msg=\'Boolean value is not True!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_true_basic_usage_1/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_true]\nRight-side variable name: b_3\nLeft value: true right value: true\n```':  # noqa
    '',

    '<iframe src="static/assert_true_basic_usage_1/index.html" width="0" height="0"></iframe>\n\nThe following assertion example (`assert_true` and value is the `Boolean(False)`) fails:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nbool_1: ap.Boolean = ap.Boolean(False)\nap.assert_true(bool_1, msg=\'Boolean value is not True!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_true_basic_usage_2/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_true]\nRight-side variable name: b_3\nLeft value: true right value: false\n...\nAssertion failed: Boolean value is not True!\n```':  # noqa
    '',

    '<iframe src="static/assert_true_basic_usage_2/index.html" width="0" height="0"></iframe>\n\nThe following assertion example (`assert_true` and value is the `Int(1)` and `type_strict` is `True`) will fail:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_1: ap.Int = ap.Int(1)\nap.assert_true(int_1, type_strict=True, msg=\'Value is not Boolean(True)!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_true_basic_usage_3/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_true]\nRight-side variable name: i_11\nLeft value: true right value: 1\n...\nAssertion failed: Value is not Boolean(True)!\n```':  # noqa
    '',

    '<iframe src="static/assert_true_basic_usage_3/index.html" width="0" height="0"></iframe>\n\nThe following assertion example (`assert_true` and value is the `Int(1)` and `type_strict` is `False`) will pass:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nint_1: ap.Int = ap.Int(1)\nap.assert_true(int_1, type_strict=False, msg=\'Value is not True!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_true_basic_usage_4/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_true]\nRight-side variable name: i_11\nLeft value: true right value: 1\n```':  # noqa
    '',

    '<iframe src="static/assert_true_basic_usage_4/index.html" width="0" height="0"></iframe>\n\nThe following assertion example (`assert_false` and value is the `Boolean(False)`) passes:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\nbool_1: ap.Boolean = ap.Boolean(False)\nap.assert_false(bool_1, msg=\'Value is not False!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_false_basic_usage_1/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_false]\nRight-side variable name: b_3\nLeft value: false right value: false\n```':  # noqa
    '',

    '<iframe src="static/assert_false_basic_usage_1/index.html" width="0" height="0"></iframe>':  # noqa
    '',

    '## assert_true API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_true -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_true(value:Any, *, type_strict:bool=True, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for true condition.<hr>\n\n**[Parameters]**\n\n- `value`: *\n  - Target value to check.\n- `type_strict`: bool, default True\n  - Whether strictly check actual value or not. For example, if type_strict is True, an integer of 1 fails tests. On the contrary (if type_strict is False), an integer of 1 passes tests.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> boolean: ap.Boolean = int_val == 10\n>>> ap.assert_true(boolean)\n```':  # noqa
    '',

    '':
    '',

    '## assert_false API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_false -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_false(value:Any, *, type_strict:bool=True, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for false condition.<hr>\n\n**[Parameters]**\n\n- `value`: *\n  - Target value to check.\n- `type_strict`: bool, default True\n  - Whether strictly check actual value or not. For example, if type_strict is True, an integer of 0 fails tests. On the contrary (if type_strict is False), an integer of 0 passes tests.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> boolean: ap.Boolean = int_val == 11\n>>> ap.assert_false(boolean)\n```':  # noqa
    '',

}
