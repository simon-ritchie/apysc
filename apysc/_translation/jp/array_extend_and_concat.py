"""This module is for the translation mapping data of the
following document:

Document file: array_extend_and_concat.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array class extend and concat interfaces':
    '',

    'This page explains the `Array` class `extend` and `concat` method interfaces.':  # noqa
    '',

    '## What interfaces are these?':
    '',

    'The `extend` and `concat` method interfaces are the two arrays\' concatenation interfaces.\n\nThe `extend` method updates an original array in place and returns the `None`. The `concat` method returns the concatenated array, and an original one is not updated.':  # noqa
    '',

    '## Basic usage':
    '',

    'The `extend` and `concat` methods require other iterable objects, like the `list`\\, `tuple`\\, or `Array` value at the first argument, as follows:':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2])\narr.extend([3, 4])\nassert arr == [1, 2, 3, 4]\n\nother_arr: ap.Array[int] = arr.concat([5, 6])\nassert other_arr == [1, 2, 3, 4, 5, 6]\nassert arr == [1, 2, 3, 4]\n```':  # noqa
    '',

    '':
    '',

    '## extend API':
    '',

    '<!-- Docstring: apysc._type.array.Array.extend -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `extend(self, other_arr:Union[List[~T], tuple, _ForwardRef(\'Array\')]) -> None`<hr>\n\n**[Interface summary]** Concatenate argument array to this one. This interface positions the argument array\'s values after this array values. This method is similar to the concat method. Still, there is a difference in whether updating the same variable (extend) or returned as a different variable (concat).<hr>\n\n**[Parameters]**\n\n- `other_arr`: Array or list or tuple\n  - Other array-like values to concatenate.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.extend([4, 5, 6])\n>>> arr\nArray([1, 2, 3, 4, 5, 6])\n```':  # noqa
    '',

    '':
    '',

    '## concat API':
    '',

    '<!-- Docstring: apysc._type.array.Array.concat -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `concat(self, other_arr:Union[List[~T], tuple, _ForwardRef(\'Array\')]) -> \'Array\'`<hr>\n\n**[Interface summary]** Concatenate argument array to this one. This interface positions the argument array\'s values after this array values. This method is similar to extend method, but there is a difference in whether updating the same variable (extend) or returned as a different variable (concat).<hr>\n\n**[Parameters]**\n\n- `other_arr`: Array or list or tuple\n  - Other array-like values to concatenate.\n\n<hr>\n\n**[Returns]**\n\n- `concatenated`: Array\n  - Concatenated array value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr = arr.concat([4, 5, 6])\n>>> arr\nArray([1, 2, 3, 4, 5, 6])\n```':  # noqa
    '',

}
