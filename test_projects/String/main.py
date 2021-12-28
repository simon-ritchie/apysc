"""Test project for `String` class.

Command examples:
$ python test_projects/String/main.py
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


class _Str5Options(TypedDict):
    string_5: ap.String


def main() -> None:
    """Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(background_color='#333')

    string_1: ap.String = ap.String(value='Hello')
    ap.assert_equal(left='Hello', right=string_1)

    string_2: ap.String = string_1 + ' World!'
    ap.assert_equal(left='Hello World!', right=string_2)

    string_3: ap.String = string_1 * 2
    ap.assert_equal(left='HelloHello', right=string_3)

    string_1 += ' World!'
    ap.assert_equal(left='Hello World!', right=string_1)

    string_1 *= 2
    ap.assert_equal(left='Hello World!Hello World!', right=string_1)

    string_4: ap.String = ap.String('Hello!')
    boolean_1: ap.Boolean = ap.Boolean(False)
    with ap.If(boolean_1, locals_=locals(), globals_=globals()):
        string_4 += ' World!'
    ap.assert_equal(left='Hello!', right=string_4)

    with ap.If(boolean_1, locals_=locals(), globals_=globals()):
        string_4 *= 3
    ap.assert_equal(left='Hello!', right=string_4)

    string_5: ap.String = ap.String('Hello!')
    options: _Str5Options = {'string_5': string_5}
    stage.click(on_stage_clicked, options=options)

    string_6: ap.String = ap.String('1970-01-05')
    ap.assert_true(value=string_6 == '1970-01-05')
    ap.assert_true(value=string_6 != '1970-01-03')
    ap.assert_true(value=string_6 < '1970-01-06')
    ap.assert_true(value=string_6 <= '1970-01-05')
    ap.assert_true(value=string_6 > '1970-01-04')
    ap.assert_true(value=string_6 >= '1970-01-05')

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_stage_clicked(e: ap.MouseEvent, options: _Str5Options) -> None:
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
    string_5: ap.String = options['string_5']
    string_5.value = 'World!'
    ap.assert_true(string_5 == 'World!')
    ap.assert_true(string_5 != 'Hello!')
    string_5.value = '1970-01-05'
    ap.assert_true(string_5 < '1970-01-06')
    ap.assert_true(string_5 <= '1970-01-05')
    ap.assert_true(string_5 > '1970-01-04')
    ap.assert_true(string_5 >= '1970-01-05')


if __name__ == '__main__':
    main()
