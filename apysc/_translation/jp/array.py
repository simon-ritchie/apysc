"""This module is for the translation mapping data of the
following document:

Document file: array.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Array':
    '',

    'This page explains the `Array` class.\n\nBefore reading on, maybe it is helpful to read the following page:\n\n- [Why the apysc library doesn\'t use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '## What is the Array?':
    '',

    'The `Array` class is the apysc array class. It behaves like the Python built-in `list` value.':  # noqa
    '',

    '## Constructor method':
    '',

    'The `Array` class constructor method requires iterable objects, like the `list`\\, `tuple`\\, `range`\\, or `Array` value.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr_from_list: ap.Array = ap.Array([1, 2, 3])\nassert arr_from_list == [1, 2, 3]\n\narr_from_tuple: ap.Array = ap.Array((4, 5, 6))\nassert arr_from_tuple == [4, 5, 6]\n\nother_arr: ap.Array = ap.Array([7, 8, 9])\narr_from_arr: ap.Array = ap.Array(other_arr)\nassert arr_from_arr == [7, 8, 9]\n```':  # noqa
    '',

    '':
    '',

    '## Generic type':
    '',

    'If the `Array` values types are unique, you can set the generic type to an `Array` value. This annotation may be helpful when you use it on the IDE (for type checkers).':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2])\nint_val: int = arr.pop()\nassert isinstance(int_val, int)\n```':  # noqa
    '',

    '':
    '',

    '## See also':
    '',

    '- [Funcdamental data classes common value interface](fundamental_data_classes_value_interface.md)\n- [Array class append and push interfaces](array_append_and_push.md)\n- [Array class extend and concat interfaces](array_extend_and_concat.md)\n- [Array class insert and insert at interfaces](array_insert_and_insert_at.md)\n- [Array class pop interface](array_pop.md)\n- [Array class remove and remove at interfaces](array_remove_and_remove_at.md)\n- [Array class sort interface](array_sort.md)\n- [Array class reverse interface](array_reverse.md)\n- [Array class slice interface](array_slice.md)\n- [Array class length interface](array_length.md)\n- [Array class join interface](array_join.md)\n- [Array class index of interface](array_index_of.md)\n- [Array class comparison interfaces](array_comparison.md)':  # noqa
    '',

    '## Array class constructor API':
    '',

    '<!-- Docstring: apysc._type.array.Array.__init__ -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `__init__(self, value:Union[List[~T], tuple, range, _ForwardRef(\'Array\')]) -> None`<hr>\n\n**[Interface summary]** Array class for the apysc library.<hr>\n\n**[Parameters]**\n\n- `value`: Array or list or tuple or range\n  - Initial array value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr\nArray([1, 2, 3])\n\n>>> arr[0]\n1\n\n>>> arr[1]\n2\n\n>>> arr = ap.Array((4, 5, 6))\n>>> arr\nArray([4, 5, 6])\n\n>>> arr = ap.Array(range(3))\n>>> arr\nArray([0, 1, 2])\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [Array class comparison interfaces document](https://simon-ritchie.github.io/apysc/array_comparison.html)':  # noqa
    '',

    '## value property API':
    '',

    '<!-- Docstring: apysc._type.array.Array.value -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface summary]** Get a current array value.<hr>\n\n**[Returns]**\n\n- `value`: list\n  - Current array value.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.value = [4, 5, 6]\n>>> arr.value\n[4, 5, 6]\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)':  # noqa
    '',

}
