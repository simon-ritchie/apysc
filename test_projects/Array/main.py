"""Test project for `Array` class.

Command examples:
$ python test_projects/Array/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType
from typing import Any

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


class _Array28Options(TypedDict):
    array_28: ap.Array


def main() -> None:
    """Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(background_color='#333')

    array_1: ap.Array = ap.Array([1, 2, 3])
    ap.assert_arrays_equal(expected=[1, 2, 3], actual=array_1)

    array_1.append(4)
    ap.assert_arrays_equal(expected=[1, 2, 3, 4], actual=array_1)

    array_1.push(5)
    ap.assert_arrays_equal(expected=[1, 2, 3, 4, 5], actual=array_1)

    array_2: ap.Array = ap.Array([1, 2])
    array_2.extend([3, 4])
    ap.assert_arrays_equal(expected=[1, 2, 3, 4], actual=array_2)
    array_3: ap.Array = ap.Array([5, 6])
    array_2.extend(array_3)
    ap.assert_arrays_equal(expected=[1, 2, 3, 4, 5, 6], actual=array_2)

    array_4: ap.Array = ap.Array([1, 2])
    array_5: ap.Array = array_4.concat([3, 4])
    ap.assert_arrays_equal(expected=[1, 2], actual=array_4)
    ap.assert_arrays_equal(expected=[1, 2, 3, 4], actual=array_5)
    array_6: ap.Array = ap.Array([5, 6])
    array_7: ap.Array = array_4.concat(array_6)
    ap.assert_arrays_equal(expected=[1, 2, 5, 6], actual=array_7)

    array_8: ap.Array[Any] = ap.Array([1, 5])
    array_8.insert(index=1, value=2)
    ap.assert_arrays_equal(expected=[1, 2, 5], actual=array_8)
    array_8.insert(index=2, value=ap.Int(3))
    ap.assert_arrays_equal(expected=[1, 2, 3, 5], actual=array_8)
    array_8.insert_at(index=3, value=4)
    ap.assert_arrays_equal(expected=[1, 2, 3, 4, 5], actual=array_8)

    int_1: ap.Int = ap.Int(2)
    array_9: ap.Array[Any] = ap.Array([1, int_1, 3])
    array_9.pop()
    ap.assert_arrays_equal(expected=[1, 2], actual=array_9)
    int_2: ap.Int = array_9.pop()
    ap.assert_arrays_equal(expected=[1], actual=array_9)
    ap.assert_equal(expected=2, actual=int_2)

    array_10: ap.Array[Any] = ap.Array([1, 2, 3, 4])
    array_10.remove(3)
    ap.assert_arrays_equal(expected=[1, 2, 4], actual=array_10)
    array_10.remove(ap.Int(2))
    ap.assert_arrays_equal(expected=[1, 4], actual=array_10)

    array_11: ap.Array = ap.Array([1, 2, 3, 4])
    array_11.remove_at(1)
    ap.assert_arrays_equal(expected=[1, 3, 4], actual=array_11)
    array_11.remove_at(ap.Int(1))
    ap.assert_arrays_equal(expected=[1, 4], actual=array_11)

    array_12: ap.Array = ap.Array([1, 2, 3])
    array_12.reverse()
    ap.assert_arrays_equal(expected=[3, 2, 1], actual=array_12)

    array_13: ap.Array = ap.Array([1, 4, 2, 3])
    array_13.sort()
    ap.assert_arrays_equal(expected=[1, 2, 3, 4], actual=array_13)

    array_14: ap.Array = ap.Array([1, 4, 2, 3])
    array_14.sort(ascending=False)
    ap.assert_arrays_equal(expected=[4, 3, 2, 1], actual=array_14)

    array_15: ap.Array = ap.Array([1, 2, 3, 4])
    array_16: ap.Array = array_15.slice(start=1, end=3)
    ap.assert_arrays_equal(expected=[2, 3], actual=array_16)
    array_17: ap.Array = array_15.slice(start=1)
    ap.assert_arrays_equal(expected=[2, 3, 4], actual=array_17)
    array_18: ap.Array = array_15.slice(end=2)
    ap.assert_arrays_equal(expected=[1, 2], actual=array_18)

    array_19: ap.Array = ap.Array([ap.Int(1), ap.Int(2), ap.Int(3)])
    ap.assert_equal(expected=2, actual=array_19[1])

    array_19[ap.Int(1)] = ap.Int(4)
    ap.assert_arrays_equal(expected=[1, 4, 3], actual=array_19)

    array_20: ap.Array = ap.Array([1, 2, 3])
    array_20[1] = 4
    ap.assert_arrays_equal(expected=[1, 4, 3], actual=array_20)

    array_21: ap.Array = ap.Array([1, 2, 3])
    del array_21[1]
    ap.assert_arrays_equal(expected=[1, 3], actual=array_21)

    array_22: ap.Array = ap.Array([1, 2, 3])
    length_1: ap.Int = array_22.length
    ap.assert_equal(expected=3, actual=length_1)

    array_23: ap.Array = ap.Array([1, ap.Int(2), '3', ap.String('4')])
    joined_1: ap.String = array_23.join(', ')
    ap.assert_equal(expected='1, 2, 3, 4', actual=joined_1)

    int_3: ap.Int = ap.Int(2)
    array_24: ap.Array = ap.Array([1, int_3, 3])
    ap.assert_equal(expected=1, actual=array_24.index_of(int_3))
    ap.assert_equal(expected=2, actual=array_24.index_of(3))

    int_4: ap.Int = ap.Int(10)
    array_25: ap.Array = ap.Array([1, 2])
    array_26: ap.Array = ap.Array([1, 2])
    with ap.If(array_25 == array_26, locals(), globals()):
        int_4.value = 20
    ap.assert_equal(expected=20, actual=int_4)

    array_27: ap.Array = ap.Array([3, 4])
    with ap.If(array_26 != array_27, locals(), globals()):
        int_4.value = 30
    ap.assert_equal(expected=30, actual=int_4)

    array_28: ap.Array = ap.Array([1, 2])
    options: _Array28Options = {'array_28': array_28}
    stage.click(on_stage_clicked, options=options)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_stage_clicked(e: ap.MouseEvent, options: _Array28Options) -> None:
    """
    Test handler that called when stage is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('stage clicked!')
    array_28: ap.Array = options['array_28']
    array_28.value = [3, 4]
    ap.assert_true(array_28 == [3, 4])
    ap.assert_true(array_28 != [1, 2])


if __name__ == '__main__':
    main()
