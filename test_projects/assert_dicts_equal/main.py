"""Test project for `assert_dicts_equal` and `assert_dicts_not_equal`
interfaces.

Command examples:
$ python test_projects/assert_dicts_equal/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(background_color='#333')

    ap.assert_dicts_equal(
        left={'a': 10}, right=ap.Dictionary({'a': 10}))
    ap.assert_dicts_equal(
        left=ap.Dictionary({'a': 10}), right={'a': 10})
    ap.assert_dicts_equal(
        left={'a': 10}, right={'a': 10})
    ap.assert_dicts_equal(
        left=ap.Dictionary({'a': 10}), right=ap.Dictionary({'a': 10}))

    ap.assert_dicts_not_equal(
        left={'a': 10}, right=ap.Dictionary({'a': 11}))
    ap.assert_dicts_not_equal(
        left=ap.Dictionary({'a': 10}), right={'a': 11})
    ap.assert_dicts_not_equal(
        left={'a': 10}, right={'a': 11})
    ap.assert_dicts_not_equal(
        left=ap.Dictionary({'a': 10}), right=ap.Dictionary({'a': 11}))

    ap.assert_equal(
        left={'a': 10}, right=ap.Dictionary({'a': 10}))

    ap.assert_not_equal(
        left={'a': 10}, right=ap.Dictionary({'a': 11}))

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
