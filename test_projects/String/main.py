"""Test project for `String` class.

Command examples:
$ python test_projects/String/main.py
$ python String/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Boolean
from apysc import If
from apysc import MouseEvent
from apysc import Stage
from apysc import String
from apysc import assert_equal
from apysc import assert_true
from apysc import save_overall_html
from apysc import trace
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    stage: Stage = Stage(background_color='#333')

    string_1: String = String(value='Hello')
    assert_equal(expected='Hello', actual=string_1)

    string_2: String = string_1 + ' World!'
    assert_equal(expected='Hello World!', actual=string_2)

    string_3: String = string_1 * 2
    assert_equal(expected='HelloHello', actual=string_3)

    string_1 += ' World!'
    assert_equal(expected='Hello World!', actual=string_1)

    string_1 *= 2
    assert_equal(expected='Hello World!Hello World!', actual=string_1)

    string_4: String = String('Hello!')
    boolean_1: Boolean = Boolean(False)
    with If(boolean_1, locals(), globals()):
        string_4 += ' World!'
    assert_equal(expected='Hello!', actual=string_4)

    with If(boolean_1, locals(), globals()):
        string_4 *= 3
    assert_equal(expected='Hello!', actual=string_4)

    string_5: String = String('Hello!')
    stage.click(on_stage_clicked, options={'string_5': string_5})

    save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_stage_clicked(e: MouseEvent, options: Dict[str, Any]) -> None:
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
    string_5: String = options['string_5']
    string_5.value = 'World!'
    assert_true(string_5 == 'World!')
    assert_true(string_5 != 'Hello!')
    string_5.value = '1970-01-05'
    assert_true(string_5 < '1970-01-06')
    assert_true(string_5 <= '1970-01-05')
    assert_true(string_5 > '1970-01-04')
    assert_true(string_5 >= '1970-01-05')


if __name__ == '__main__':
    main()
