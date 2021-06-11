"""Test project for `assert_dicts_equal` and `assert_dicts_not_equal`
interfaces.

Command examples:
$ python test_projects/assert_dicts_equal/main.py
$ python assert_dicts_equal/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Dictionary
from apysc import Stage
from apysc import assert_dicts_equal
from apysc import assert_dicts_not_equal
from apysc import assert_equal
from apysc import assert_not_equal
from apysc.file import file_util
from apysc.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: Stage = Stage(background_color='#333')

    assert_dicts_equal(
        expected={'a': 10}, actual=Dictionary({'a': 10}))
    assert_dicts_equal(
        expected=Dictionary({'a': 10}), actual={'a': 10})
    assert_dicts_equal(
        expected={'a': 10}, actual={'a': 10})
    assert_dicts_equal(
        expected=Dictionary({'a': 10}), actual=Dictionary({'a': 10}))

    assert_dicts_not_equal(
        expected={'a': 10}, actual=Dictionary({'a': 11}))
    assert_dicts_not_equal(
        expected=Dictionary({'a': 10}), actual={'a': 11})
    assert_dicts_not_equal(
        expected={'a': 10}, actual={'a': 11})
    assert_dicts_not_equal(
        expected=Dictionary({'a': 10}), actual=Dictionary({'a': 11}))

    assert_equal(
        expected={'a': 10}, actual=Dictionary({'a': 10}))

    assert_not_equal(
        expected={'a': 10}, actual=Dictionary({'a': 11}))

    exporter.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
