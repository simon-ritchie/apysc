"""Test project for `Dictionary` class.

Command examples:
$ python test_projects/Dictionary/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


class _Dict1Options(TypedDict):
    dict_1: ap.Dictionary


def main() -> None:
    """Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(background_color='#333')

    dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
    ap.assert_dicts_equal(expected={'a': 10}, actual=dict_1)

    dict_1.value = {'b': 20}
    ap.assert_dicts_equal(expected={'b': 20}, actual=dict_1)

    options: _Dict1Options = {'dict_1': dict_1}
    stage.click(on_stage_click, options=options)
    ap.assert_dicts_equal(expected={'b': 20}, actual=dict_1)

    dict_2: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
    length: ap.Int = dict_2.length
    ap.assert_equal(expected=2, actual=length)

    int_1: ap.Int = ap.Int(30)
    string_1: ap.String = ap.String('a')
    number_1: ap.Number = ap.Number(3.5)
    dict_3: ap.Dictionary = ap.Dictionary({'a': 10, 2: 20, 3.5: int_1})
    ap.assert_equal(expected=10, actual=dict_3['a'])
    ap.assert_equal(expected=10, actual=dict_3[string_1])
    ap.assert_equal(expected=20, actual=dict_3[2])
    ap.assert_equal(expected=int_1, actual=dict_3[number_1])

    dict_3[string_1] = 40
    ap.assert_equal(expected=40, actual=dict_3[string_1])
    dict_3['a'] = int_1
    ap.assert_equal(expected=int_1, actual=dict_3['a'])

    dict_4: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
    string_2: ap.String = ap.String('a')
    del dict_4[string_2]  # type: ignore
    ap.assert_dicts_equal(expected={'b': 20}, actual=dict_4)

    dict_5: ap.Dictionary = ap.Dictionary({'a': 10})
    dict_6: ap.Dictionary = ap.Dictionary({'a': 10})
    result: ap.Boolean = dict_5 == dict_6
    ap.assert_true(result)

    result = dict_5 == {'a': 10}
    ap.assert_true(result)

    dict_7: ap.Dictionary = ap.Dictionary({'a': 20})
    result = dict_5 != dict_7
    ap.assert_true(result)

    result = dict_5 != {'a': 20}
    ap.assert_true(result)

    int_2: ap.Int = ap.Int(20)
    int_3: ap.Int = ap.Int(30)
    dict_8: ap.Dictionary = ap.Dictionary({'a': int_2})
    got_val_1: ap.Int = dict_8.get('a', default=int_3)
    ap.assert_equal(expected=20, actual=got_val_1)
    got_val_1 = dict_8.get('b', default=int_3)
    ap.assert_equal(expected=30, actual=got_val_1)
    got_val_2: None = dict_8.get('c', default=None)
    ap.assert_equal(expected=None, actual=got_val_2)
    got_val_3: int = dict_8.get('d', default=40)
    ap.assert_equal(expected=40, actual=got_val_3)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_stage_click(e: ap.MouseEvent, options: _Dict1Options) -> None:
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
    dict_1: ap.Dictionary = options['dict_1']
    dict_1.value = {'c': 30}
    ap.assert_dicts_equal(expected={'c': 30}, actual=dict_1)


if __name__ == '__main__':
    main()
