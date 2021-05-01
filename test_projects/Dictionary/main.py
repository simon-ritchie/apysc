"""Test project for `Dictionary` class.

Command examples:
$ python test_projects/Dictionary/main.py
$ python Dictionary/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Dictionary
from apysc import Int
from apysc import MouseEvent
from apysc import Number
from apysc import Stage
from apysc import String
from apysc import assert_dicts_equal
from apysc import assert_equal
from apysc import trace
from apysc.file import file_util
from apysc.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    stage: Stage = Stage(background_color='#333')

    dict_1: Dictionary = Dictionary({'a': 10})
    assert_dicts_equal(expected={'a': 10}, actual=dict_1)

    dict_1.value = {'b': 20}
    assert_dicts_equal(expected={'b': 20}, actual=dict_1)

    stage.click(on_stage_click, options={'dict_1': dict_1})
    assert_dicts_equal(expected={'b': 20}, actual=dict_1)

    dict_2: Dictionary = Dictionary({'a': 10, 'b': 20})
    length: Int = dict_2.length
    assert_equal(expected=2, actual=length)

    int_1: Int = Int(30)
    string_1: String = String('a')
    number_1: Number = Number(3.5)
    dict_3: Dictionary = Dictionary({'a': 10, 2: 20, 3.5: int_1})
    assert_equal(expected=10, actual=dict_3['a'])
    assert_equal(expected=10, actual=dict_3[string_1])
    assert_equal(expected=20, actual=dict_3[2])
    assert_equal(expected=int_1, actual=dict_3[number_1])

    dict_3[string_1] = 40
    assert_equal(expected=40, actual=dict_3[string_1])
    dict_3['a'] = int_1
    assert_equal(expected=int_1, actual=dict_3['a'])

    dict_4: Dictionary = Dictionary({'a': 10, 'b': 20})
    string_2: String = String('a')
    del dict_4[string_2]
    assert_dicts_equal(expected={'b': 20}, actual=dict_4)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_stage_click(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when stage is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created event instance.
    options : dict
        Optional arguments dictionary.
    """
    trace('stage clicked!')
    dict_1: Dictionary = options['dict_1']
    dict_1.value = {'c': 30}
    assert_dicts_equal(expected={'c': 30}, actual=dict_1)


if __name__ == '__main__':
    main()
