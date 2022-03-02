"""This module is for the translation mapping data of the
following document:

Document file: assert_dicts_equal_and_dicts_not_equal.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# assert_dicts_equal and assert_dicts_not_equal interfaces':
    '',

    'This page explains the `assert_dicts_equal` and `assert_dicts_not_equal` function interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `assert_dicts_equal` function interface asserts specified two dictionaries (`Dictionary` type value) are equal. Conversely, the `assert_dicts_not_equal` function interface asserts specified two dictionaries are not equal.':  # noqa
    '',

    '## See also':
    '',

    '- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)':  # noqa
    '',

    '## Basic usage':
    '',

    'Both of the `assert_dicts_equal` and `assert_dicts_not_equal` interfaces require the `left` and `right` arguments. The `msg` argument is optional.\n\nYou can specify a Python built-in `dict` and `Dictionary` values to these arguments.\n\nThe following example (`assert_dicts_equal` and values are equal) passes:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\ndict_val: ap.Dictionary = ap.Dictionary({\'a\': 10, \'b\': 20})\nap.assert_dicts_equal(\n    left={\'a\': 10, \'b\': 20}, right=dict_val,\n    msg=\'Values are not equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_dicts_equal_basic_usage_1/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_dicts_equal]\nLeft value: {a: 10, b: 20} right value: dct_1\n```':  # noqa
    '',

    '<iframe src="static/assert_dicts_equal_basic_usage_1/index.html" width="0" height="0"></iframe>\n\nThe following example (`assert_dicts_equal` and values are not equal)  fails:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\ndict_val: ap.Dictionary = ap.Dictionary({\'a\': 10, \'b\': 20})\nap.assert_dicts_equal(\n    left={\'a\': 30}, right=dict_val, msg=\'Values are not equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_dicts_equal_basic_usage_2/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_dicts_equal]\nLeft value: {a: 30} right value: dct_1\n...\nAssertion failed: Values are not equal!\n```':  # noqa
    '',

    '<iframe src="static/assert_dicts_equal_basic_usage_2/index.html" width="0" height="0"></iframe>\n\nThe following example (`assert_dicts_not_equal` and values are not equal) passes:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\ndict_val: ap.Dictionary = ap.Dictionary({\'a\': 10, \'b\': 20})\nap.assert_dicts_not_equal(\n    left={\'a\': 30}, right=dict_val, msg=\'Values are equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_dicts_not_equal_basic_usage_1/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_dicts_not_equal]\nLeft value: {a: 30} right value: dct_1\n```':  # noqa
    '',

    '<iframe src="static/assert_dicts_not_equal_basic_usage_1/index.html" width="0" height="0"></iframe>':  # noqa
    '',

    '## Notes for the assert_equal and assert_not_equal interfaces':
    '',

    'If a `Dictionary` value is specified to the `assert_equal` or `assert_not_equal` interface\'s argument value, then the `assert_dicts_equal` or `assert_dicts_not_equal` interfaces will be called instead of the `assert_equal` or `assert_not_equal` interfaces automatically.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\ndict_val: ap.Dictionary = ap.Dictionary({\'a\': 30})\nap.assert_equal(\n    left={\'a\': 30}, right=dict_val,\n    msg=\'Values are not equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_dicts_equal_notes_for_assert_equal/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_dicts_equal]\nLeft value: {a: 30} right value: dct_1\n```':  # noqa
    '',

    '<iframe src="static/assert_dicts_equal_notes_for_assert_equal/index.html" width="0" height="0"></iframe>':  # noqa
    '',

    '## assert_dicts_equal API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_dicts_equal -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_dicts_equal(left:Any, right:Any, *, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for Dictionary values equal condition.<hr>\n\n**[Parameters]**\n\n- `left`: *\n  - Left-side value to compare.\n- `right`: *\n  - Right-side value to compare.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Notes]**\n\nThis interface is used instead of assert_equal for Dictionary class comparison (JavaScript can not compare dictionary (Object) directly, like a Python, for example, `{"a": 10} === {"a": 10}` becomes false).<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> dict_1: ap.Dictionary = ap.Dictionary({\'a\': 10})\n>>> dict_2: ap.Dictionary = ap.Dictionary({\'a\': 10})\n>>> ap.assert_dicts_equal(dict_1, dict_2)\n```':  # noqa
    '',

    '':
    '',

    '## assert_dicts_not_equal API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_dicts_not_equal -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_dicts_not_equal(left:Any, right:Any, *, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for Dictionary values not equal condition.<hr>\n\n**[Parameters]**\n\n- `left`: *\n  - Left-side value to compare.\n- `right`: *\n  - Right-side value to compare.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Notes]**\n\nThis interface is used instead of assert_not_equal for Dictionary class comparison (JavaScript can not compare dictionary (Object) directly, like a Python, for example, `{"a": 10} !== {"a": 10}` becomes true).<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> dict_1: ap.Dictionary = ap.Dictionary({\'a\': 10})\n>>> dict_2: ap.Dictionary = ap.Dictionary({\'a\': 20})\n>>> ap.assert_dicts_not_equal(dict_1, dict_2)\n```':  # noqa
    '',

}
