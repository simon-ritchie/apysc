"""This module is for the translation mapping data of the
following document:

Document file: assert_arrays_equal_and_arrays_not_equal.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# assert_arrays_equal and assert_arrays_not_equal interfaces':
    '',

    'This page explains the `assert_arrays_equal` and `assert_arrays_not_equal` function interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `assert_arrays_equal` function interface asserts that the two arrays are equal. Conversely, the `assert_arrays_not_equal` function interface asserts that the two arrays are not equal.':  # noqa
    '',

    '## See also':
    '',

    '- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)':  # noqa
    '',

    '## Basic usage':
    '',

    'Both of the `assert_arrays_equal` and `assert_arrays_not_equal` interfaces require the `left` and `right` arguments. The `msg` argument is optional.\n\nThe arguments accept a Python built-in `list` value and `Array` value.\n\nThe following example (`assert_arrays_equal` and values are equal) passes:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_equal(\n    left=[1, 2, 3], right=arr_1, msg=\'Values are not equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_arrays_equal_basic_usage_1/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_arrays_equal]\nLeft value: [1, 2, 3] right value: arr_2\n```':  # noqa
    '',

    '<iframe src="static/assert_arrays_equal_basic_usage_1/index.html" width="0" height="0"></iframe>\n\nThe following example (`assert_arrays_equal` and values are not equal) fails:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_equal(\n    left=[1, 2], right=arr_1, msg=\'Values are not equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_arrays_equal_basic_usage_2/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_arrays_equal]\nLeft value: [1, 2] right value: arr_2\n...\nAssertion failed: Values are not equal!\n```':  # noqa
    '',

    '<iframe src="static/assert_arrays_equal_basic_usage_2/index.html" width="0" height="0"></iframe>\n\nThe following example (`assert_arrays_not_equal` and values are not equal) passes:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\narr_1: ap.Array = ap.Array([1, 2, 3])\nap.assert_arrays_not_equal(\n    left=[1, 2], right=arr_1, msg=\'Values are equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_arrays_not_equal_basic_usage_1/\')\n```':  # noqa
    '',

    '<iframe src="static/assert_arrays_not_equal_basic_usage_1/index.html" width="0" height="0"></iframe>':  # noqa
    '',

    '## Notes for the assert_equal and assert_not_equal interfaces':
    '',

    'If an `Array` value is specified to the `assert_equal` or `assert_not_equal` interface\'s values, then the `assert_arrays_equal` or `assert_arrays_not_equal` interfaces will be called instead of the `assert_equal` or `assert_not_equal` interfaces automatically.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\nstage: ap.Stage = ap.Stage(\n    stage_width=0, stage_height=0, background_color=\'#333\',\n    stage_elem_id=\'stage\')\n\narr_1: ap.Array = ap.Array([1, 2, 3, 4, 5])\nap.assert_equal(\n    left=[1, 2, 3, 4, 5], right=arr_1, msg=\'Values are equal!\')\n\nap.save_overall_html(\n    dest_dir_path=\'assert_arrays_equal_notes_for_the_assert_equal/\')\n```':  # noqa
    '',

    '':
    '',

    '```\n[assert_arrays_equal]\nLeft value: [1, 2, 3, 4, 5] right value: arr_2\n```':  # noqa
    '',

    '<iframe src="static/assert_arrays_equal_notes_for_the_assert_equal/index.html" width="0" height="0"></iframe>':  # noqa
    '',

    '## assert_arrays_equal API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_arrays_equal -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_arrays_equal(left:Any, right:Any, *, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for Array values equal condition.<hr>\n\n**[Parameters]**\n\n- `left`: *\n  - Left-side value to compare.\n- `right`: *\n  - Right-side value to compare.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Notes]**\n\nThis interface is used instead of assert_equal for Array class comparison (JavaScript can not compare arrays directly, like a Python, for example, `[1, 2] === [1, 2]` becomes false).<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr_1: ap.Array = ap.Array([1, 2, 3])\n>>> arr_2: ap.Array = ap.Array([1, 2, 3])\n>>> ap.assert_arrays_equal(arr_1, arr_2)\n```':  # noqa
    '',

    '':
    '',

    '## assert_arrays_not_equal API':
    '',

    '<!-- Docstring: apysc._console.assertion.assert_arrays_not_equal -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `assert_arrays_not_equal(left:Any, right:Any, *, msg:str=\'\') -> None`<hr>\n\n**[Interface summary]** JavaScript assertion interface for Array values not equal condition.<hr>\n\n**[Parameters]**\n\n- `left`: *\n  - Left-side value to compare.\n- `right`: *\n  - Right-side value to compare.\n- `msg`: str, optional\n  - Message to display when assertion failed.\n\n<hr>\n\n**[Notes]**\n\nThis interface is used instead of assert_not_equal for Array class comparison (JavaScript can not compare arrays directly, like a Python, for example, `[1, 2] === [1, 2]` becomes false).<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr_1: ap.Array = ap.Array([1, 2, 3])\n>>> arr_2: ap.Array = ap.Array([4, 5, 6])\n>>> ap.assert_arrays_not_equal(arr_1, arr_2)\n```':  # noqa
    '',

}
