"""Test project for `Array` class.

Command examples:
$ python test_projects/Array/main.py
$ python Array/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.console.assertion import assert_arrays_equal
from apyscript.console.assertion import assert_equal
from apyscript.display import Stage
from apyscript.file import file_util
from apyscript.html import exporter
from apyscript.type import Array
from apyscript.type import Int
from apyscript.type import String

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    _: Stage = Stage(background_color='#333')

    array_1: Array = Array([1, 2, 3])
    assert_arrays_equal(expected=[1, 2, 3], actual=array_1)

    array_1.append(4)
    assert_arrays_equal(expected=[1, 2, 3, 4], actual=array_1)

    array_1.push(5)
    assert_arrays_equal(expected=[1, 2, 3, 4, 5], actual=array_1)

    array_2: Array = Array([1, 2])
    array_2.extend([3, 4])
    assert_arrays_equal(expected=[1, 2, 3, 4], actual=array_2)
    array_3: Array = Array([5, 6])
    array_2.extend(array_3)
    assert_arrays_equal(expected=[1, 2, 3, 4, 5, 6], actual=array_2)

    array_4: Array = Array([1, 2])
    array_5: Array = array_4.concat([3, 4])
    assert_arrays_equal(expected=[1, 2], actual=array_4)
    assert_arrays_equal(expected=[1, 2, 3, 4], actual=array_5)
    array_6: Array = Array([5, 6])
    array_7: Array = array_4.concat(array_6)
    assert_arrays_equal(expected=[1, 2, 5, 6], actual=array_7)

    array_8: Array = Array([1, 5])
    array_8.insert(index=1, value=2)
    assert_arrays_equal(expected=[1, 2, 5], actual=array_8)
    array_8.insert(index=2, value=Int(3))
    assert_arrays_equal(expected=[1, 2, 3, 5], actual=array_8)
    array_8.insert_at(index=3, value=4)
    assert_arrays_equal(expected=[1, 2, 3, 4, 5], actual=array_8)

    int_1: Int = Int(2)
    array_9: Array = Array([1, int_1, 3])
    array_9.pop()
    assert_arrays_equal(expected=[1, 2], actual=array_9)
    int_2: Int = array_9.pop()
    assert_arrays_equal(expected=[1], actual=array_9)
    assert_equal(expected=2, actual=int_2)

    array_10: Array = Array([1, 2, 3, 4])
    array_10.remove(3)
    assert_arrays_equal(expected=[1, 2, 4], actual=array_10)
    array_10.remove(Int(2))
    assert_arrays_equal(expected=[1, 4], actual=array_10)

    array_11: Array = Array([1, 2, 3, 4])
    array_11.remove_at(1)
    assert_arrays_equal(expected=[1, 3, 4], actual=array_11)
    array_11.remove_at(Int(1))
    assert_arrays_equal(expected=[1, 4], actual=array_11)

    array_12: Array = Array([1, 2, 3])
    array_12.reverse()
    assert_arrays_equal(expected=[3, 2, 1], actual=array_12)

    array_13: Array = Array([1, 4, 2, 3])
    array_13.sort()
    assert_arrays_equal(expected=[1, 2, 3, 4], actual=array_13)

    array_14: Array = Array([1, 4, 2, 3])
    array_14.sort(ascending=False)
    assert_arrays_equal(expected=[4, 3, 2, 1], actual=array_14)

    array_15: Array = Array([1, 2, 3, 4])
    array_16: Array = array_15.slice(start=1, end=3)
    assert_arrays_equal(expected=[2, 3], actual=array_16)
    array_17: Array = array_15.slice(start=1)
    assert_arrays_equal(expected=[2, 3, 4], actual=array_17)
    array_18: Array = array_15.slice(end=2)
    assert_arrays_equal(expected=[1, 2], actual=array_18)

    array_19: Array = Array([Int(1), Int(2), Int(3)])
    assert_equal(expected=2, actual=array_19[1])

    array_19[Int(1)] = Int(4)
    assert_arrays_equal(expected=[1, 4, 3], actual=array_19)

    array_20: Array = Array([1, 2, 3])
    array_20[1] = 4
    assert_arrays_equal(expected=[1, 4, 3], actual=array_20)

    array_21: Array = Array([1, 2, 3])
    del array_21[1]
    assert_arrays_equal(expected=[1, 3], actual=array_21)

    array_22: Array = Array([1, 2, 3])
    length_1: Int = array_22.length
    assert_equal(expected=3, actual=length_1)

    array_23: Array = Array([1, Int(2), '3', String('4')])
    joined_1: String = array_23.join(', ')
    assert_equal(expected='1, 2, 3, 4', actual=joined_1)

    int_3: Int = Int(2)
    array_24: Array = Array([1, int_3, 3])
    assert_equal(expected=1, actual=array_24.index_of(int_3))
    assert_equal(expected=2, actual=array_24.index_of(3))

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
